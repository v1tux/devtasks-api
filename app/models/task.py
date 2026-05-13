class Task:
    def __init__(self, id: int, title: str, done: bool = False):
        self.id = id
        self.title = title
        self.done = done

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }