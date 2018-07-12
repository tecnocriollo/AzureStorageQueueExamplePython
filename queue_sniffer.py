from azure.storage.queue import QueueService

queue_service = QueueService(account_name='xxx', account_key='xxx')

print("messages from queue 01")
messages = queue_service.peek_messages('queue01')
for message in messages:
    print(message.content)

print("")
print("messages from queue 02")
messages = queue_service.peek_messages('queue02')
for message in messages:
    print(message.content)