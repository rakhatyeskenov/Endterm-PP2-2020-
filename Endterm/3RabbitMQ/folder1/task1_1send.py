# Hello world!

import pika

# connect with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# declare queue
channel.queue_declare(queue='hello')

# sending to exchange
channel.basic_publish(exchange='', routing_key='hello', body='Hello world!')
print("[x] sent 'Hello world!'")

connection.close()
