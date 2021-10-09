items = ['note', 'notebook', 'sketchbook']
print(type(items))
print(items)

items.append('paperbook')
items = ['book'] + items
print(items)

items[3] = 'booklet'
print(items)

items[4] = 'booktrade'
del items[1]
print(items)

items[4] = 'booktrade'