
class Student: student_id = 1; student_name = "John"


Student.student_class = "AAA"
print(f"Add student_class ...")
for i,j in Student.__dict__.items():
    if not i.startswith('_'):
        print(f"{i} : {j}")

del Student.student_name
print(f"\nDelete student_name ...")
for i,j in Student.__dict__.items():
    if not i.startswith('_'):
        print(f"{i} : {j}")

