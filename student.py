class Student:
    id_name = ()
    grades = {}
    email = ()
    courses = {}

    def __init__(self, student_id, student_name, email, grades = None, courses = None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades
        self.courses = courses

    def __str__(self):
        return f"Student ID: {self.student_id}, Student Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    
class StudentRecords:
    student_list = []

    def __init__(self):
        pass

    @classmethod
    
    def add_student(cls, student_id, email = None, grades = None, courses = None):
        cls.student_list += 1
        new_student = StudentRecords(cls, student_list, student_id)
        










