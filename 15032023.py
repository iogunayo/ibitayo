# data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']
#
# # chars = []
# # for char in data:
# #     if char not in chars:
# #         chars.append(char)
# # print(chars)
#
# char_set = {}
# for char in set(data):
#     count = 0
#     for char1 in data:
#         if char == char1:
#             count += 1
#     char_set[char] = count
# print(char_set)
#
# char_comprehension = {element: len([char for char in data if element == char]) for element in set(data)}
# print (char_comprehension)


# 24032024

# data = [10, 20, 'a']
#
# sum_data = 0
# count_data = 0
# try:
#         for item in data:
#         sum_data += item
#         count_data += 1
#     average = sum_data / count_data
#     print(average)
# except ZeroDivisionError:
#     average = 0
#     print(average)
# except TypeError:
#     print('you cant add numeric to character')

# to skip non_numeric items, we handle TypeError by skipping the non_numeric item


r = range(10)
print(r)
print(list(r))
