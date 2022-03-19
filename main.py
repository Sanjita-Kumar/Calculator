def add(x, y):
    return round(x + y,2)

def subtract(x, y):
    return round(x - y,2)
    
def multiply(x, y):
    return round(x * y,2)
    
def divide(x, y):
    return round(x / y,2)
    
def exponent(x, y):
  return round(x ** y,2)
  
def squareroot(x):
  return round(x**(0.5),2)
  
def cuberoot(x):
  return round(x**(1/3),2)
  
  
  
    
print(" PLEASE SELECT THE OPERATION")

print()
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exponent")
print("6.squareroot")
print("7. cuberoot")

print()
print ("ENTER THE OPERATION YOU WISH TO DO= 1/2/3/4/5/6/7:  ")

choice =input()

if choice in ('1', '2', '3', '4' ):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print()

if choice == '1':
  print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
  print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
  print(num1, "/", num2, "=", divide(num1, num2))
  
if choice in ('5'):
  num1a = float(input("Enter the base:  "))
  num1b = float(input("Enter the power:  "))
  
if choice == '5':
  print(num1a,"**",num1b,"=", exponent(num1a,num1b))
            
if choice in ('6','7'):
  num3 = float(input("what is the number: "))
  print()
  
if choice == '6':
  print(num3,"squareroot= ", squareroot(num3))
  
elif choice == '7':
  print(num3,"cube root= ",cuberoot(num3))

  
  

