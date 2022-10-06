import string
import random


class Password:

    def __init__(self, charset, length):

        self.charset = charset
        self.length = length
        self.characters = []
        self.password = []

    def set_charset(self):

        if ('l' in self.charset):
            self.characters.append(string.ascii_lowercase)

        if ('u' in self.charset):
            self.characters.append(string.ascii_uppercase)

        if ('d' in self.charset):
            self.characters.append(string.digits)

        if ('s' in self.charset):
            self.characters.append(string.punctuation)

    def characters(self):

        return self.characters

    def gen_pass(self):

        # print(self.characters)
        for i in range(self.length):
            out_list = random.randrange(0, len(self.characters))
            in_list = random.randrange(0, len(self.characters[out_list]))
            self.password.append(self.characters[out_list][in_list])

    def get_pass(self):

        return ''.join(self.password)
