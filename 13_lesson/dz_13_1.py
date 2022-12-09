import random
# from py_random_words import RandomWord


int_list = []
float_list = []
str_list = []

int_list = [random.randint(0, 1000) for a in range(5000)]
float_list = [random.uniform(0.1, 100) for a in range(5000)]

# rnd_word = RandomWords()
#
# print(rnd_word.get_word())
print(int_list)

print(float_list)