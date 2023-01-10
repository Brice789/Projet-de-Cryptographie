from math import prod, floor, gcd
from collections.abc import Sequence

def products(*integers: int) -> list[list[int]]:
    """Tree with the root as the product, input as leaves and intermediate
       states as intermediate nodes"""
    xs = list(integers)
    result = [xs]
    while len(xs) > 1:
        xs = [prod(xs[i * 2: (i + 1) * 2]) for i in range((len(xs) + 1) // 2)]
        result.append(xs)
    return result

def batch_gcd(*integers: int) -> list[int]:
    xs = list(integers)
    tree = products(*xs)
    node = tree.pop()
    while tree:
        xs = tree.pop()
        node = [node[floor(i / 2)] % xs[i] ** 2 for i in range(len(xs))]

    res = []
    for r, n in zip(node, xs):
        res.append("GCD= " + str(gcd(r // n, n)) + ", r = " + str(r) + ", n = " + str(n))
    
    return res

counter = 0

result = []

with open("RSAkey.txt") as f:
    for line in f:
        key = int(line, base=16)
        result.append(key)
        counter += 1
        if counter == 100:
            break

result = batch_gcd(*result)

#after_batch = batch_gcd(*result) # send the result for batch gcd

with open("result.txt", "w") as f:
    for item in result:
        f.write("%s\n" % item)

# print(after_batch)


for item in result:
    print(item)
