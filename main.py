from alice import Alice
from bob import Bob
from letterbox import Letterbox


def main():
    alice_letterbox = Letterbox()
    bob_letterbox = Letterbox()
    bob = Bob(False, alice_letterbox, bob_letterbox)
    alice = Alice(True, bob_letterbox, alice_letterbox)

    bob.check_letter_box()
    alice.check_letter_box()


if __name__ == '__main__':
    main()
