class Student: pass


class Marks: pass


student_ = Student()
mark_ = Marks()

print(f"Is student_ in Student() : {isinstance(student_, Student)}")
print(f"Is mark_ in Marks() : {isinstance(mark_, Marks)}")
print(f"Is student_ in Marks() : {isinstance(student_, Marks)}")
print(f"Is mark_ in Student() : {isinstance(mark_, Student)}")

print(f"Is student_ an object : {issubclass(Student, object)}")
print(f"Is mark_ an object : {issubclass(Marks, object)}")
