'''
What do you think the following code will output?
'''
nan_value = float("nan")

print(nan_value == float("nan"))
'''
the code will output False, as Nan object are designed to be unique

To reliably test if the value is nan, import the math module to use the isnan method
'''