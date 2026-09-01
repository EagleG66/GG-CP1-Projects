# GLENN GUDMUNSON Average Grade

class1 = input("What percent do you have in your first period class? ")
class2 = input("What percent do you have in your second period class? ")
class3 = input("What percent do you have in your third period class? ")
class4 = input("What percent do you have in your advisory class? ")
class5 = input("What percent do you have in your sixth period class? ")
class6 = input("What percent do you have in your seventh period class? ")
class7 = input("What percent do you have in your eighth period class? ")

avg_grade = (class1+class2+class3+class4+class5+class6+class7)/7

print("Your average grade is",round(avg_grade,2))