"""         @author:            Guang Yang
            @mktime:            2/8/2015
            @description:       Reads from ggtracker recent matches api and
                                puts in kafka
"""

import requests
from kafka import *
import time


def send_messages_to_kafka():
    try:
        recent_matches = requests.get("http://api.ggtracker.com/api/v1/matches")
        recent_matches_json = recent_matches_raw.json()['collection']

        for recent_match in recent_matches:
            producer.send_messages(KAFKA_TOPIC, json.dumps(recent_match))

        time.sleep(SLEEP_TIMER)

    except Exception, e:
        print(e)
        kafka.close()


i = 0
while True:
    i = i + 1
    producer.send_messages("test", str(i))
end


if __name__ == "__main__":
    my_kafka = KafkaClient("ec2-54-67-92-5.us-west-1.compute.amazonaws.com:"
                           "9092")
    producer = SimpleProducer(my_kafka)
    SLEEP_TIMER = 1         # in seconds
    KAFKA_TOPIC = "recent_matches"
    send_messages_to_kafka()
