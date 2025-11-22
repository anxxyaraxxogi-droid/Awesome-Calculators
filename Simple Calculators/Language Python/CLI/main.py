def calc():
   #taking input for the operation the user wants to perfom
   op =  input("choose the operation: [+ , - , * , / , %]: ")

   #taking input for the numbers
   firstnum =  float(input("enter first number: "))
   secondnum = float(input("enter second number: "))

   #conditions for operation performing
   if op == "+":
      result = firstnum + secondnum
      print(f"The result of your operation is: {result}")
   
   elif op == "-":
      result = firstnum - secondnum
      print(f"The result of your operation is: {result}")

   elif op == "*":
      result = firstnum * secondnum
      print(f"The result of your operation is: {result}")

   elif op == "/":
         if secondnum == 0:
              print("undefined")
         else:
             result = firstnum / secondnum
             print(f"The result of your operation is: {result}")
   
   elif op == "%":
       if secondnum == 0:
          print("Undefined")
       else:
         result = firstnum % secondnum
         print(f"The result of your operation is: {result}")
    
   else:
      print("Invalid Value")
if __name__ == "__main__":
 calc()
print("Thankyou for using the awesome calculator!")
   
   
   
   

      
      
      