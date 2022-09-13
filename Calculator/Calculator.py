from art import logo
from replit import clear

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2


calc = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def Calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))
    for i in calc:
        print(i,end="\n")

    cond = True
    while cond:
        sym = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        for i in calc:
            if sym == i:
                answer = calc[i](n1,n2)
        
        print(f"{n1} {sym} {n2} = {answer}")
        n1 = answer
        yes_no = input(f"Type 'y' to continue calculating with {answer}, or type 'n' for new calculations : ")

        if yes_no == 'n':
            cond = False
            clear()
            Calculator()

Calculator()