from multiprocessing import Pool
from time import time

count = 500_000_000


def countdown(process_number, start_number, end_number):
    n = start_number
    while n < end_number:
        n += 1
    print(f'{process_number=} done: from {start_number} to {end_number} iterations ({end_number - start_number})')


if __name__ == '__main__':
    process_number = 10
    pool = Pool(processes=process_number)
    for i in range(process_number):
        pool.apply_async(
            countdown,
            kwds=dict(
                process_number=i,
                start_number=count // process_number * i,
                end_number=count // process_number * (i + 1),
            ),
        )

    start_time = time()
    pool.close()
    pool.join()
    end_time = time()

    print(f'Took {end_time - start_time} seconds')

# Race condition, deadlock
