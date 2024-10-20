# The End is Not Here But Near

def penultimate(sentence):
    sentence = sentence.strip(' ')
    if ' ' in sentence:
        if sentence != ' '*len(sentence):
            return sentence.split(' ')[-2]
        return ''
    else:
        return sentence

# TODO: Edge cases where there is less than one word or no words
# return 
# check if there are spaces, else return an empty string
# if there are spaces, check if the string is only spaces. if it is, return an
# string
# if there is only one word, return that word



# New function: Return middle word


# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(penultimate("") == "")
print(penultimate("      ") == "")

print(penultimate("last     ") == "last")
print(penultimate("last") == "last")

a_word = '     wordy bird'
print(len(a_word))
print(penultimate("last     ") == "last")
print(penultimate(a_word))
print(a_word)
print(len(a_word))