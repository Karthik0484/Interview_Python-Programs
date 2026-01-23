# Public access modifier

class Developer:

    def __init__(self):
        self.name = 'Karthik'

d1 = Developer()
print(d1.name)

# Protected access modifier

class College:

    def __init__(self):
        self._college = 'PMC tech'

class Graduate(College):

    def show(self):
        print(f"Graduated from {self._college}")

g1 = Graduate()
g1.show()

# Private access modifier
# Python does not enforce strict privacy. Instead, it renames any attribute starting
# with __ to _ClassName__attributeName to prevent accidental overwriting in subclasses [1, 3].
# This is a safety mechanism, not a security one.

class Grade:

    def __init__(self):
        self.__marks = 90

    def show(self):
        print("Grade A: ",self.__marks)

g1 = Grade()
g1.show()
print(g1._Grade__marks)
