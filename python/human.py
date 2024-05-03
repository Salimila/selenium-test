class human :
    name="salim"
    #built-in#constructor#initialize
    def __init__(self,name):
        self.name=name
        print("Bir human instance 'i üretildi")
    def __str__(self) -> str:
        return f"STR foknsiyonundan dönen değeri:{self.name}" 
    def talk(self,sentence,):
        print(f"{self.name}:{sentence}")
    def walk (self):
        print(f"{self.name}:is walking")
