class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


s = Student("leelei",95)
print("ins's __dict__:")#实例的属性，只有两个
print(s.__dict__)
s.__dict__ = {}#清空属性
print(s.__dict__)
print("class's __dict__:")
print(Student.__dict__)#类的属性，有好多，包括方法