items = ['note', 'notebook', 'sketchbook']
print(type(items))
print(items)

items.append('paperbook')
items = ['book'] + items
print(items)

items[3] = 'booklet'
print(items)

del items[1]
print(items)