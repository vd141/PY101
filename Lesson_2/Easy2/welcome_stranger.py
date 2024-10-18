# Welcome Stranger

def greetings(name, status):
    name_string = ' '.join(name)
    title = status['title']
    occupation = status['occupation']
    return (f'Hello {name_string}! I\'m so excited to finally meet a {title}'
            f' {occupation}.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.