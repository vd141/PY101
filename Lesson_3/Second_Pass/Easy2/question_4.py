'''
Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number
at index 2, so that the list becomes [1, 2, 4, 5]
'''

a_list = [1, 2, 3, 4, 5]

'''
we can use the del function or we can use the list's pop method
'''

del(a_list[2]) # [1, 2, 4, 5]
#a_list.pop(2) # [1, 2, 4, 5]

print(a_list)