'''
One day, Spot was playing with the Munster family's home computer, and he wrote
a small program to mess with their dmeographic data:
'''
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"
'''
After writing the function, he typed the following code:
'''
mess_with_demographics(munsters)

'''
What happened to the family's data?

the dictionary is passed by object reference into the function. 

an augmented assignment addition is being performed on the value of 'age' in index'ed
dictionary value. the gender of each value is set to the value of "other"

the dictionary that was passed in is mutable, so these operations affect the values
in the dict

this mutates the inner dict for each key value pair of the outer dictionary

Spot has modified the family's data
'''

