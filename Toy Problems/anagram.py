# def allAnagrams(myString):
#     anagrams = []
#     def build(anchor,restOfString):
#         return
#     for i in range(len(myString)):
#         print(myString.pop(), myString)
#         build(myString.pop(), myString)
#         continue
#     return anagrams

# print(allAnagrams(['abc']))

# def generate_anagrams(word):
#     if len(word) <= 1:
#         return [word]
#     else:
#         anagrams = []
#         for perm in generate_anagrams(word[1:]):
#             for i in range(len(perm) + 1):
#                 anagrams.append(perm[:i] + word[0] + perm[i:])
#         return anagrams

# def find_anagrams(word_list):
#     all_anagrams = []
#     for word in word_list:
#         all_anagrams.extend(generate_anagrams(word))
#     return all_anagrams

# # Example usage:
# word_list = ["abc", "dog", "abcd"]
# print(find_anagrams(word_list))


# a
# ab
# abc
# a
# ac
# acb
# b
# ba
# bac
# b
# bc
# bca
# c
# cb
# cba
# c
# ca
# cab





def find_anagrams(word):
    if len(word) <= 1:
        print(word)
        return [word]
    anagrams = []
    for perm in find_anagrams(word[1:]):
        print(perm, word)
        for i in range(len(perm) + 1):
            print(perm, word)
            anagrams.append(perm[:i] + word[0] + perm[i:])
    return anagrams

# Example usage:
word = "big penis"
print(find_anagrams(word))

