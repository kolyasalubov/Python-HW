from random import choice
colors = ["white", "yellow", "purple", "red"]
class Ghost(object):
    def __init__(self):
         self.color = choice(colors)
