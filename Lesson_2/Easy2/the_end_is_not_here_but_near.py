# The End is Not Here But Near

def penultimate(sentence):
    return sentence.split(' ')[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")