class Vector:

    def __init__(self, input_list):
        self.elements = input_list
        self.len = len(input_list)

    def __str__(self):
        return '(' + ','.join([str(a) for a in self.elements]) +')'

    def add(self, vec):
        return Vector([a + b for (a, b) in zip(self.elements, vec.elements)]) if self.len == vec.len else ValueError("Dimension mismatch")

    def subtract(self, vec):
        return Vector([a - b for (a, b) in zip(self.elements, vec.elements)]) if self.len == vec.len else ValueError("Dimension mismatch")

    def dot(self, vec):
        return sum([a*b for (a, b) in zip(self.elements, vec.elements)]) if self.len == vec.len else ValueError("Dimension mismatch")

    def equals(self, vec):
        return all([a == b for (a, b) in zip(self.elements, vec.elements)]) if self.len == vec.len else False

    def norm(self):
        return sum([a**2 for a in self.elements])**(1/2)

def main():

    a = Vector([1, 4])
    b = Vector([1, 4])
    print(a.equals(b))
    return 0

if __name__ == "__main__":
    main()
