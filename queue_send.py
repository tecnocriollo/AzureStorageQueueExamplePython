from azure.storage.queue import QueueService

queue_service = QueueService(account_name='xxx', account_key='xxx')

queue_service.create_queue('queue01')
queue_service.create_queue('queue02')

queue_service.put_message('queue01', u'Hello World 1 to queue 1')
queue_service.put_message('queue02', u'Hello World 1 to queue 2')
queue_service.put_message('queue01', u'Hello World 2 to queue 1')
queue_service.put_message('queue02', u'Hello World 2 to queue 2')
queue_service.put_message('queue01', u'Hello World 3 to queue 1')
queue_service.put_message('queue02', u'Hello World 3 to queue 2')

