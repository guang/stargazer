[![][stargazer_logo]][website]
====================
Project for Data Engineering Fellowship at Insight Data Science '15A

Questions and comments welcome at gy8 [AT] berkeley [DOT] edu

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
- [Background](#background)
- [Motivation](#motivation)
- [Data](#data)
  - [Historical](#historical)
  - [Realtime](#realtime)
- [Pipeline](#pipeline)
  - [Batch Processing](#batch-processing)
  - [Stream Processing](#stream-processing)
  - [API](#api)



## Overview
Stargazer is a data pipeline that serves up aggregated map statistics from a massive amount of
player-submitted replay files - leveraging Kafka for ingestion, Avro for serialization,
Spark Streaming for stream processing, Spark SQL for batch processing, Cassandra for
data storage and Flask for front-end API.


## Getting Started

### Usage
##### Before you begin, I assume you have:
  1. set up a hadoop cluster where you run ingestion and processing (Kafka, HDFS, Spark) after
    installing required dependencies (pretty much everything except Cassandra)

  2. set up a cassandra cluster (you
    do not need the dependencies you have installed for the hadoop cluster)

  3. cloned this repo on your master node in the hadoop cluster


##### To start the Kafka producer that pulls recent matches from GGtracker API:

  1. ssh into the master node of your hadoop cluster

    ```
    $ ssh -i ~/.ssh/YO_PEM_KEY.pem ubuntu@ec2-XX-XX-XX-X.us-west-1.compute.amazonaws.com
    ```

  2. double check zookeeper is running

    ```
    $ cd /opt/cloudera/parcels/CDH-5.3.0-1.cdh5.3.0.p0.30/bin
    $ sudo ./zookeeper-server status
    ```

  3. start up Kafka server (you should run this in the background via tmux as
    it will lock your terminal)

    ```
    $ ./stargazer/codes/ingestion/start_kafka_server.sh
    ```

  4. start running the Kafka producer

    ```
    $ python stargazer/codes/ingestion/produce_recent_matches.py
    ```


##### To start Spark Streaming:

  1. ssh into the master node of your hadoop cluster

    ```
    $ ssh -i ~/.ssh/YO_PEM_KEY.pem ubuntu@ec2-XX-XX-XX-X.us-west-1.compute.amazonaws.com
    ```

  2. change directory into SparkStreaming

    ```
    $ cd stargazer/codes/streaming/StreamProcessing
    ```

  3. package dependencies:

    ```
    $ sbt assembly
    ```

  4. do a little compilin':

    ```
    $ sbt package
    ```

  5. spark-submit and hope you do not see 3 pages of error messages start flowing:

    ```
    $ ./run_streamprocessing.sh
    ```

##### To do batch processing in Spark:

  1. ssh into the master node of your hadoop cluster

    ```
    $ ssh -i ~/.ssh/YO_PEM_KEY.pem ubuntu@ec2-XX-XX-XX-X.us-west-1.compute.amazonaws.com
    ```

  2. package dependencies, compile and spark-submit

    ```
    $ sbt assembly
    $ sbt package
    $ ./run_sparkcassie.sh
    ```

##### To check what is going on in your Cassandra:

  1. ssh into the seed node (node0 by default) of your cassandra cluster

    ```
    $ ssh -i ~/.ssh/YO_PEM_KEY.pem ubuntu@ec2-XX-XX-XX-X.us-west-1.compute.amazonaws.com
    ```

  2. fire up cassandra cql shell

    ```
    $ cqlsh
    ```

  3. create or view keyspaces and tables using
  [CQL commands](https://cassandra.apache.org/doc/cql3/CQL.html)


### Dependencies
Distribution:

- CDH (Cloudera Distribution Including Apache Hadoop): 5.3.0

Technologies:

- Spark (Spark SQL and Spark Streaming): 1.2.0

- Hadoop: 2.5.0

- Cassandra: 2.1.2

- Avro: 1.7.7

Third-party Libraries:

- [spark-cassandra-connector](https://github.com/datastax/spark-cassandra-connector): 1.2.0

- [spark-avro](https://github.com/databricks/spark-avro): 0.1


## Background
Starcraft II is a real-time strategy game released by Blizzard Entertainment in 2010.
In addition to having a large user base with 300,000 active players world wide, Starcraft II
has an exciting competitive scene - Just this last year, the finals of one of the top
tournaments, the World Champion Series, were broadcasted live on ESPN (not to mention
the $1.6 million total prize pool).

Gameplay centers around 1v1 matches: where each player builds bases to gather resources
in order to produce armies to eliminate his/her opponent. Players compete on the ladder
system for higher ranks. Many professional gamers (most play for sponsored teams) were
discovered for very high ranking on the ladder.

## Motivation
Map is an integral part of the Starcraft II gaming experience. All ranked ladder games are
played on a different set of maps each season. Many of these ladder maps are used in
international tournaments.

Designing a great map is inherently difficult: on one hand it has to offer
complexity with features that give an advantage to skilled players who really understands
the game dynamics; on the other hand it needs to be balanced across different play styles,
such as:

- Races (every player can choose to be either Terran, Protoss, or Zerg, each race with its
  unique units and strategies)
- Strategies (some players opt for early rush, some aim to out last their opponent in long, dragged out games)

It is especially difficult to measure how balanced a map is - rounds and rounds of beta testing
simply does not capture the whole picture. Currently, selecting which maps to be kept for the
new season is largely a *qualitative* process, where users vote on the maps that they like.
This naturally led to the question that I attempt to address with this project:
**What does game data reveal about map balance?**

## Data
All the data (JSON) come from API calls made against
[ggtracker.com](http://www.ggtracker.com/api).
Specifically, there are 3 types of data we can extract from each match submitted by
ggtracker users:

- meta-data about the match
  (match id, map name, winner, when the match ended, match duration, etc)

- snapshot of the game state taken every 10 seconds
  (current mineral/gas count, supply count, etc)

- game events triggered by players at different times
  (upgrades, scouting, aggressions, etc)

### Historical
For historical data, the above information are stored in
- [simple details](https://github.com/gy8/stargazer/raw/master/data/sample_matches_simple.json)
  (meta-data)
- [extended details](https://github.com/gy8/stargazer/raw/master/data/sample_matches_extended.json)
  (10 second snapshots and events triggered)

### Realtime
In terms of realtime data, the API does not offer real time streaming of the data but instead
gives a list of 10 most
[recent matches](https://github.com/gy8/stargazer/raw/master/data/sample_matches_recent.json)
submitted when you make the API call.

## Pipeline
![][stargazer_logo]



### Batch Processing
### Stream Processing
### API

[stargazer_logo]: https://github.com/gy8/stargazer/raw/master/images/stargazer_logo.jpg
[pipeline]: https://github.com/gy8/stargazer/raw/master/images/pipeline.jpg
[website]: http://stargazer.pw
