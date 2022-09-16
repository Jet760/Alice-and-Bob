from person import Person
from charli import Charli
from letterbox import Letterbox


def main():
    alice_letterbox = Letterbox()
    bob_letterbox = Letterbox()
    po_letterbox = Letterbox()
    bob = Person("Bob", False, "alice", bob_letterbox, po_letterbox)
    alice = Person("Alice", True, "bob", alice_letterbox, po_letterbox)
    charli = Charli(po_letterbox, alice_letterbox, bob_letterbox)

    bob.check_letter_box()
    charli.check_post_office()
    alice.check_letter_box()


if __name__ == '__main__':
    main()
