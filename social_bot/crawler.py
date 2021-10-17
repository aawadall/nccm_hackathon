"""Social media crawler
TODO: Read from kafka stream and check ths score via incident analyzer
"""
from database import Database
from incident_analyzer import HateIncidentAnalyzer
from thresholds import *
import json

# Kafka
from kafka import KafkaConsumer
from kafka import KafkaProducer

# Global variables
topics = {
    "twitter": "twitter-feed",
    "response": "twitter-response",
    "human-feed": "human-feed",
}

kafka_cluster_address = 'localhost:29092'


def log_message(message):
    """Log message"""
    print(f'{message.value}')


def get_tweet(message):
    """Get tweet from message, assuming json content with tweet field"""
    return message['tweet']


def get_handle(message):
    """Get handle from message, assuming json content with handle field"""
    return message['handle']


def get_timestamp(message):
    """Get timestamp from message, assuming json content with timestamp field"""
    return message['timestamp']


def main():
    """Main function"""

    # Consumer
    consumer = KafkaConsumer(
        topics['twitter'],
        bootstrap_servers=[kafka_cluster_address],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: x.decode('utf-8')
    )

    # Human feed producer
    human_feed_producer = KafkaProducer(
        bootstrap_servers=[kafka_cluster_address],
        value_serializer=lambda x: x.encode('utf-8')
    )

    # Response producer
    response_producer = KafkaProducer(
        bootstrap_servers=[kafka_cluster_address],
        value_serializer=lambda x: x.encode('utf-8')
    )

    # Database init
    db = Database()
    ia = HateIncidentAnalyzer(hate_categories, 0.9)
    # Consumer loop
    for message in consumer:
        # log
        log_message(message)
        # get score vector
        tweet = get_tweet(json.loads(message.value))
        handle = get_handle(json.loads(message.value))
        timestamp = get_timestamp(json.loads(message.value))

        # store in database
        db.store_tweet(handle, timestamp, tweet)

        current_score = ia.analyze_incident(tweet)

        db.store_violation(handle, timestamp, current_score)

        # run time weighted analysis
        weighted_score = ia.time_weighted_analysis(db.get_violations(handle))

        # intial response
        initial_response = get_escalations(weighted_score)

        # if score is above threshold
        if (initial_response != None):
            # iterate through dictionary
            for key, value in initial_response.items():
                # send response to human feed
                human_feed_producer.send(
                    topic=topics['human-feed'],
                    value=value.response
                )

                # send response to response topic
                response_producer.send(
                    topic=topics['response'],
                    value=value.response
                )


if __name__ == '__main__':
    main()
