# Combines all three concepts:
#   1) class + instance methods
#   2) class attributes
#   3) inheritance + super()
# Example: Person -> Student 

class Person:
    species = "Human"                 # class attribute
    people_created = 0                # class-level counter

    def __init__(self, name, age):
        self.name = name              # instance attributes
        self.age = age
        Person.people_created += 1

    def show_info(self):
        print(f"My name is {self.name} and I am {self.age} years old "
              f"({Person.species})")


class Student(Person):
    university = "UOL"         # another class attribute, shared by students
    students_created = 0

    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)   # reuse Person's constructor
        self.roll_no = roll_no
        self.course = course
        Student.students_created += 1

    # override the parent method, then extend it with super()
    def show_info(self):
        super().show_info()
        print(f"I study {self.course} at {Student.university}, "
              f"my roll number is {self.roll_no}")

    # instance method specific to students
    def study(self, subject):
        print(f"{self.name} is studying {subject} right now.")


if __name__ == '__main__':
    # objects of the child class
    me = Student("Muhammad Saad Khan", 21, "70153904", "Advanced Backend")
    friend = Student("Ali Hassan", 22, "70154663", "Advanced Frontend")

    # object of the parent class still works
    teacher = Person("Tahir Ilyas", 35)

    print("--- Parent class object ---")
    teacher.show_info()

    print("\n--- Student 1 ---")
    me.show_info()
    me.study("Python OOP")

    print("\n--- Student 2 ---")
    friend.show_info()

    # class attributes are shared across every object
    print("\n--- Shared class attributes ---")
    print(f"Both at same university? "
          f"{me.university == friend.university}")
    print(f"People created (class counter) : {Person.people_created}")
    print(f"Students created (class counter): {Student.students_created}")

    # inheritance check
    print(f"\nIs 'me' a Person?      {isinstance(me, Person)}")
    print(f"Is 'me' a Student?     {isinstance(me, Student)}")
    print(f"Is 'teacher' a Student? {isinstance(teacher, Student)}")
