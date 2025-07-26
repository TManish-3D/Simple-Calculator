HISTORY_FILE="HISTORY.TXT"
def show_history():
  file=open(HISTORY_FILE,'r')
  lines=file.readlines()
  if len(lines)==0:
    print("No data is found")
  else:
    for line in reversed(lines):
      print(line.strip()+"\n")
  file.close() 
def clear():
  file=open(HISTORY_FILE,'w')
  file.close()
  print('History cleared') 
def save(num1,op,num2,result):
 file=open(HISTORY_FILE,'a')
 file.write(str(num1)+ op + str(num2) +'='+ str(result)+"\n")
 file.close() 
     
def calculation():
     num1=int(input("Enter a number :"))
     op=input('Enter the operator (+,-,*,/) :')
     num2=int(input("Enter a number :"))
     
     if op=='+':
        result=(num1+num2)
        print(result)
     elif op=='-':
        if num1>num2:
         result=(num1-num2)
         print(result)
        else:
           print('Invalid input') 
     elif op=='*':
       result=(num1*num2)
       print(result)   
     elif op=='/':
       if num2==0:
          print('Math error')
       else:
          result=(num1/num2)
          print(result)
     save(num1,op,num2,result)
   
def main():
 print("Calculator")
 while True:
  user=input("What will you do\na.Calculation\nb.History\nc.Clear history\nd.Exit\n")
  if user=="d":
   print('Thank you for using it')
   break
  elif user=='c':
   clear()
  elif user=='b':
   show_history()
  elif user=='a':
    calculation()
  else:
    print('Invalid input')
main()
    


   

   
