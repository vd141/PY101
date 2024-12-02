'''
Alyssa was asked to write an implementation of a rolling buffer. You can add and
remove elements from a rolling buffer. However, once the buffer becomes full,
any new elements will displace the oldest elements in the buffer.

What is the key difference between these two implementations?
'''
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
'''
The usage of the append and pop methods suggests that the buffer is made from a list,
which is mutable. the first implementation of the buffer mutates the original list,
since the method is being called from the parameter itself.

in the second function, buffer is a local variable that shadows the argument. 
any additions or removals of elements from the buffer affect the local buffer,
not the argument.
'''