class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
class Gradebook:
    def __init__(self):
        self.students = []  

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if not self.students:  
            return 0

        total = 0
        for student in self.students:
            total += student.score

        return total / len(self.students)


gb = Gradebook()

gb.add_student(Student("Fetty", 70))
gb.add_student(Student("Dorlie", 60))
gb.add_student(Student("Rebby", 50))
gb.add_student(Student("Letty", 85))

print("Class Average:", gb.get_average())