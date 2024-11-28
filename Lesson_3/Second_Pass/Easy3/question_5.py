'''
the following function unecessarily uses two return statements to return boolean
values. can you rewrite this function so that it only has one return statement and 
does not explicitly use either True or False?
'''
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
'''
we can move the blue and green strings into a list and check to see if color is in
that list. we would return the value of that expression
'''
def color_is_valid(color):
    return color in ['blue', 'green']
