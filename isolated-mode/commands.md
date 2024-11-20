# Commands

## Table of Contents

1. [Run Docker](#run-docker)
1. [Topics](#topics)
2. [Producer](#producer)
3. [Consumer](#consumer)
4. [Consumer Groups](#consumer-groups)
5. [KRaft](#kraft)

## Run Docker
to up the server

```bash
docker-compose up --build
```

then after that you can use the following commands in new terminal.

## Topics

To create a new topic

```bash
kafka-topics --create --topic <TOPIC_NAME> --bootstrap-server localhost:29092
```

By default the partition is set to 1 and the replication factor is set to 1. You can specify certain partition and replication factor by

```bash
kafka-topics --create --topic <TOPIC_NAME> --bootstrap-server localhost:29092 --partitions 1 --replication-factor 1

```

To list the topics

```bash
kafka-topics --list --bootstrap-server localhost:29092
```

To describe a topic

```bash
kafka-topics --describe --topic <TOPIC_NAME> --bootstrap-server localhost:29092
```

To delete a topic

```bash
kafka-topics --delete --topic <TOPIC_NAME> --bootstrap-server localhost:29092
```

## Producer

To produce messages to the topic

```bash
kafka-console-producer --topic <TOPIC_NAME> --bootstrap-server localhost:29092
```

**NOTE:** By default if there is no topic exist as you specified then Kafka will create that topic with the default partitions and replication factors mentioned in the `server.properties` You can edit the default configurations at `kafka/config/server.properties`

We can set different Acknowledgement level by

```bash
kafka-console-producer --topic <TOPIC_NAME> --bootstrap-server localhost:29092 --producer-property acks=all
```

## Consumer

To consume the topic

```bash
kafka-console-consumer --topic <TOPIC_NAME> --bootstrap-server localhost:29092
```

By default it will start consuming the message after the above command executed. If need to consume from the beginning

```bash
kafka-console-consumer --topic <TOPIC_NAME> --bootstrap-server localhost:29092 --from-beginning
```

To have a consumer inside a group

```bash
kafka-console-consumer --topic <TOPIC_NAME> --bootstrap-server localhost:29092 --group log-application-group-1
```

## Consumer Groups

To list all the consumer groups

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --list
```

To describe a consumer group

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --describe --group <CONSUMER_GROUP>
```

By this command we can check the current offset of the consumer group, the lag and the log offset. 

To reset the offset of a consumer group

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --group <CONSUMER_GROUP> --reset-offsets --to-earliest --execute --topic first_topic
```

This command will reset the offset for a specific topic. To reset for all topics

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --group <CONSUMER_GROUP> --reset-offsets --to-earliest --execute --all-topics
```

To go before 2 offset

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --group <CONSUMER_GROUP> --reset-offsets --shift-by -2 --execute --all-topics
```

If provided positive number it will shift forward and a negative number will shift backward

To delete a consumer group

```bash
kafka-consumer-groups --bootstrap-server localhost:29092 --delete --group <CONSUMER_GROUP>
```

**NOTE:** You can’t delete a consumer group when it is active

## KRaft

To describe the KRaft `meta.properties`

```bash
kafka-metadata-quorum --bootstrap-server localhost:29092 describe --status
```

To dump the log file for debugging

```bash
kafka-dump-log --cluster-metadata-decoder --files <PATH_TO_LOG>
```