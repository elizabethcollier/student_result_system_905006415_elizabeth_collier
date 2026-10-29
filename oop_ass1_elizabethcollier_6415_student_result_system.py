class Student:
    school_name = "Limkokwing University"

    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

    # Instance method
    def calculate_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"

    # Instance method
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.calculate_grade())

    # Class method
    @classmethod
    def display_school(cls):
        print("School:", cls.school_name)


class ExamResultSystem:

    def __init__(self):
        self.students = []

    # Instance method
    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    # Instance method
    def display_all_results(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            print("\n--------------------")
            student.display_info()

    # Instance method
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                return

        print("Student not found.")

    # Class method
    @classmethod
    def display_system_name(cls):
        print("Student Digital Exam and Results Management System")


# Create the system object
system = ExamResultSystem()

# Display system information
ExamResultSystem.display_system_name()
Student.display_school()

# Create student objects
student1 = Student("ST001", "Elizabeth", 85)
student2 = Student("ST002", "John", 72)
student3 = Student("ST003", "Mary", 48)

# Add students to the system
system.add_student(student1)
system.add_student(student2)
system.add_student(student3)

# Display all examination results
print("\nALL STUDENT RESULTS")
system.display_all_results()

# Search for a student
print("\nSEARCH RESULT")
system.find_student("ST002")

# Display the total number of students
print("\nTotal students:", len(system.students))