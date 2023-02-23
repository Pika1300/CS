''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number=0000,name="",credit_hr=0.0,grade=0.0):
      print("s-course")
      if isinstance(number,int) and number>=0:
        self.numberr=number
      else:
        raise ValueError("Incorrect Number")
      if isinstance(name,str):
        self.namee=name
      else:
        raise ValueError("Incorrect Name")
      if isinstance(credit_hr,float) and credit_hr>=0:
        self.credit_hrr=credit_hr
      else:
        raise ValueError("Incorrect credit_hr")
      if isinstance(grade,float) and grade>=0.0 and grade<=4.0:
        self.gradee=grade
      else:
        raise ValueError("Incorrect grade")
      print("e-course")
      
    def number(self):
      print("a")
      return self.numberr
    def name(self):
      print("b")
      return self.namee
    def credit_hr(self):
      print("c")
      return self.credit_hrr
    def grade(self):
      print("d")
      return self.gradee

  
    def __eq__(self, other):
      print(1)
      if isinstance(other,Course):
        if self.numberr==other.numberr:
          return(True)
        else:
          return False
    def __ne__(self, other):
      print(2)
      if isinstance(other,Course):
        if self.numberr!=other.numberr:
         return(True)
        else:
          return False
    def __lt__(self, other):
      print(3)
      if isinstance(other,Course):
        if self.numberr<other.numberr:
          return(True)
        else:
          return False
    def __gt__(self, other):
      print(4)
      if isinstance(other,Course):
        if self.numberr>other.numberr:
          return(True)
        else:
          return False
    def __le__(self, other):
      print(5)
      if isinstance(other,Course):
        if self.numberr<=other.numberr:
          return(True)
        else:
          return False
    def __ge__(self, other):
      print(6)
      if isinstance(other,Course):
        if self.numberr>=other.numberr:
          return(True)
        else:
          return False
    def __str__(self):
      print("e")
      return (f"{self.name()} Grade:{self.grade()} Credit Hourse:{self.credit_hr()}")