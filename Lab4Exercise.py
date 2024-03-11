students_lists = []
students_dict = {}

print("Student Information")
name = input("Enter the name: ")
age = input("Age: ")
grade = input("Enter grade: ")
students_lists.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Student found!")
print(students_dict)
print("Search for student")
search_name =input("Enter the name of student: ")
if search_name in students_lists: 
    print(f"Information Displayed. Name: {students_dict[search_name]}")
else: 
    print("Incorrect input!!!")

remove_name = input("Enter the name of the student to be removed: ")
print("Along with name the student's information will be also removed!")
if remove_name in students_lists:
    remove_student = students_dict[remove_name]
    students_lists.remove(remove_name)
    del students_dict[name]
    print("Name removed succesfully")
else:
    print("Name not found. Try again!")