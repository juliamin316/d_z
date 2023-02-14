from datetime import datetime
class User:
    def __init__(self, u_id, username):
        self.id = u_id
        self.username = username
        self.created_at = datetime.datetime.now() 
        
class Chat:
    def __init__(self, c_id, name, users):
        self.id = c_id
        self.name = name
        self.users = users
        self.created_at = datetime.datetime.now() 
        
class Message:
    def __init__(self, m_id, c_id, author_id, text):
        self.id = m_id
        self.chat   = c_id
        self.author = author_id
        self.text = text
        self.created_at = datetime.datetime.now() 
        
class UserStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_user(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_user(self, user):
        global user_id_generator
        user_id_generator += 1 
        user.set_id(user_id_generator)
        self.__RECORDS[user_id_generator] = user
        return user.id 
        
class ChatStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_chat(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_chat(self, chat):
        global chat_id_generator
        chat_id_generator += 1
        chat.set_id(chat_id_generator)
        self.__RECORDS[chat_id_generator] = chat
        for user in chat.users:
            user_storage.get_user(user).add_new_chat(chat)
        return chat.id

class MessageStorage:
    def __init__(self):
        self.__RECORDS = {}
    
    def get_message(self, id):
        return self.__RECORDS.get(id, None)
    
    def add_message(self, message):
        global message_id_generator
        message_id_generator += 1 
        message.set_id(message_id_generator)
        self.__RECORDS[message_id_generator] = message
        user = message.author_id
        chat = message.chat_id
        user_storage.get_user(user).add_new_message(message)
        chat_storage.get_chat(chat).add_new_message(message)
        return message.id 
        
class UserService:
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def create_user(self, username: str):
        return self.user_storage.add_user(username).id

class ChatService:
    def __init__(self, user_storage: UserStorage, chat_storage: ChatStorage):
        self.user_storage = user_storage
        self.chat_storage = chat_storage
    
    def create_chat(self, name: str, users_ids: list[int]):
        users = [self.user_storage.get_user(user_id) for user_id in users_ids]
        return self.chat_storage.add_chat(name, users).id
    
    def get_user_chats(self, user_id: int):
        user = self.user_storage.get_user(user_id)
        chats = self.chat_storage.get_chats_for_user(user)
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
        messages = self.message_storage.get_messages_in_chat(chat)
        return sorted(messages, key=lambda m: m.created_at, reverse=True)
