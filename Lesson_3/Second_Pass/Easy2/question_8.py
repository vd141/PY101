'''
determine whether the following dictionary of people and their age contains
an entry for 'Spot'
'''
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
'''
we can use the dictionary get method
or we can use the in keyword
'''
print('Spot' in ages)
print(ages.get('Spot'))
print('Herman' in ages)
print(ages.get('Herman'))