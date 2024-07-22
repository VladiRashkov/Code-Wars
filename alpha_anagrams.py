from math import factorial

def list_position(word):
    def count_smaller_chars(ch, suffix):
        return sum(1 for x in suffix if x < ch)
    
    def factorial_division(n, char_counts):
        result = factorial(n)
        for count in char_counts.values():
            result //= factorial(count)
        return result

    sorted_word = ''.join(sorted(word))
    position = 1
    char_counts = {ch: word.count(ch) for ch in set(word)}

    for i, ch in enumerate(word):
        for smaller_char in sorted(set(word[i:])):
            if smaller_char < ch:
                char_counts[smaller_char] -= 1
                position += factorial_division(len(word) - i - 1, char_counts)
                char_counts[smaller_char] += 1
        
        char_counts[ch] -= 1

    return position

print(list_position('CABB'))  # Expected output: 10


# Alphabetic Anagrams
# Consider a "word" as any sequence of capital letters A-Z (not limited to just "dictionary words"). For any word with at least two different letters, there are other words composed of the same letters but in a different order (for instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters as these two).

# We can then assign a number to every word, based on where it falls in an alphabetically sorted list of all words made up of the same group of letters. One way to do this would be to generate the entire list of words and find the desired one, but this would be slow if the word is long.

# Given a word, return its number. Your function should be able to accept any word 25 letters or less in length (possibly with some letters repeated), and take no more than 500 milliseconds to run. To compare, when the solution code runs the 27 test cases in JS, it takes 101ms.

# For very large words, you'll run into number precision issues in JS (if the word's position is greater than 2^53). For the JS tests with large positions, there's some leeway (.000000001%). If you feel like you're getting it right for the smaller ranks, and only failing by rounding on the larger, submit a couple more times and see if it takes.

# Python, Java and Haskell have arbitrary integer precision, so you must be precise in those languages (unless someone corrects me).

# C# is using a long, which may not have the best precision, but the tests are locked so we can't change it.

# Sample words, with their rank:
# ABAB = 2
# AAAB = 1
# BAAA = 4
# QUESTION = 24572
# BOOKKEEPER = 10743