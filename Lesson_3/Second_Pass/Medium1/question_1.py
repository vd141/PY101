'''
write a program that outputs The Flintstones Rock! 10 times, with each line 
prefixed by one more hyphen than the line above it. The output should start out 
like this:

-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
'''
repeat_me = 'The Flintstones Rock!'

'''
we can multiply the string '-' by the iteration of the for loop. this will be 
appended to the string

the for loop will be made with a range sequence
'''

for idx in range(1,11):
    print(f'{'-' * idx}{repeat_me}')