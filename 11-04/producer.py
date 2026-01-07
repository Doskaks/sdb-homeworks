#!/usr/bin/env python
# coding=utf-8
import pika

# Добавляем аутентификацию
credentials = pika.PlainCredentials('admin', 'admin')

# Используем правильный порт 5672 (а не 15672)
parameters = pika.ConnectionParameters(
    host='192.168.88.10',
    port=5672,
    virtual_host='/',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Создаем очередь 'hello'
channel.queue_declare(queue='hello')

# Исправляем: routing_key должно быть 'hello' (имя очереди), 
# а сообщение передается в параметре body
channel.basic_publish(
    exchange='',
    routing_key='hello (rmq01)',  # Имя очереди
    body='Hello, happy New Year Netology, from Nikolai!'  # Само сообщение
)

print("✅ Сообщение отправлено!")

connection.close()
