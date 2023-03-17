class Person:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        
    @property
    def name_(self):
        return self.name
    
    @name_.setter
    def name_(self, input_):
        if len(input_) < 3:
            print("Imię jest za krótkie! Musi mieć minimum 3 znaki!")
        else:
            self.name = input_
    
    @property        
    def surname_(self):
        return self.surname
    
    @surname_.setter
    def surname_(self, input_):
        if len(input_) < 3:
            print("Nazwisko jest za krótkie! Musi mieć minimum 3 znaki!")
        else:
            self.surname = input_
            
    @property
    def age_(self):
        return self.age
    
    @age_.setter
    def age_(self, input_):
        try:
            input_ = int(input_)
        except ValueError:
            print("Proszę wprowadzić liczbę całkowitą!")
            return
        
        if 0 <= input_ <= 130:
            self.age = input_
        else:
            print("Proszę wprowadzić liczbę z przedziału 0-130!")
            
    def __str__(self):
        return f"Nazywam się {self.name} {self.surname} i mam {self.age} lat."
        

class Student(Person):
    def __init__(self):
        super().__init__()
        self.field_of_study = None
        self.student_book = {}

    def change_field(self) -> None:
        self.field_of_study = input("Wprowadź nowy kierunek studiów\n> ")
        
    def add_modify_class(self) -> None:
        class_name = input("Wprowadź nazwę przedmiotu\n> ")
        self.student_book[class_name] = input("Wprowadź ocenę z przedmiotu\n> ")
        
    def __str__(self) -> str:
        output = ""
        for sub in self.student_book:
            output += f"{sub}: {self.student_book[sub]}\n"
        return f"{super().__str__()} Jestem studentem {self.field_of_study}. Moje oceny to:\n {output}"
    
    
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.job_title = None
        self.skills = {}
        
    def change_job(self) -> None:
        self.job_title = input("Wprowadź zawód\n> ")
        
    def add_modify_skill(self) -> None:
        skill_name = input("Wprowadź umiejętność\n> ")
        self.skills[skill_name] = input("Wprowadź stopień biegłości\n> ")
        
    def __str__(self):
        output = ""
        for skill in self.skills:
            output += f"{skill}: {self.skills[skill]}\n"
        return f"{super().__str__()} Jestem {self.job_title}. Moje umiejętności to:\n {output}"
        
        
    
if __name__ == "__main__":
    people = [Student(), Employee()]
    
    for person in people:
        while person.name is None:
            person.name_ = input("Wprowadź imię (min. 3 znaki)\n> ")
        while person.surname is None:
            person.surname_ = input("Wprowadź nazwisko (min. 3 znaki)\n> ")
        while person.age is None:
            person.age_ = input("Wprowadź wiek (0-130)\n> ")
    
    running_ = True
    while running_:
        
        for idx, person in enumerate(people):
            print(f"{idx + 1}. {person}")
        try:
            choice = int(input("Którą osobę chcesz edytować? Wpisz odpowiedni numer. Wpisz -1 aby zamknąć program\n> "))
        except ValueError:
            print("Podaj liczbę całkowitą!")
            
        if choice == -1:
            running_ = False
            exit()
            
        try:
            cmd = input("Co chcesz zrobić z wybraną osobą?\n1. Zmień zawód/kierunek studiów\n2. Dodaj/modyfikuj umiejętności/oceny\n> ")
            if cmd == "1":
                if isinstance(people[choice - 1], Student):
                    people[choice - 1].change_field()
                else:
                    people[choice - 1].change_job()
            elif cmd == "2":
                if isinstance(people[choice - 1], Student):
                    people[choice - 1].add_modify_class()
                else:
                    people[choice - 1].add_modify_skill()
        except IndexError:
            pass