subjects = ["C", "C++", "Java","Python","BASIC"]

print(subjects)
print(subjects[0])
print(subjects[2:])
print((subjects[-1]))

print("Python" in subjects)
print("swift" not in subjects)

print(subjects + ["Swifts",27])

print(subjects * 3)

subjects.append("TOC")
print(subjects)
subjects.insert(2,"OS")
print(subjects)
subjects.remove("OS")
print(subjects)
subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

