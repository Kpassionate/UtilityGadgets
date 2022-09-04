import time
from concurrent.futures import ThreadPoolExecutor


def fun(index):
    print(index)
    time.sleep(3)


pool = ThreadPoolExecutor(max_workers=200)
for i in range(1000):
    pool.submit(fun, i)
pool.shutdown(wait=True)
