#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('admin', 'admin')

parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials 
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello, happy New Year Netology, from Nikolai!'
)
print("✅ Сообщение отправлено!")
connection.close()