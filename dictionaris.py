animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

'''
def how_many(aDict):

    sum = 0
    for animal in aDict:
        sum += len(aDict[a])
    return sum

print(how_many(animals))
'''

'''
def biggest(aDict):
    maxim = 0
    values = aDict.values()
    for v in values:
        if maxim < len(v):
            maxim = len(v)

    for a in aDict:
        if len(aDict[a]) == maxim:
            return a

    return None

print(biggest(animals))
'''


def fib(n, d):
    global num_calls
    num_calls += 1
    if n in d:
        return d[n]
    else:
        ans = fib(n - 1, d) + fib(n - 2, d)
        d[n] = ans
        return ans

d = {1: 1, 2: 2}
num_calls = 0
print(fib(10, d))
print(num_calls)
