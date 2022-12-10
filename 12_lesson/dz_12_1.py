import concurrent.futures
# from multiprocessing import Process, Pool
import time

def fact(a):
    n = 1
    for i in range(1, a + 1):
        n = n * i
    return n


arr_pr = []


def process():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for n in range(1000):
            future = executor.submit(fact, n)
            arr_pr.append(future.result())


arr_th = []


def thread():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for n in range(1000):
            future = executor.submit(fact, n)
            arr_th.append(future.result())


if __name__ == '__main__':
    ti = time.time()
    process()
    time_process = time.time() - ti
    print("time of ProcessPoolExecutor = {}".format(time_process))

    tn = time.time()
    thread()
    time_thread = time.time() - tn
    print("time of ThreadPoolExecutor  = {}".format(time_thread))
    if time_thread < time_process:
        print("Thread is faster than process in {} times".format(time_process / time_thread))
    else:
        print("Process is faster than thread in {} times".format(time_thread / time_process))









