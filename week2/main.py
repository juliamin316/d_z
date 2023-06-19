from datetime import datetime

user_id_generator = 0
chat_id_generator = 0
message_id_generator = 0


class User:
    def __init__(self, u_id, username):
        self.id = u_id
        self.username = username
        self.created_at = datetime.now()

    def set_id(self, u_id):
        self.id = u_id


class Chat:
    def __init__(self, c_id, name, users):
        self.id = c_id
        self.name = name
        self.users = users
        self.created_at = datetime.now()

    def set_id(self, c_id):
        self.id = c_id

    def add_new_message(self, message):
        pass


class Message:
    def __init__(self, m_id, c_id, author_id, text):
        self.id = m_id
        self.chat_id = c_id
        self.author_id = author_id
        self.text = text
        self.created_at = datetime.now()

    def set_id(self, m_id):
        self.id = m_id


class UserStorage:
    def __init__(self):
        self.__RECORDS = {}

    def get_user(self, u_id):
        return self.__RECORDS.get(u_id, None)

    def add_user(self, user):
        global user_id_generator
        user_id_generator += 1
        user.set_id(user_id_generator)
        self.__RECORDS[user_id_generator] = user
        return user


class ChatStorage:
    def __init__(self):
        self.__RECORDS = {}

    def get_chat(self, c_id):
        return self.__RECORDS.get(c_id, None)

    def add_chat(self, chat):
        global chat_id_generator
        chat_id_generator += 1
        chat.set_id(chat_id_generator)
        self.__RECORDS[chat_id_generator] = chat
        for user in chat.users:
            user.add_new_chat(chat)
        return chat


class MessageStorage:
    def __init__(self):
        self.__RECORDS = {}

    def get_message(self, m_id):
        return self.__RECORDS.get(m_id, None)

    def add_message(self, chat, author, text):
        global message_id_generator
        message_id_generator += 1
        message = Message(message_id_generator, chat.id, author.id, text)
        self.__RECORDS[message_id_generator] = message
        author.add_new_message(message)
        chat.add_new_message(message)
        return message


class UserService:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def create_user(self, username: str):
        user = User(None, username)
        return self.user_storage.add_user(user)


class ChatService:
    def __init__(self, user_storage: UserStorage, chat_storage: ChatStorage):
        self.user_storage = user_storage
        self.chat_storage = chat_storage

    def create_chat(self, name: str, users_ids: list):
        users = [self.user_storage.get_user(user_id) for user_id in users_ids]
        chat = Chat(None, name, users)
        return self.chat_storage.add_chat(chat)

    def get_user_chats(self, user_id: int):
        user = self.user_storage.get_user(user_id)
        chats = [chat for chat in self.chat_storage.__RECORDS.values() if user in chat.users]
        return sorted(chats, key=lambda c: c.created_at)


class MessageService:
    def __init__(self, user_storage: UserStorage, chat_storage: ChatStorage, message_storage: MessageStorage):
        self.user_storage = user_storage
        self.chat_storage = chat_storage
        self.message_storage = message_storage

    def send_message(self, from_user_id: int, to_chat_id: int, text: str):
        user = self.user_storage.get_user(from_user_id)
        chat = self.chat_storage.get_chat(to_chat_id)
        assert user in chat.users, "User is not a member in chat"
        self.message_storage.add_message(chat, user, text)

    def get_messages_in_chat(self, chat_id: int):
        chat = self.chat_storage.get_chat(chat_id)
        messages = [message for message in self.message_storage.__RECORDS.values() if message.chat_id == chat.id]
        return sorted(messages, key=lambda m: m.created_at, reverse=True)
