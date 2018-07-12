from azure.storage.queue import QueueService

queue_service = QueueService(account_name='xxx', account_key='xxx')

messages = queue_service.get_messages('queue01', num_messages=1, visibility_timeout=5*60)
for message in messages:
    print(message.content)
    queue_service.delete_message('queue01', message.id, message.pop_receipt)
