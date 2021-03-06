# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr


def cons(a, b):
    return lambda m: m(a, b)


def car(cons):
    return cons(lambda a, b: a)


def cdr(cons):
    return cons(lambda a, b: b)


print(car(cons(3, 4)))

# The solution they provided


def car1(pair):
    return pair(lambda a, b: a)


def cdr1(pair):
    return pair(lambda a, b: b)
