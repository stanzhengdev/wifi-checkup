# Imports the Google Cloud client library
from google.cloud import pubsub_v1
import speedtest
import time, json
import uuid;
computer=hex(uuid.getnode())
s = speedtest.Speedtest()
# Instantiates a client
publisher = pubsub_v1.PublisherClient()
# The resource path for the new topic contains the project ID
# Data must be a bytestring # and the topic name.
topic_path = publisher.topic_path('cloudreach-mars', 'firehose')

# Create the topic.
while True:
    s = speedtest.Speedtest(); _ = s.get_best_server(); _ = s.download();
    msg = s.results.dict()
    msg["computer_id"] = computer
    data = json.dumps(msg).encode()
    # Data must be a bytestring
    publisher.publish(topic_path, data=data)
    print (data)
    time.sleep(30)
