from PIL import Image
from bitstring import Bits

class FingerPrint:
    def __init__(self, filename):
        self.filename = filename
        self._crop_file_box_center()
        self._read_wordlist()

    def get_seed_phrase(self):
        seed_bits = self._get_bits_for_seed_phrase()
        seed_phrase = self._get_seed_phrase(seed_bits)
        return seed_phrase

    def _crop_file_box_center(self):
        image_file = Image.open(self.filename)
        image_size = image_file.size
        image_center_box_coords = (
            image_size[0] / 4,
            image_size[1] / 4,
            image_size[0] - image_size[0] / 4,
            image_size[1] - image_size[1] / 4
        )
        cropped_image_file = image_file.crop(image_center_box_coords)
        cropped_image_file.save("test.png")

    def _get_bits_for_seed_phrase(self):
        image_bits = Bits(filename=self.filename)
        image_bits_half_len = int(len(image_bits) / 2)
        seed_bits = image_bits[image_bits_half_len:image_bits_half_len + 256]
        i = 0
        seed_bits_parsed = []
        while i < 256:
            seed_bits_parsed.append(seed_bits[i:i+11].uint)
            i += 11
        return seed_bits_parsed

    def _get_seed_phrase(self, seed_bits):
        seed_phrase = ""
        for seed_bit in seed_bits:
            seed_word = self.wordlist[seed_bit - 1].rsplit()[0] + " "
            seed_phrase += seed_word
        return seed_phrase[:-1]

    def _read_wordlist(self):
        with open("wordlist.txt", "r") as file:
            self.wordlist = file.readlines()
