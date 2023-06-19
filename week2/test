def run_tests():
    user_storage = UserStorage()
    chat_storage = ChatStorage()
    message_storage = MessageStorage()

    # Создание пользователей
    user1 = UserService(user_storage).create_user("Alice")
    user2 = UserService(user_storage).create_user("Bob")
    user3 = UserService(user_storage).create_user("Charlie")

    # Проверка создания пользователей
    assert user1.username == "Alice"
    assert user2.username == "Bob"
    assert user3.username == "Charlie"

    # Создание чата
    chat_id = ChatService(user_storage, chat_storage).create_chat("Chat 1", [user1.id, user2.id, user3.id])

    # Проверка создания чата
    chat = chat_storage.get_chat(chat_id)
    assert chat.name == "Chat 1"
    assert user1 in chat.users
    assert user2 in chat.users
    assert user3 in chat.users

    # Отправка сообщений
    MessageService(user_storage, chat_storage, message_storage).send_message(user1.id, chat.id, "Hello, everyone!")
    MessageService(user_storage, chat_storage, message_storage).send_message(user2.id, chat.id, "Hi, Alice!")
    MessageService(user_storage, chat_storage, message_storage).send_message(user3.id, chat.id, "Hey there!")

    # Получение сообщений в чате
    messages = MessageService(user_storage, chat_storage, message_storage).get_messages_in_chat(chat.id)

    # Проверка полученных сообщений
    assert len(messages) == 3
    assert messages[0].text == "Hey there!"
    assert messages[1].text == "Hi, Alice!"
    assert messages[2].text == "Hello, everyone!"

    print("All tests passed!")


run_tests()
