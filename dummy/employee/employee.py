class Employee:
    def __init__(self, firstname, lastname, salary, known_as=None):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = f"{self.firstname}.{self.lastname}@klee.com"
        self.known_as = known_as

    def raised(self, salary):
        self.salary = salary
        
    def other_name(self):
        return  f"{self.firstname} {self.lastname} is also known as: {self.known_as}"

class Developer(Employee):
    def __init__(self, firstname, lastname, salary, programming_languages):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_languages
        
    def addLanguage(self, lang):
        self.prog_langs += [lang]
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None, known_as=None):
        super().__init__(first, last, pay, known_as)
        
        self.employees = [] if employees is None else employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print ('-->', emp)
            

kal = Employee('koua', 'lee', 800)
# print (kal.__dict__)

dev = Developer('john', 'doe', 1000, ['python'])
# dev.raised(1200)
# dev.addLanguage('java')
# print (dev.__dict__)

print (dev.other_name())


mgr = Manager('song', 'thao', 1000, employees=[dev], known_as='ntxhoo')
print (mgr.email)

print (mgr.other_name())
# print (mgr.aka)