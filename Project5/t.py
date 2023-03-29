class test:
    def __init__(self):
        self.num=0
    def change(self, change):
        change+=1
    def p(self):
        num=self.num
        print(num)
        self.change(1)
        print(self.num)

t=test()
t.p()