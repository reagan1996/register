student = "test student1"
name1 = student.split(" ")
print(name1)
print(name1[1:])

last_name = ""
for names in name1[1:]:
    last_name = last_name + " " + names
other_names = last_name.rstrip(" ")
print(other_names)