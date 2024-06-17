widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0}
]

# widget_dict = {}
# for i in range(len(widget_sales)):
#     nam = widget_sales[i]['name']
#     sale = widget_sales[i]['sales']
#     widget_dict[nam] = sale
#
# print(widget_dict)
#
# widget_compre = {widget_sales[i]['name']: widget_sales[i]['sales'] for i in range(len(widget_sales))}
# print(widget_compre)
#
# print(widget_sales[0]['sales'])

new_dict = {}
for dic in widget_sales:
    nom = dic['name']
    sal = dic['sales']
    new_dict[nom] = sal

print(new_dict)