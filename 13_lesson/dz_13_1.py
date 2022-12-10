import random
from random_words import RandomWords


int_list = []
float_list = []
str_list = []

int_list = [random.randint(0, 1000) for a in range(5000)]
float_list = [random.uniform(0.1, 100) for a in range(5000)]
rw = RandomWords()
str_list = rw.random_words(count=5000)
#
print(str_list)
print(int_list)
print(float_list)

