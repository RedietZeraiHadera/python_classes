import datetime
class Student:
    school = 'AkiraChix'
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.age = age
        self.country = country
        self.last_name = last_name
            
    def greet_student(self):
        return f"Hello{self.first_name} from {self.country} welcome to {self.school}"
    def show_full_name(self):
        return f"My name is {self.first_name} {self.last_name}"
    def year_of_birth(self):
      current_year = datetime.datetime.now().year
      birth_year =  current_year-self.age
      return f"{self.first_name}, was born in {birth_year}"
    def show_initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}."
    
    