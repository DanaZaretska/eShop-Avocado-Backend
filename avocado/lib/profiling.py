import asyncio
import time


def timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **params)
        else:
            return func(*args, **params)

    async def helper(*args, **params):
        start = time.time()
        result = await process(func, *args, **params)
        end = time.time()
        print(
            f'"{func.__name__}" took {(end - start) * 1000:.3f} ms to execute'
        )
        return result

    return helper
