class studentData: # create a class
    name1 = "subhan" #class attribute
    age = 12 
    
    def __init__(self,name,age): # constructor or instance
        self.name = name #instance attribute
        self.age = age #instance attribute
    
    

class chargingChecker:
    def connect_device(self,battery):
        if battery == 0:
            print("Your device is powered off ❌")
        elif battery < 30 and battery >= 1:
            print(f"Please connect your charger 🔌 ({battery}%)")
        elif battery >=30 and battery <=50:
          print(f"Battery health is good 🙂 ({battery}%)")
        elif battery >=51 and  chaging <= 100:
            print(f"Battery health is excellent 🔋 ({battery}%)")
        else:
             print("Invalid battery percentage ⚠️")
    
student = studentData("ayan",14) # create an object 
print(student.name1, student.age)

# student.connect_device(-1)

checker = chargingChecker()
checker.connect_device(0)