from datetime import date
class person:
    
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
        
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return {age,self.country,self.name,self.date_of_birth}
    def get_profile(self):
        return {
            "name":self.name,
            "country":self.country,
            "date of birth":self.date_of_birth,
            "age":self.calculate_age()
            
            
        }
person = person("Subhan","Pakistan",date(2007,3,7))
print(person.get_profile())        
        