from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)  # Dictionary to store grouped anagrams

    for word in strs:
        sorted_word = "".join(sorted(word))  # Sort the characters of the word
        anagrams[sorted_word].append(word)  # Group words with the same sorted key

    return list(anagrams.values())  # Convert dictionary values to a list of lists

# Taking user input
strs = input("Enter words separated by spaces: ").split()
print(group_anagrams(strs))