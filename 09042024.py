data = [1, 2, '3', 4, 5]
# print(data.pop())
# print(data)

sum_ = 0
count = 0


for number in data:
    try:
        sum_ += number
        count += 1
        result = sum_ / count
    except TypeError:
        pass
    except ZeroDivisionError:
        print(f'dividing by zero not allowed')
print(result)


enum1 = enumerate('abc')
print(list(enum1))
print(list(enum1))