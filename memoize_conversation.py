#define the memoize_string function
def memoize_string(string):
    memo = {}
    for index, char in enumerate(string):
        if char not in memo: 
            memo[char] = []
        memo[char].append((0, index))
    return memo

# this is the conversation text
conversation = \"\""
User: what can zapier let you do?
Assistant: Zapier is a powerful tool that allows you to automate tasks between different web apps. It's essentially a bridge that enables different applications to communicate and perform tasks without any manual intervention. Here are some of the things you can do with Zapier...\"\""

# memoize the conversation
memo = memoize_string(conversation)
print(memo)