import time

cache = {}


def memoization(num):
    if num in cache:
        print("cached")
        return cache[num]
    print("computing...")
    time.sleep(2)
    result = num*num
    cache[num] = result
    return result


print(memoization(4))
print(memoization(4))
print(memoization(4))
print(memoization(4))
