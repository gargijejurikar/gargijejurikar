# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(text):
    count_vowels = 0
    count_consonants = 0
    for character in text:
        if (character in "aeiouAEIOU"):
            count_vowels +=1
        else:
            count_consonants +=1
    return(count_vowels, count_consonants)
print(counting_vowels_and_consonants("hello world"))

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    import re
    sentences = [s.strip() for s in re.split(r'[.!?]', paragraph) if s.strip()]
    total_vowels = 0
    total_consonants = 0
    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants
    number_of_sentences = len(sentences)
    average_vowels = total_vowels / number_of_sentences
    average_consonants = total_consonants / number_of_sentences
    return(number_of_sentences, average_vowels, average_consonants)


# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
result1, result2, result3 = average_vowels_and_consonants(paragraph)
print(f"The number of sentences is {result1}, the average vowels per sentence is {result2}, and the average consonants per sentence is {result3}.")