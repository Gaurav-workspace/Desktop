class student():
    def __init__(self,name,age,marks) -> None:
        self.name = name
        self.age = age
        self.marks = marks
    def __str__(self) -> str:
        return f"{self.name} : {self.age}"
s1 = student("Gaurav",20,90)
s2 = student("Vision",21,80)
s3 = student("Ultron",22,70)
array = [s1,s2,s3]
print(*array)
array.sort(key = lambda obj1: obj1.marks)
print(*array)