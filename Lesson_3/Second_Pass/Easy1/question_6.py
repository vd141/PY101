'''
Determine whether the name 'Dino' appears in the strings below -- check each string separately:
'''
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
'''
We can use the in keyword to check of the existence of something in a collection. the expression will return a boolean
'''

find_me = 'Dino'

print(find_me in str1)
print(find_me in str2)