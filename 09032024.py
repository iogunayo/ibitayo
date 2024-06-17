from math import sqrt
# new = "abcde"
# new2 = enumerate("abcde")
#
# print(list(new2))

# l = [(0, 0), (1, 1), (1, 2), (3, 5)]
# l1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# mag = [sqrt(x ** 2 + y ** 2) for x, y in l]
# print(mag)
#
# l2 = [x ** 2 for x in l1]
# print(l2)
#
#
# sq = []
# for x in l1:
#     sq.append(x ** 2)
# print(sq)

# even_int = [x ** 2 for x in l1 if x % 2 == 0]
# print(even_int)


# sales = {
#     'widget 1': 0,
#     'widget 2': 5,
#     'widget 3': 10,
#     'widget 4': 2
# }
#
# high_sales = [key for key, value in sales.items() if value >= 5]
# print(high_sales)



# identity_matrix = []
# for m in range(3):
#     row = []
#     for n in range(3):
#         if m == n:
#             row.append(1)
#         else:
#             row.append(0)
#     identity_matrix.append(row)
#
# print(identity_matrix)


# m = [
#     [1 if row == col else 0 for col in range(3)]
#     for row in range(3)
# ]
# print(m)
# m = []
# for row in range(3):
#     n = []
#     for col in range(3):
#         n.append(0)
#     m.append(n)
# print(m)

widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
sales = [10, 5, 15, 0]

sale_dict = {key: value for key, value in zip(widgets, sales) if value > 0}
print(sale_dict)