data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

# for list_ in data:
#     new_data = ' '
#     for item in list_:
#         new_data = new_data + str(item) + ',' + ' '
#     print(new_data)


# for list_ in data:
#     new_data = ''
#     str_list = str(list_)
#     new_data = new_data.join(str_list + ',' + ' ')
#     print(new_data)


for inner_list in data:

#    for elements in inner_list:
    output = ','.join(str(element) for element in inner_list)
    print(output)