from letter import Letter


class Alice:
    def __init__(self, waiting, b_letterbox, a_letterbox):
        self.waiting_response = waiting
        self.received_letters = []
        self.alice_letterbox = a_letterbox
        self.bob_letterbox = b_letterbox

    def write_letter(self):
        if not self.waiting_response:
            title = input("Enter the Title of the letter to Bob > ")
            print("Alice wrote a letter for Bob")
            letter = Letter(title)
            self.put_letter_in_letterbox(letter)
        else:
            print("")
            return

    def put_letter_in_letterbox(self, letter):
        self.bob_letterbox.receive_letter(letter)
        self.waiting_response = True
        print("Alice delivered the letter to Bob's letterbox")

    def check_letter_box(self):
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
        if not letter.return_read_status():
            print("Alice read the letter")
            letter.mark_as_read()
        else:
            return
