
# def one():
#     return 1
#
#
# result = one()
# print(result)
#
#
# def say_hello():
#     print('hello!')

# def subtract(a, b):
#     return a - b
#
#
# test = subtract(10, 7)
# print(test)

def gen_matrix(m, n):
    return [
        [1 if col == row else 0 for col in range(n)] for row in range(m)
    ]


matrix_ = gen_matrix(4, 4)
print(matrix_)
