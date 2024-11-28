'''
Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or punctuation: remove
everything starting from the beginning of house to the end of the sentence.
'''
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
'''
We can use list splicing to do this. We'll print all the elements of advice up to the starting index of the substring 'house'.
To find the starting index of house, we can use the find string method
'''
last_index = advice.find('house')
print(advice[:last_index])