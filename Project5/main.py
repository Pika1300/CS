from stack import Stack
f = open("Project5\data.txt", "r")

def eval_postfix(expr):
    if str(expr)!=expr:
       raise SyntaxError
    expr=expr.strip()
    expr=expr.replace(" ","")
    evals=Stack()
    nums=0
    op=0
    for x in expr: 
        if x.isdigit()==True:
            nums+=1
        else:
            op+=1
    if nums-1!=op:
        raise SyntaxError("Not Valid")  
    for x in expr: 
        if x.isdigit()==True:
            evals.push(x)

        else:

            i1=int(evals.pop())
            i2=int(evals.pop())
            if x=="+":
               evals.push(i2+i1)     
            elif x=="-":
               evals.push(i2-i1) 
            elif x=="/":
               evals.push(i2/i1)  
            elif x=="*":
               evals.push(i2*i1)  
    return float(str(evals))


def in2post(expr):
    if str(expr)!=expr:
       raise ValueError
    expr=expr.strip()
    expr=expr.replace(" ","")
    #print("expr: "+expr)
    operands=Stack()
    operators=Stack()
    prec = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "(": 3,
    ")": 3
    }
    l=0
    r=0
    for x in expr:
        if x=="(":
            l+=1
        if x==")":
            r+=1
    if l!=r:
        raise ValueError("Incorrect Value")
    for x in expr:
        """" 
        print("______")
        print("operands: ")
        print(operands)
        print("operators: ")
        print(operators)
        """
        #input("_________")
        #print("x:"+x)
       
        #digits pushed onto operands

        if x.isdigit()==True:
            operands.push(int(x))
        #operators
        else:
            precedance=prec[x]
            #print(str(x)+" "+str(precedance))
            #print(operators)

            #empty operator list
            if operators.siz==0:
                operators.push(x)
            
            #there are items in the operator list
            else:
                if operators.top()==")":
                    while operators.top()!="(":
                        top=operators.top()
                        if top=="(" or top==")":
                            operators.pop()
                        else:
                            operands.push(operators.pop())
                    
                #if the top is lesser precedence
                if prec[operators.top()]<precedance or operators.top()=="(":
                    operators.push(x)
                #greater precedence
                else:
                    #until it reaches a greater or higher precedence
                    while prec[operators.top()] >=precedance and operators.top()!="(":
                        top=operators.top()
                        if top=="(" or top==")":
                            operators.pop()
                        else:
                            operands.push(operators.pop())
                        
                        if (operators.siz)==0:
                            break
                    operators.push(x)

    while operators.siz!=0:
        top=operators.top()
        if top=="(" or top==")":
            operators.pop()
        else:
            operands.push(operators.pop())
    """""     
    print("operands:")
    print(operands)
    print()
    """
    return(str(operands))

    



def main():
    return 0
    
if __name__=="__main__":
    main()

contents=f.readlines()
print(in2post("(8+3)*(5-6))"))
  

f.close()
