# Task 1: University Course Catalog

from employee import Employee  # ✅ Importing the Employee class

# Base Class: Course
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        print(f"{self.course_code} - {self.course_name} ({self.credit_hours} credits)")

# CoreCourse subclass
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        super().display_info()
        print("Required for Major:", "Yes" if self.required_for_major else "No")

# ElectiveCourse subclass
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        super().display_info()
        print("Elective Type:", self.elective_type)

# Main program
if __name__ == "__main__":
    core_course = CoreCourse("CS101", "Intro to CS", 4, True)
    elective_course = ElectiveCourse("HUM202", "World History", 3, "liberal arts")

    print("Core Course Info:")
    core_course.display_info()

    print("\nElective Course Info:")
    elective_course.display_info()

    # ✅ Create and display Employee info
    emp = Employee("Alice", 60000)
    print("\nEmployee Info:")
    print("Name:", emp.get_name())
    print("Salary:", emp.get_salary())
