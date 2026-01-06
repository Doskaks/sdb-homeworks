#!/usr/bin/env python
# coding=utf-8
import pika
import time

credentials = pika.PlainCredentials('admin', 'admin123')
parameters = pika.ConnectionParameters('192.168.88.10', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(5):
    message = f'Сообщение #{i+1} от producer'
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Отправлено: {message}")
    time.sleep(1)

connection.close()
print("✅ Все сообщения отправлены!")