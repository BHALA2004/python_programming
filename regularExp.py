import re 

strings = "the way rain"

matching = re.search("ain",strings)
if matching:
    print(matching.group())

matcho = re.findall("a",strings)
print(matcho)

hey = re.sub("a","x",strings)
print(hey)
