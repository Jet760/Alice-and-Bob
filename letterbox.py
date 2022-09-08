class Letterbox:
    def __init__(self):
        """
        A letterbox object that can store letters.
        Has a flag that will go up when a letter is received, then go down when the letter is taken.
        """
        self.flag = False
        self.stored_letters = []

    def receive_letter(self, letter):
        """
        Adds the letter to the letter list and sets the flag to True.

        :param letter: A letter objectS
        """
        self.stored_letters.append(letter)
        self.flag = True

    def letter_taken(self):
        """
        Removes the last letter from the letter list and sets flag to false.

        :returns: letter object
        """
        letter = self.stored_letters[-1]
        self.flag = False
        return letter
