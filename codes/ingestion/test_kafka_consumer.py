from kafka import *
import os
import time

my_kafka = KafkaClient("ec2-54-67-92-5.us-west-1.compute.amazonaws.com:9092")

consumer = SimpleConsumer(my_kafka, "consumer", "test",  max_buffer_size=999999999999)

is_log_empty = True

time_stamp = time.strftime('%Y%m%d%H%M%S')
temp_file_path = "/home/ubuntu/data/temp{0}.dat".format(time_stamp)
temp_file = open(temp_file_path, "w")
messages = consumer.get_messages(count=10000, block=False)

while True:
    if not messages:
        break
    for message in messages:
        is_log_empty = False
        temp_file.write(message.message.value + "\n")
    if temp_file.tell() > 10000000:   # 10 MB
        temp_file.close()
        os.system("sudo -u hdfs hdfs dfs -put {0} /data/".format(temp_file_path))
        time_stamp = time.strftime('%Y%m%d%H%M%S')
        temp_file_path = "/home/ubuntu/data/temp{0}.dat".format(time_stamp)
        temp_file = open(temp_file_path, "w")
    consumer.commit()
