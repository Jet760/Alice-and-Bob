from letter import Letter


class Alice:
    def __init__(self, waiting, b_letterbox, a_letterbox):
        """
        Alice loves writing letters to Bob and reading his responses <3

        :param waiting: bool representing if Alice is waiting for a letter from Bob
        :param b_letterbox: Bob's letterbox object
        :param a_letterbox: Alice's letterbox object
        """
        self.waiting_response = waiting
        self.received_letters = []
        self.alice_letterbox = a_letterbox
        self.bob_letterbox = b_letterbox

    def write_letter(self):
        """
        Writes a letter and puts it in Bob's letterbox.
        This method will require user input for the content of the letter.
        Prints out a string to show success.
        """
        if not self.waiting_response:
            content = input("Enter the content of the letter to Bob > ")
            print("Alice wrote a letter for Bob")
            letter = Letter(content)
            self.put_letter_in_letterbox(letter)
        else:
            print("")
            return

    def put_letter_in_letterbox(self, letter):
        """
        Puts the letter into Bob's letterbox.
        Sets waiting bool to True.
        Prints out a string to show success.

        :param letter: A letter object
        """
        self.bob_letterbox.receive_letter(letter)
        self.waiting_response = True
        print("Alice delivered the letter to Bob's letterbox")

    def check_letter_box(self):
        """
        Checks if Alice is waiting for a letter

        if True: Alice checks if her letterbox's flag is up
                if True: Print out a string.
                Take the letter and store it in the received letter list.
                Set waiting to False.
                Read the letter.

                if False: Print out a string
        if False: Alice will write a letter
        """
        if self.waiting_response:
            print("Alice checked her letterbox")
            if self.alice_letterbox.flag:
                print("And found a letter!!")
                received_letter = self.alice_letterbox.letter_taken()
                self.received_letters.append(received_letter)
                self.waiting_response = False
                self.read_letter(received_letter)
            else:
                print("And found no letters")
        else:
            self.write_letter()

    def read_letter(self, letter):
        """
        Alice reads the letter and tells it to mark itself as read.

        :param letter: A letter object
        """
        if not letter.return_read_status():
            print("Alice read the letter")
            letter.mark_as_read()
        else:
            return
