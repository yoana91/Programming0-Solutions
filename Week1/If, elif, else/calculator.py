a = input ("a")
b = input ("b")
a = int (a)
b = int (b)
oper = input ("oper")
if oper== "+":
    result= a+b
elif oper== "-":
     result= a-b
elif oper=="*":
     result=a*b
elif oper=="/":
      result= a/b
if result != False:
    print("Result is:")
    print(result)
else:
    print("We do not support that operation.")
