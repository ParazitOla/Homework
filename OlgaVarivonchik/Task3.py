### Task 6.3 Implement The Keyword encoding and decoding for latin alphabet. The Keyword Cipher uses a Keyword
# to rearrange the letters in the alphabet. Add the provided keyword at the begining of the alphabet.
# A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
# Repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword
# matching to A, B, C etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used
# in alphabetical order, excluding those already used in the key.


class Cipher:
    base_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    new_alphabet = []
    word_to_encode = ''

    def __init__(self, keyword):
        self.key = keyword

        for letter in self.key:
            self.alphabet.remove(letter)
            self.new_alphabet.append(letter)
        self.new_alphabet.extend(self.alphabet)

    def encode(self, word_to_encode):
        answer = ''
        self.word_to_encode = word_to_encode
        for letter in self.word_to_encode:
            if letter.isalpha():
                position = self.base_alphabet.index(letter.lower())
                if letter == letter.upper():
                    answer += self.new_alphabet[position].upper()
                else:
                    answer += self.new_alphabet[position]
            else:
                answer += letter

        print(answer)

    def decode(self, word_to_encode):
        answer = ''
        self.word_to_encode = word_to_encode
        for letter in self.word_to_encode:
            if letter.isalpha():
                position = self.new_alphabet.index(letter.lower())
                if letter == letter.upper():
                    answer += self.base_alphabet[position].upper()
                else:
                    answer += self.base_alphabet[position]
            else:
                answer += letter

        print(answer)


cipher = Cipher("crypto")
cipher.encode("Hello world")
# "Btggj vjmgp"
cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"
