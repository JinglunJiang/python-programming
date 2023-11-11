from pathlib import Path
import string

def fill_completions(fd):
    """
    Takes an opened file as input, and returns a dictionary.

    The function loops through each word in a file and builds a dictionary:

    - The keys of the dictionary are tuples of the form `(n, letter)` where `n` is an integer and `letter` is a lowercase letter `a-z`.
    - The value associated with key `(n, letter)` is the set of words that contain `letter` at position `n`.  
    All words should be converted to lower case for simplicity. 
    If the file contained the word `Python`, then `d[0, "p"]`, `d[1, "y"]`, `d[2, "t"]`, `d[4, "h"]`, `d[5, "o"]`, and `d[6, "n"]` would all contain the word `python`.
    - Words must be stripped of leading & trailing punctuation.
    - Words containing non-alphabetic characters are ignored, as are words of length 1.
    """
    completions = {}
    for line in fd.readlines():
        line = line.lower()
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            if word.isalpha() and len(word) > 1:
                for index, char in enumerate(word):
                    completions[(index, char)] = completions.get((index, char), set())
                    completions[(index, char)].add(word)
    return completions

def find_completions(prefix, comp_dict):
    """
    Takes a prefix string and `comp_dict` (the result of `fill_completions`) as input. 
    It returns a the set of strings that complete the prefix. If no words match, it returns an empty set.
    """
    output = set().union(*comp_dict.values())
    for index, char in enumerate(prefix):
        output = comp_dict.get((index, char), set()) & output
    return output

def main():
    """
    1. Open a file named `"articles.txt"`.  This file contains the text of recent news articles.
    2. Calls `fill_completions` to fill out a completion dictionary.
    3. Repeatedly prompts the user for a prefix to complete.
    4. Prints out each word that can complete the given prefix (one per line). If no completions are possible it should print `"No completions."`.
    5. Quit if the user enters the word `quit`.
    """
    path = Path(__file__).parent/"articles.txt"
    fd = path.open()
    dictionary = fill_completions(fd)
    while True:
        prefix = input("Enter prefix: ").lower()
        if prefix == "quit":
            break
        completions = find_completions(prefix, dictionary)
        if completions:
            for word in completions:
                print(f"{word}")
        else:
            print("No Completions")

if __name__ == "__main__":
    main()