# Azure Storage Queue Example For Python

 
## English

A simple example using Azure Store Queues For Python

You have to change the line below with your storage account name and storage account key from Azure Portal

queue_service = QueueService(account_name='xxx', account_key='xxx')

### Usage:
You have 4 files:

* queue_send.py - this script sends messages to two queues named queue01 and queue02
* queue_sniffer.py - this script reads and prints the last message from both queues, but dont' remove it
* queue_client01.py - this script reads and remove a message from queue01
* queue_client02.py - this script reads and remove a message from queue01

First import the Azure Storage Libs with (make sure you have pip installed first)

```
pip install azure
```
After that you can you queue_send to send messages to both queues, then review the last message using queue_sniffer, run the clients and run queue sniffer each time to watch that the message are removed from queue. Feel free to change the execution order of clients or try to send more messages.


## Español

Un ejemplo simple sobre el uso de Azure Queues

Debes cambiar la linea de más abajo con tu nombre de cuenta y clave de storage que se puede obtener desde portal AzureY

queue_service = QueueService(account_name='xxx', account_key='xxx')

### Uso:

Tienes 4 archivos:

* queue_send.py - este script envía mensajes a dos colas llamadas queue01 and queue02
* queue_sniffer.py - este script lee e imprime el último mensaje de las dos colas, pero no las quita
* queue_client01.py - este script lee y quita un mensaje de queue01
* queue_client02.py - este script lee y quita un mensaje de  queue01

Primero importar las libs de Azure Storage (asegúrate de que tienes instalado pip)

```
pip install azure
```
Luego de esto puedes usar queue_send para enviar mensajes a ambas colas, luego revisar los últimos mensajes de cada con queue_sniffer, ejecutar los clientes respectivos y volver a ejecutar queue_sniffer para ver que el último elemento de cada uno cambia. Siéntente libre de ir cambiando el orden de ejecución o agregar más mensajes.
