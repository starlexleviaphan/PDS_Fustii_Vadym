import random
from random_words import RandomWords
import time
from statistics import mean


int_list = []
float_list = []
str_list = []

int_list = [random.randint(0, 1000) for a in range(5000)]
float_list = [random.uniform(0.1, 100) for a in range(5000)]
rw = RandomWords()
str_list = rw.random_words(count=5000)
#
# print(str_list)
# print(int_list)
# print(float_list)

def bubble_sort(array):                                                  #bubble sort
    n = len(array)

    for i in range(n):

        already_sorted = True


        for j in range(n - i - 1):
            if array[j] > array[j + 1]:

                array[j], array[j + 1] = array[j + 1], array[j]


                already_sorted = False


        if already_sorted:
            break

    return array


def partition(nums, low, high):                                                         #quick sort
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

# def time_sort(array, attemts):
#     time_arr = []
#
#     for i in range(attemts):
#         temp_list = array
#         init = time.time()
#         bubble_sort(temp_list)
#         t = time.time() - init
#         time_arr.append(t)
#     summ = sum(time_arr)
#
#     mean = summ / len(time_arr)
#     return time_arr, mean
#
# list, avg_time = time_sort(str_list, 10)

def sort_meter(data, iterations):                                           #time measure

    timer = []
    for s in range(iterations):
        temp_list = data
        cur_time = time.time()
        quick_sort(temp_list)
        interval = time.time() - cur_time
        timer.append(interval)
    return mean(timer)

avg_time = sort_meter(str_list, 9)
print("avg time = {}".format(avg_time))

# t1 = time.time()
# sort = bubble_sort(float_list)
# t = time.time() - t1
# print(t)
