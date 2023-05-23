from azure.eventhub import EventHubProducerClient,EventData

connection_str = 'Endpoint=sb://stream-event-namespace.servicebus.windows.net/;SharedAccessKeyName=stream_hub_policy;SharedAccessKey=5aTyGxcTR8gTaIVVFDfHBzf1nC7kKhYZg+AEhEdQn2c='
eventhub_name = 'stream_event_hub'
client = EventHubProducerClient.from_connection_string(connection_str,eventhub_name = eventhub_name)
data = '{"ID":2,"Name":"Akash","City":"Delhi","Posts":3,"email":"xyx@gmail.com"}'

event_data_batch = client.create_batch()
event_data_batch.add(EventData(data))
with client:
    client.send_batch(event_data_batch)