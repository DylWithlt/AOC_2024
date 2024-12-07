import itertools
import asyncio
from concurrent.futures import ProcessPoolExecutor
from tqdm.asyncio import tqdm
from functools import partial
from itertools import islice

opts = ["+", "*", "||"]


def read_input(file_path):
    with open(file_path, "r") as f:
        return [
            [
                int(line.split(":")[0]),
                list(map(int, line.split(":")[1].strip().split(" "))),
            ]
            for line in f
        ]


def chunked_iterable(iterable, chunk_size):
    iterator = iter(iterable)
    while chunk := list(islice(iterator, chunk_size)):
        yield chunk


def check_combos_sync(test_val, vals):
    for combo in chunked_iterable(itertools.product(opts, repeat=len(vals) - 1), 500):
        total = vals[0]
        for i, x in enumerate(vals[1:]):
            if total > test_val:
                break
            op = combo[i]
            if op == "+":
                total += x
            elif op == "*":
                total *= x
            elif op == "||":
                total = total * 10 ** len(str(x)) + x
        if total == test_val:
            return True
    return False


def check_combos_wrapper(args):
    test_val, vals = args
    return check_combos_sync(test_val, vals)


async def can_hit_target(test_val, vals, semaphore, pool):
    async with semaphore:
        loop = asyncio.get_running_loop()
        # Submit the task to a persistent pool
        return await loop.run_in_executor(pool, check_combos_wrapper, (test_val, vals))


async def main():
    data = read_input("./Day7/input.txt")
    semaphore = asyncio.Semaphore(20)
    pool = ProcessPoolExecutor()  # Persistent pool

    async def helper(dat):
        if await can_hit_target(dat[0], dat[1], semaphore, pool):
            return dat[0]
        return 0

    res = await tqdm.gather(*[helper(dat) for dat in data])
    pool.shutdown()  # Clean up the pool
    print(sum(res))


if __name__ == "__main__":
    asyncio.run(main())
