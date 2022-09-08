class Letterbox:
    def __init__(self):
        self.flag = False
        self.stored_letters = []

    def receive_letter(self, letter):
        self.stored_letters.append(letter)
        self.flag = True

    def letter_taken(self):
        letter = self.stored_letters[-1]
        self.flag = False
        return letter
