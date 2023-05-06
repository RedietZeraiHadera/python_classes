class Car:
    country_manufature = "Germany"
    def __init__(self,make,model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_details(self):
        return f"This is a {self.year} {self.make} {self.model} from {self.country_manufature} "
    def start_car(self):
        return "vroom"
  
        
    