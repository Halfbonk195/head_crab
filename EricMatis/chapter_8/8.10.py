def send_messages(messages_list, sent_messages):
    while messages_list:
        message = messages_list.pop()
        sent_messages.append(message)
        print(message)


messages_list = ['hello', 'its', 'me', 'mario', 'I love Python!']
sent_messages = []
send_messages(messages_list, sent_messages)

for message in sent_messages:
    print(message)
