from letter import Letter

class Bob:
    def __init__(self, waiting, a_letterbox, b_letterbox):
        """
        Bob enjoys writing letters to Alice and reading her responses <3

        :param waiting: bool representing if Bob is waiting for a letter from Alice
        :param a_letterbox: Alice's letterbox object
        :param b_letterbox: Bob's letterbox object
        """
        self.waiting_response = waiting
        self.received_letters = []
        self.bob_letterbox = b_letterbox
        self.alice_letterbox = a_letterbox

    def write_letter(self):
        """
        Writes a letter and puts it in Alice's letterbox.
        This method will require user input for the content of the letter.
        Prints out a string to show success.
        """
        if not self.waiting_response:
            content = input("Enter the content of the letter to Alice > ")
            print("Bob wrote a letter for Alice")
            letter = Letter(content)
            self.put_letter_in_letterbox(letter)
        else:
            print("")
            return

    def put_letter_in_letterbox(self, letter):
        """
        Puts the letter into Alice's letterbox.
        Sets waiting bool to True.
        Prints out a string to show success

        :param letter: A letter object
        """
        self.alice_letterbox.receive_letter(letter)
        self.waiting_response = True
        print("Bob delivered the letter to Alice's letterbox")

    def check_letter_box(self):
        """
        Checks if Bob is waiting for a letter

        if True: Bob checks if his letterbox's flag is up
                if True: Print out a string.
                Take the letter and store it in the received letter list.
                Set waiting to False.
                Read the letter.

                if False: Print out a string
        if False: Bob will write a letter
        """
        if self.waiting_response:
            print("Bob checked his letterbox")
            if self.bob_letterbox.flag:
                print("And found a letter!!")
                received_letter = self.bob_letterbox.letter_taken()
                self.received_letters.append(received_letter)
                self.waiting_response = False
                self.read_letter(received_letter)
            else:
                print("And found no letters")
        else:
            self.write_letter()

    def read_letter(self, letter):
        """
        Bob reads the letter and tells it to mark itself as read.

        :param letter: A letter object
        """
        if not letter.return_read_status():
            print("Bob read the letter")
            letter.mark_as_read()
        else:
            return


