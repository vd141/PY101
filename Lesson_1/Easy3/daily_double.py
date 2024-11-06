# Daily double
# write a function that takes a string argument and returns a new string that 
# contains the value of the original string with all consecutive duplicate 
# characters collapsed into a single character

def crunch(string):
    # first option: loop through each character of string. save unique character
    # to a list. join characters of list at the end
    no_dupes = []
    prev_char = None

    for i in string:
        if i != prev_char:
            prev_char = i
            no_dupes.append(i)

    return ''.join(no_dupes)
        
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')