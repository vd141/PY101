# The End is Not Here But Near

def penultimate(sentence):
    sentence = sentence.strip(' ')
    if ' ' in sentence:
        if sentence != ' ' * len(sentence):
            return sentence.split(' ')[-2]
        return ''
    else:
        return sentence

# New function: Return middle word
# first, strip whitespace, check for edge cases
# what remains is the sentence. if the sentence has an even number of words, 
# return the word at the index
# [0 1 2 3 4] length of 5 midpoint is 2.5 (rounded to 2 with floor division)
# [0 1 2 3] length of 4 midpoint is 2
# if length of sentence is 1 word, return that word

def middle(sentence):
    sentence = sentence.strip(' ')
    if ' ' in sentence:
        if sentence != ' ' * len(sentence):
            sentence_list = sentence.split(' ')
            num_words = len(sentence_list)
            return sentence_list[num_words//2]
        return ''
    else:
        return sentence


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(penultimate("") == "")
print(penultimate("      ") == "")

print(penultimate("last     ") == "last")
print(penultimate("last") == "last")

# a string is passed by value into a python function
a_word = '     wordy bird'
print(len(a_word))
print(penultimate("last     ") == "last")
print(penultimate(a_word))
print(a_word)
print(len(a_word))

print(middle('this is a sentence with odd number of words')) # prints with
print(middle('even number of words')) # prints of
print(middle('word')) # prints word
print(middle('   word   ')) # prints word
print(middle('')) # prints ''
print(middle('   ')) # prints ''