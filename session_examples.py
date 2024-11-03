#1
text = 'Hello, there!'

def concat(s1, s2):
    s1 + s2
    return s1

print(concat(text, '!!'))
print(text)

text = 'Hello, there!'

#2
def concat(s1, s2):
    s1 += s2
    return s1

print(concat(text, '!!'))
print(text)

#3
def add_player(name, info):
    players[name] = info

players = {
    "Bob": {"age": 32},
    "Alicia": {"age": 28},
    "Marcus": {"age": 25},
    "Phoebe": {"age": 27},
}

add_player("Jacob", {"age": 18})
print(players)

#4
def add_player(collection, name, info):
    collection[name] = info

players = {
    "Bob": {"age": 32},
    "Alicia": {"age": 28},
    "Marcus": {"age": 25},
    "Phoebe": {"age": 27},
}

add_player(players, "Jacob", {"age": 18})
print(players)