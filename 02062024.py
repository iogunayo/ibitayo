class Vector:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __add__(self, other):
        return self.m + other.m, self.n + other.n

    def __eq__(self, other):
        if self.m == other.m and self.n == other.m:
            return True
        return False


v1 = Vector(2, 2)
v2 = Vector(2, 2)
v3 = Vector(4, 5)

# print(f'Sum v1 + v2 is', v1 + v2)
print(f'compare v1 and v2 is', v1 == v2)
