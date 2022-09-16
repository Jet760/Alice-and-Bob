from letter import Letter


class Person:
    def __init__(self, name, waiting, recipient_of_letters, my_letterbox, po_letterbox):
        """

        :param waiting: bool representing if the person is waiting to receive a letter
        :param my_letterbox: This person's letterbox object
        :param po_letterbox: The post office's letterbox object
        """
        self.name = name
        self.waiting_response = waiting
        self.recipient_of_letters = recipient_of_letters.lower()
        self.received_letters = []
        self.my_letterbox = my_letterbox
        self.post_office_letterbox = po_letterbox

    def write_letter(self):
        """
        Writes a letter and puts it in the post office's letterbox.
        Prints out a string to show success.
        """
        if not self.waiting_response:
            content = "A letter for you!"
            print(f"{self.name} wrote a letter")
            letter = Letter(content, self.recipient_of_letters)
            letter.encrypt()
            print("The letter has been encrypted")
            self.put_letter_in_letterbox(letter)
        else:
            print("")
            return

    def put_letter_in_letterbox(self, letter):
        """
        Puts the letter into the post office's letterbox.
        Sets waiting bool to True.
        Prints out a string to show success.

        :param letter: A letter object
        """
        self.post_office_letterbox.receive_letter(letter)
        self.waiting_response = True
        print(f"{self.name} delivered the letter to the post office letterbox")

    def check_letter_box(self):
        """
        Checks if waiting for a letter

        if True: Person checks if their letterbox's flag is up
                if True: Print out a string.
                Take the letter and store it in the received letter list.
                Set waiting to False.
                Read the letter.

                if False: Print out a string
        if False: Person will write a letter
        """
        if self.waiting_response:
            print(f"{self.name} checked their letterbox")
            if self.my_letterbox.flag:
                print("And found a letter!!")
                received_letter = self.my_letterbox.letter_taken()
                self.received_letters.append(received_letter)
                self.waiting_response = False
                self.read_letter(received_letter)
            else:
                print("And found no letters")
        else:
            self.write_letter()

    def read_letter(self, letter):
        """
        Person reads the letter and tells it to mark itself as read.

        :param letter: A letter object
        """
        letter.decrypt()
        print(f"{self.name} decrypted the letter")
        if letter.check_if_readable():
            print(f"{self.name} read the letter")
            letter.mark_as_read()
        else:
            return
