class Student:
    
    def __init__(self, student_id, student_name, email, grade = None, courses = None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grade = grade if grade is not None else "N/A"
        self.courses = courses if courses is not None else []

    def __str__(self):
        return f("Student ID: {self.student_id}, Student Name: {self.student_name}, Email: {self.student_name}," \
                    "Grade: {self.grade}, Courses: {",".join(self.courses)}")

class StudentRecords:

    def __init__(self):
        self.student_list = []

    def add_student(self, student_id, student_name, email, grade = None, courses = None):
        new_student = Student(student_id, student_name, email, grade, courses)
        self.student_list.append(new_student)
        return "New Student Added Scuccessfully!"

    def update_student(self, student_id, student_name = None, email = None, grade = None, courses = None):
        for student in self.student_list:
            if student.student_id == student_id:
                if self.student_name is not None:
                    student.student_name = student_name
                if self.email is not None:
                    student.email = email
                if self.grade is not None:
                    student.grade = grade
                if self.courses is not None:
                    student.courses = courses
                return "Data Updated Successfully!"
            return "No ID Exists!"
    
    
    def delete_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                return "Student Removed!"
            return "No Student Found!"

    
    def enroll_course(self, student_id, course):
        pass

    def search_student(self, student_id):
        pass
        










