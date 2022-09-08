from alice import Alice
from bob import Bob
from letterbox import Letterbox

alice_letterbox = Letterbox()
bob_letterbox = Letterbox()
bob = Bob(False, alice_letterbox, bob_letterbox)
alice = Alice(True, bob_letterbox, alice_letterbox)

while True:
    alice.check_letter_box()
    bob.check_letter_box()


