# pika package required
import pika

# wait for connection before continuing 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# get the channel class
channel = connection.channel()
# declare queue in case doesnt exist
channel.queue_declare(queue='test_queue')
# define the callback function
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
# bind the callback function
channel.basic_consume(callback,
                  queue='test_queue',
                  no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# begin waiting for messages and consuming them
channel.start_consuming()