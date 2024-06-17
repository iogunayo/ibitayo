# m = [[0] * 3] * 3
# print(m)
#
# m2 = [[0] * 3 for row in range(3)]
# print(m2)
#
# print(m2[0][0] is m2[0][1])
# print(m[0][0] is m[0][1])


widget_sales = [
    {'name': 'widget1', 'sales': 10},
    {'name': 'widget2', 'sales': 5},
    {'name': 'widget3', 'sales': 15}
]
# high_sales = {widget_sales[i]['name']: widget_sales[i]['sales'] for i in range(len(widget_sales)) if widget_sales[i]['sales'] > 5}
# print(high_sales)

# high_sales = {}
# for i in range(len(widget_sales)):
#     if widget_sales[i]['sales'] > 5:
#         high_sales[widget_sales[i]['name']] = widget_sales[i]['sales']
# print(high_sales)

data = ['a', 'a', 'b', 'b', 'b', 'c']

# frequency = {}
# for i in data:
#     if i not in frequency:
#         count = 1
#     else:
#         count += 1
#     frequency[i] = count
# print(frequency)

comp_frequency = {data[i]: count for i in data len(set(j))}