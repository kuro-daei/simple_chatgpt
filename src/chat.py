from message import Message


class Chat:
    def __init__(self, model='gpt-3.5-turbo', temperature=0.0, content=None) -> None:
        self.title = None
        self.model = model
        self.temperature = temperature
        self.messages = []
        if content is not None:
            message = Message(content=content, role='user')
            self.messages.append(message)
            self.title = content
