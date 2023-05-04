from Person import Person

class Student(Person):

    __gr = "NoGroup"

    @staticmethod
    def pr():
        print(Student.__gr)

    def __init__(self,name,age):
        super().__init__(name,age)
        self.gr = ' '

    def print_per(self):

        print('Name: ',self.name, ' Age: ', self.age,' Group: ', self.gr)