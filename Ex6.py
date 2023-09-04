def student_data(student_id, **kwargs):
    print(f"ID: {student_id}")

    for i, j in kwargs.items():  # key-value
        print(f"{i}: {j}")


student_data(1, Name="Papa", Class="AAA")

obj_ = {"Name": "Papa", "Class": "AAA"}
student_data(2, **obj_)

obj_ = {"Name": "Papa"}
student_data(3, **obj_)
