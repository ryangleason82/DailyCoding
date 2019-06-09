# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


from collections import defaultdict


# def numDecode(msg):
#     dict = {}
#     # I know there's a simple way to map each number to each letter
#     dict = {{1, 26}, {a, z}}
#     return 0


# Solution
# "", the empty string and the base case should return 1
# '1' should return 1 since we can parse it as "a" + ""
# "11" should return 2 since we can parse it as "a" + "a" + ""

# if the string starts with zero, then there's no valid encoding.
# if the string's length is less than or equal to 1, there is only 1 encoding
# if the first two digits form a number k that is less than or equal to 26,
#  we can recursively count the number of encodings assuming we pick k as a letter
# We can also pick the first digit as a letter and count the number of encodings with this assumption


def num_1encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:  # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total


# not efficient we can use dynamic programming


def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1  # Empty string is 1 valid encoding
   # print(cache)
    for i in reversed(range(len(s))):
        print(cache)
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]


print(num_encodings('111'))
