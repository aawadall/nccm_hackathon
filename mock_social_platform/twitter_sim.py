"""Twitter simulator"""

import datetime
import json
import time
# Kafka imports
from kafka import KafkaProducer
from kafka import KafkaConsumer

# Global variables
topics = {
    "twitter": "twitter-feed",
    "response": "twitter-response",
    "human-feed": "human-feed",
}

kafka_cluster_address = 'localhost:29092'


def main():
    """Main function"""
    # Kafka producer
    producer = KafkaProducer(bootstrap_servers=kafka_cluster_address,
                             value_serializer=lambda v: v.encode('utf-8'))

    # Kafka consumer
    consumer = KafkaConsumer(
        topics['response'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='twitter-sim',
        bootstrap_servers=kafka_cluster_address
    )

    end_flag = False
    handle = input("Enter your twitter handle: ")

    # Twitter simulator
    while end_flag == False:
        # read tweets from console
        tweet = input("@"+handle + " Enter tweet: ")
        if tweet == "end":
            end_flag = True
        else:
            # make payload
            timestamp = str(datetime.datetime.now())

            payload = json.dumps({
                "tweet": tweet,
                "handle": handle,
                "timestamp": timestamp
            })

            print("Sending tweet: ", payload)
            # send payload to kafka
            producer.send(topics['twitter'], value=payload)

        # add some delay
        time.sleep(1)
        # peek messages from kafka
        msg = consumer.poll(timeout_ms=100)
        if msg:
            for topic, msg_list in msg.items():
                for msg in msg_list:
                    print("Received response: ", msg.value)
            consumer.commit()
        else:
            print("No response received")
        # # if any message at consumer, read one, delete and continue
        # if len(consumer.poll(timeout_ms=100)) > 0:
        #     print("reading tweet")
        #     for message in consumer:
        #         print("decoding")
        #         print("Response: ", message.value.decode('utf-8'))
        #         consumer.commit_async()

        # else:
        #     print("No response")


if __name__ == "__main__":
    print("Twitter simulator")
    main()
