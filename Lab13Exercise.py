class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing exam.")


class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

student1 = Student("Ugyen Wangchuk", 20, "12001005036", "02230231", "Computor Programming", 1, 3.8)

# Access all Student attributes
print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"CID Number: {student1.cid_number}")
print(f"Student ID: {student1.student_id}")
print(f"Course: {student1.course}")
print(f"Year: {student1.year}")
print(f"GPA: {student1.gpa}")
#Calling all student methods
student1.walk()
student1.talk()
student1.eat()
student1.sleep()
student1.study()
student1.attend_class()
student1.write_exam()

teacher1 = Teacher("Sonam Yangchen", 27, "12121200000", "CSF", 50000, "Math Department", "Professor")
# Access all Teacher attributes
print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.age}")
print(f"CID Number: {teacher1.cid_number}")
print(f"Subject: {teacher1.subject}")
print(f"Salary: {teacher1.salary}")
print(f"Department: {teacher1.department}")
print(f"Designation: {teacher1.designation}")
#Calling all teacher methods
teacher1.walk()
teacher1.talk()
teacher1.eat()
teacher1.sleep()
teacher1.teach()
teacher1.grade_students()
teacher1.attend_meeting()
