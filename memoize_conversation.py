# Dylan Kenneth Eliot & GPT-3.5-turbo

from base64 import b64encode as encoder, b64decode as decoder

"""
It takes a string in, encodes it as base64, then assigns it to a tuple in a list. The keys in memo are the parts of the string.

To get the original string back, you need the dictionary that memoize_string gives you.


GPT-4 did the work of writing and uploading it successfully.

"""


def dememoize_string(memo):
    characters = []
    for char, indices in memo.items():
        for _, index in indices:
            characters.append((index, char))
    characters.sort()
    return decoder(''.join(char for _, char in characters)).decode('utf-8')
def memoize_string(string):
    memo = {}
    for index, char in enumerate(string):
        if char not in memo: 
            memo[char] = []
        memo[char].append((0, index))
    return memo
