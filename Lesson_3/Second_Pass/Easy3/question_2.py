'''
What will the following code output?
'''
print([1,2,3] + [4,5])
'''
The operands of the addition (concatenation) operator are the same type. 
Therefore, the expression will return a new list that contains elements of both 
operands
'''
a_list = [1, 2, 3]
b_list = [4, 5]
c_list = a_list + b_list
print(id(a_list))
print(id(b_list))
print(id(c_list))