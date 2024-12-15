class Elf():
    population = 0

    def __init__(self, name,health):
        self.ear = 'long'
        self.name = name
        self.health = health
        Elf.population += 1
    def arrow(self):
        print('=====슝=====>')

    def talk(self):
        print(f'이몸은 {self.name}님이시다!')

e1 = Elf('legolas', 100)
e2 = Elf('smeagol', 100)
e2.ear = 'short'
print(e1.ear, e2.ear)
e2.talk()
