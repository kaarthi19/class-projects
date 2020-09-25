
def Welcome():
  print("Welcome to your personal Integer Calculator.")
  print("")
  
def AskNum_1():
  while True:                                       #Using a while loop to validate the integer only input
    try:
      num_1 = int(input('Enter your first number: '))                       #Message promtping to insert the first number
      break
    except ValueError:
      print("Error! Please enter a whole number.")                          #Error message for non integer input
      
  while num_1 <= limit_1:                                                   #Using a while loop to check the limit and the number
    global a
    a = num_1  
    print("The first number is {}.". format(num_1))                        #Displaying the first number set
    break
  else:
    print("Your value exceeds the limit set. Please enter a new value.")    #Error message for exceeding the limit set
    AskNum_1()

def AskNum_2():
  while True:                                       #Using a while loop to validate the integer only input
    try:
      num_2 = int(input('Enter your second number: '))                      #Message promtping to insert the first number
      break
    except ValueError:
      print("Error! Please enter a whole number.")                          #Error message for non integer input
    
  
  while num_2 <= limit_2:                                                   #Using a while loop to check the limit and the number
    global b
    b = num_2
    print("The second number is {}.". format(num_2))                       #Displaying the second number set
    break
  else:
    print("Your value exceeds the limit set. Please enter a new value.")    #Error message for exceeding the limit set
    AskNum_2()
        
def FindNum_1():                  #Setting a funtion with a set of function (for PART 1)to enter the first number for the calculation
  global limit_1
  while True:                                       #Using a while loop to validate the integer only input
    try:
      limit_1 = int(input("Enter the limit for the first number: "))            #Message promtping to insert the first limit
      print ("The limit for the first number is {}.". format(limit_1))           #Displaying the first limit set
      break
    except ValueError:
      print("Error! Please enter a whole number.")                              #Error message for non integer input
  AskNum_1()
  print("")
  
def FindNum_2():                  #Same funtion concept used for PART 1 (For PART 2)
  global limit_2
  while True:                                       #Using a while loop to validate the integer only input
    try:
      limit_2 = int(input("Enter the limit for the second number: "))           #Message promtping to insert the second limit
      print ("The limit for the second number is {}.". format(limit_2))          #Displaying the second limit set
      break
    except ValueError:
      print("Error! Please enter a whole number.")                              #Error message for non integer input
  AskNum_2()
  print("")

def Calculate():
  print ("The first number is {} and the second number is {}.". format(a, b))        #Recalling the numbers entered
  print ("The sum of the numbers are")                                              #Doing the summation of the two numbers and printing the result
  print (a + b)
  print("")

def Thanks():
  print("Thank you and Goodbye.")
  print("")

                                #Main Function
Welcome()
FindNum_1()                                                                 #PART 1 - Operation is done using the FindNum1 function to set the first number
FindNum_2()                                                                 #PART 2 - Using FindNum2 function with the same concept as PART 1 to set the second number
Calculate()                                                                 #PART 3 - Summation of the two numbers set 
Thanks()

