

from kafka import KafkaProducer
import json


class KafkaClient:
    def __init__(self, brokers):
        self.producer = KafkaProducer(
            bootstrap_servers=brokers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )

    def send_message(self, topic, message):
        """Send a message to a Kafka topic."""
        self.producer.send(topic, message)
        self.producer.flush()  # Ensure the message is sent

# Example usage
if __name__ == "__main__":
    kafka_client = KafkaClient(brokers=["localhost:29092", "localhost:39092"])
    kafka_client.send_message(topic="gg", message={"key": "ggggg"})
    print("Message sent to Kafka!")
