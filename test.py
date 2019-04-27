from fingerprint import FingerPrint
from crypto import *

finger_module = FingerPrint("pictures/finger.jpg")

if __name__ == "__main__":
    seed_phrase = finger_module.get_seed_phrase()
    print(generate_wallet(seed_phrase))
