l1 = ['a', 'b', 'c', 'd']
l2 = [97, 98, 99, 100]
comp = [(l1[x], l2[x]) for x in range(len(l2))]
print(comp)


data = {
    ('item1', 10, 100.0),
    ('item2', 5, 25.0),
    ('item3', 100, 0.5)
}
dict_ = {}
for items in data:
    dict2 = {}
    dict2['num_sold'] = items[1]
    dict2['unit_price'] = items[2]
    for i in range(3):
        dict_['item']i = dict2
    print(dict_)
