class node:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Data: {self.data}"


n1 = node(4)

print(n1)