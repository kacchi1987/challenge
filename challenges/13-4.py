class Horse:
    def __init__(self, name, breed, jockey):
        self.name = name
        self.breed = breed
        self.jockey = jockey

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("Yutaka Take")
horse = Horse("Max", "Sarabread", rider)

print(horse.jockey.name)
