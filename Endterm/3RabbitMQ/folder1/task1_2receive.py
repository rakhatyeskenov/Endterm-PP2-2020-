import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, property, body):
   print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print(' [*] Wainting for messages. To exit press CTRL+C')
channel.start_consuming()
