class Message:
    def __init__(self, role='system', content='') -> None:
        self.role = role
        self.content = content
