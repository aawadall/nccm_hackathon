# Chamberless Bot

## [Presentation](https://docs.google.com/presentation/d/1FAVXRjwxo2iMDFJoilPiqV6KywaZcZrwGougBtpsBIQ/edit#slide=id.g35f391192_00)
## [Wireframe](https://www.figma.com/file/JbrWA4GeySGL24eLduSvpF/Wireframes-for-online-hate-speech?node-id=0%3A1)

## Trying it out
to try this proof of concept, you need to have docker desktop installed on your machine 
also you need pyton 3 installed

### Start Kafka Cluster
open a terminal window and navigate to `infrastructure` folder then run the following command
```
docker-compose up
```
### Start Twitter Simulator 
open a terminal window and navigate to `mock_social_platform` folder and run the following command 
```
python ./twitter_sim.py
```
### Start Crawler 
open a terminal window and navigate to `social_bot` folder and run the following command 
```
python ./crawler.py
```

now you can send tweets and monitor hate level on bot and twitter simulator
