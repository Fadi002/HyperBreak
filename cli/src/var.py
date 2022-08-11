import random,string
class HyperBreak_name_gen:
    def __init__(self):
        self.methods = [self.get_random,self.random_string,self.scream,self.l_and_i,self.single_letter_a_lot]
    def get_random(self, id=1):
        return random.choice(self.generator_options)(id)
    def random_string(self, id=1, length=70):
        return "".join(random.choice(string.ascii_letters) for i in range(length)) + str(id)
    def l_and_i(self, id=1):
        return "".join(random.choice("Il") for i in range(id))
    def scream(self, id=1):
        return "".join(random.choice("Aa") for i in range(id))
    def single_letter_a_lot(self, id=1):
        return random.choice(string.ascii_letters) * id