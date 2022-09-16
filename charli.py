class Charli:
    def __init__(self, po_letterbox, alice_letterbox, bob_letterbox):
        """
        Charli is a postie! They check the post office for letters and deliver them to Bob and Alice <3

        :param po_letterbox: Letterbox object
        :param alice_letterbox: Letterbox object
        :param bob_letterbox: Letterbox object
        """

        self.post_office_letterbox = po_letterbox
        self.alice_letterbox = alice_letterbox
        self.bob_letterbox = bob_letterbox
        self.letters = []

    def check_post_office(self):
        """
        Checks if the post office's letterbox's flag is up.

        if True: prints out a string.
            Takes the letter from the letterbox and puts it in the letter list.
            Delivers the mail.

        if False: prints a string
        """
        print("Charli checked the post office for letters")
        if self.post_office_letterbox.flag:
            print("And found a letter!")
            letter_for_delivery = self.post_office_letterbox.letter_taken()
            self.letters.append(letter_for_delivery)
            self.deliver_mail()

        else:
            print("And found no letters :(")
            print("Time to knock off")
            return

    def deliver_mail(self):
        """
        Delivers mail to the recipient specified in the letter object.
        """
        letter = self.letters[-1]
        recipient = letter.recipient
        print(f"The letter is addressed to {recipient}")
        if recipient == "bob":
            self.bob_letterbox.receive_letter(letter)
            print("Charli delivered the letter to Bob's letterbox")
        elif recipient == "alice":
            self.alice_letterbox.receive_letter(letter)
            print("Charli delivered the letter to Alice's letterbox")
        else:
            print("Charli didn't know the address for the recipient so has returned the letter to sender")
