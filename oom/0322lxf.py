def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 返回布尔值
def _not_divisible(n):
    return lambda x:x % n > 0



def primes():
    yield 2
    it = _odd_iter()
    # yield next(it)
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

        # print("it: ",it)
for n in primes():
    if n < 10:
        print("P: ",n)
    else:
        break
