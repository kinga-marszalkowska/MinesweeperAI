sentence = {(5, 0), (5, 1), (5, 2), (7, 2)}
other = {(5, 1), (5, 0)}

if sentence.issubset(other):
    new_set = other.difference(sentence)
    print(new_set)
elif sentence.issuperset(other):
    new_set = sentence.difference(other)
    print('super', new_set)
