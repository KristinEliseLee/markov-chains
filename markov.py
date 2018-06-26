"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file:
        whole_text = file.read()
    return whole_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    all_words_list = text_string.split()

    chains = {}

    for index in range(len(all_words_list)-2):
        word1 = all_words_list[index]
        word2 = all_words_list[index + 1]
        new_value = all_words_list[index + 2]
        chains.setdefault((word1, word2), []).append(new_value)
        # chains[(word1, word2)] += [new_value]

    return chains


def make_text(chains):
    """Return text from chains."""
    # Get the link randomly from imported dict (key) and add to the list 'words'
    # Choose random word from the list of that keys values, append new word to list
    # New key becomes second word from list and third word from list
    # repeat finding value, then new key (tuple of index -2 and -1)
    # keep going whil the tuple can be found in the dict, if not, stop


    words = []

    words.extend(choice(list(chains.keys())))

    link = (words[-2], words[-1])
    while link in chains and len(words) < 1000:
        words.append(choice(chains[link]))
        link = (words[-2], words[-1])

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
