from kafka import KafkaConsumer
import json

class KafkaConsumerClient:
    def __init__(self, topic, brokers):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=brokers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            group_id="django-consumer-group",
            auto_offset_reset="earliest"  # Start from the beginning of the topic
        )

    def consume_messages(self):
        """Continuously listen for messages from the topic."""
        print("Listening for messages...")
        for message in self.consumer:
            print(f"Received: {message.value}")

# Example usage
if __name__ == "__main__":
    consumer = KafkaConsumerClient(topic="gg", brokers=["localhost:29092", "localhost:39092"])
    consumer.consume_messages()
