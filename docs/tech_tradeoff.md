Tradeoffs in Different Technologies
===================================

## Ingestion
### Trade-offs:
Consumption Quantity:

Order Guarantees:

### Kafka
- read call me maybe article
- designed for throughput
- needs Zookeeper
- http://www.quora.com/RabbitMQ-vs-Kafka-which-one-for-durable-messaging-with-good-query-features
- no message acknowledgements (hence Zookeeper)

- designed for both online and batch consumers
- designed for holding and distributing large volumes of messages



### RabbitMQ
- read call me maybe article
- http://www.quora.com/RabbitMQ-vs-Kafka-which-one-for-durable-messaging-with-good-query-features
- assumes consumers are mostly online


## File Format



## Batch



## Streaming
- Spark Streaming
- Storm


## Data Store
### Trade-offs:
Store types:
- Key/Value Based
- Column Based
- Document Based
- Graph Based

CA vs CP:
- AP (cassandra, riak, couchdb, dynamodb)
- CP (redis, hbase, mongoDB, bigtable)

### Technologies



## Front-End


## Other
### EC2 Instances
HVM (Hardware-assisted Virtual Machine) vs PV (Paravirtualization)

