from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    print("s-calc")
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    print("e-calc")
    return sumGrades / credits

def is_sorted(lyst):
    print("s-sort")
    print(lyst)
    for i in range(0, len(lyst)  - 1):
        
        if lyst[i] > lyst[i + 1]:
            print("2e-sort")
            return False
    print("1e-sort")
    return True

def main():
    pass
    
  
if __name__ == "__main__":
    main()