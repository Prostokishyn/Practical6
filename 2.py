class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Ім'я {self.name},  {self.age} років")
        
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position=position
    def work(self):
        print(f"{self.name}, {self.age}, {self.position}")
        
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id=student_id
    def study(self):
        print(f"{self.name}, {self.age}, {self.student_id}")
        
class University:
    def __init__(self):
         self.employes = []
         self.students = []
    def add_employee(self, employee):
         if isinstance(employee, Employee):
             self.employes.append(employee)
    def add_student(self, student):
         if isinstance(student, Student):
             self.students.append(student)
    def show_info(self):
         print("Викладачі")
         for employee in self.employes:
             employee.introduce()
             employee.work()
         print("\nСтуденти")
         for student in self.students:
             student.introduce()
             student.study()

university = University()
employee1 = Employee('Наташа', 37, "Викладач")
employee2 = Employee('Ольга', 21, "Викладач")
student1 = Student('Альоша', 19, 2)
student2 = Student('Ігор', 18, 9)
university.add_employee(employee1)
university.add_employee(employee2)
university.add_student(student2)
university.add_student(student1)
university.show_info()