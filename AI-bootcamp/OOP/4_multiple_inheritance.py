# multiple-inheritance

# Ana sınıflar
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} çalışıyor ve maaşı {self.salary} TL."

class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university

    def study(self):
        return f"{self.name}, {self.university} üniversitesinde okuyor."

# Çoklu Kalıtım: Stajyer hem Employee hem Student özelliklerini miras alıyor.
class Intern(Employee, Student):
    def __init__(self, name, salary, university, internship_duration):
        Employee.__init__(self, name, salary)  # Employee sınıfının __init__ metodunu çağır
        Student.__init__(self, name, university)  # Student sınıfının __init__ metodunu çağır
        self.internship_duration = internship_duration  # Staj süresi

    def info(self):
        return f"{self.name}, {self.university} öğrencisi ve {self.salary} TL maaşla {self.internship_duration} aylık staj yapıyor."

# Nesne oluşturma
intern1 = Intern("Ahmet", 5000, "İTÜ", 6)

# Metotları kullanma
print(intern1.work())   # Employee sınıfından
print(intern1.study())  # Student sınıfından
print(intern1.info())   # Intern sınıfından
