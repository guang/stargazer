from kafka import *

my_kafka = KafkaClient("ec2-54-67-92-5.us-west-1.compute.amazonaws.com:9092")

producer = SimpleProducer(my_kafka)

i = 0
while True:
    i = i + 1
    producer.send_messages("test", str(i))
end
