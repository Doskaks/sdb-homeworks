#!/usr/bin/env python
# coding=utf-8
import pika

# Добавляем такую же аутентификацию
credentials = pika.PlainCredentials('admin', 'admin')

parameters = pika.ConnectionParameters(
    host='192.168.88.11',
    port=5672,
    virtual_host='/',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Объявляем ту же очередь
channel.queue_declare(queue='hello (rmq02)')

print(' [*] Ожидание сообщений. Для выхода нажмите CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Получено: {body.decode()}")

# Исправляем вызов basic_consume (правильный порядок аргументов)
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True  # вместо no_ack=True в новой версии pika
)

channel.start_consuming()