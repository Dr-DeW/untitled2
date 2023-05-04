class p:
    def __init__(self):
        self.__age = 1

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        if 1 <= a < 120:
            self.__age = a

private int age;
public int Age
{
    get
{
    return age
}
set
{
if 1 <= value < 120:
    age = value
}

}