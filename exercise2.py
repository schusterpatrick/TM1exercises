import random
from matplotlib import pyplot as plt

NUMBER_STEPS = 1000000
class Flea:
    def __init__(self):
        self.spin = 1

    def change_spin(self):
        if self.spin == 1:
            self.spin = -1
        else:
            self.spin = 1

def initialize_spin_chain(number_spins):
    spin_chain = []
    for i in range(number_spins):
        flea = Flea()
        spin_chain.append(flea)
    return spin_chain

def change_random_spin(spin_chain):
    random.choice(spin_chain).change_spin()

def get_sum(spin_chain):
    sum = 0
    number = 0
    for flea in spin_chain:
        number +=1
        sum += flea.spin
    return sum, number, (sum -50)/(-2)


histogram = []
chain = initialize_spin_chain(50)
for j in range(NUMBER_STEPS):
    change_random_spin(chain)
    histogram.append(get_sum(chain)[2])
plt.plot(range(NUMBER_STEPS),histogram)
plt.show()



