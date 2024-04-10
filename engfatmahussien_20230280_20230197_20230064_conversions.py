#from decimal to binary
def dec_to_bin (number1):#number1 is the number
    number1=int(number1)
    list_binary=''
    while number1!=0:
        remin=number1%2
        list_binary=str(remin)+list_binary
        number1=int(number1/2)  
    return list_binary#string value is returned

#from decimal to hexadecimal
def dec_to_hexa(number1):
    number1=int(number1)
    list_hexa=''
    while number1!=0:
        remin=number1%16
        if remin==10:remin='A'
        elif remin==11:remin='B'    
        elif remin==12:remin='C'    
        elif remin==13:remin='D'
        elif remin==14:remin='E'
        elif remin==15:remin='F'
        list_hexa=str(remin)+list_hexa
        number1=int(number1/16)
    return list_hexa#string value is returned

##from binary to decimal
def bin_to_dec(number1):
    number1=int(number1)
    sum=0
    i=0
    while number1!=0:
        remin=number1%10
        dec_digit=remin*(2**i)
        sum=sum+dec_digit
        number1=int(number1/10)
        i+=1
        
    return sum#int value is returned

##from decimal to octal
def dec_to_octal (number1):
    number1=int(number1)
    list_oct=''
    while number1!=0:
        remin=number1%8
        list_oct=str(remin)+list_oct
        number1=int(number1/8)
    return list_oct#string value returned

#from hexadecimal to decimal
def hexa_to_dec (x):#x is the input number
         
 x=list(x)
 y = len(x)
 sum=0
 for i in range(y): 
  if    x[i] == 'A':
   x[i] = 10 
  elif  x[i] == 'B':
   x[i] = 11
  elif  x[i] == 'C':
   x[i]= 12
  elif  x[i] == 'D':
   x[i]=13
  elif  x[i] == 'E':
   x[i]=14
  elif  x[i] == 'F':
   x[i]=15
 x=[int(i) for i in x]
 x=x[::-1]
 for i in range(y):
  dec=x[i]*(16**i)
  sum+= dec 
 return sum#return int value

#from octal to decimal
def octal_to_decimal(octal_num):
    octal_num = octal_num[::-1]
    decimal_num = 0
    for i in range(len(octal_num)):
        bit = int(octal_num[i])
        decimal_num+= (bit * (8 ** i))
    return decimal_num

#from octal to hexa
def octal_to_hexa(number1):
    result=octal_to_decimal(number1)
    oct_to_hexa=dec_to_hexa(result)
    return oct_to_hexa

#from hexa to octal
def hexa_to_oct(number1):
    res=hexa_to_dec(number1)
    octal=dec_to_octal(res)
    return octal

#from bin to octal
def bin_to_octal(number1):#you can input str or int values
    number1=int(number1)
    list_octal=""
    while number1!=0:
        remin=number1%(10**3)
        remin=bin_to_dec(remin)
        list_octal=str(remin)+list_octal
        number1=int(number1/(10**3))
    return list_octal# the returned value is str

#from bin to hexa
def bin_to_hexa(number1):#you can input str or int values
    number1=int(number1)
    list_hexa=""
    while number1!=0:
        remin=number1%(10**4)
        remin=bin_to_dec(remin)
        if remin==10:
            remin='A'
        if remin==11:
            remin='B'
        if remin==12:
            remin='C'
        if remin==13:
            remin='D'
        if remin==14:
            remin='E'
        if remin==15:
            remin='F'    
            
        list_hexa=str(remin)+list_hexa
        number1=int(number1/(10**4))
    return list_hexa# the returned value is str


def octal_to_binary(octal_num):
    b = ""
    for i in range(len(octal_num)-1,-1,-1):# a is the conversion of octal digit to binary number
        if octal_num[i]=="0":
            a = "000"

        elif octal_num[i]=="1":
            a = "001"

        elif octal_num[i]=="2":
            a = "010"

        elif octal_num[i]=="3":
            a = "011"
        elif octal_num[i]=="4":
            a = "100"

        elif octal_num[i]=="5":
            a = "101"

        elif octal_num[i]=="6":
            a = "110"

        elif octal_num[i]=="7":
            a = "111"
        b =a+b
    return(b)

def hexa_to_bin(number1):
    list_bin=''
    for i in range(len(number1)-1,-1,-1):# a is the conversion of hexa digit to binary number
        if number1[i]=="0":
            a = "0000"

        elif number1[i]=="1":
            a = "0001"

        elif number1[i]=="2":
            a = "0010"

        elif number1[i]=="3":
            a = "0011"
        elif number1[i]=="4":
            a = "0100"

        elif number1[i]=="5":
            a = "0101"

        elif number1[i]=="6":
            a = "0110"

        elif number1[i]=="7":
            a = "0111"
        elif number1[i]=="8":
            a='1000'
        elif number1[i]=="9":
            a='1001'    
        elif number1[i]=="A":
            a='1010'
        elif number1[i]=="B":
            a='1011'
        elif number1[i]=="C":
            a='1100'
        elif number1[i]=="D":
            a='1101'
        elif number1[i]=="E":
            a='1110'
        elif number1[i]=="F":
            a='1111'
        list_bin=a+list_bin
    return list_bin    
   


##main program##
while True:
    print('**numbering system converter**')#starting the program 
    print("A) insert a new number ")
    print("B) exit program")
    choice=input()
    if choice=='B':#to exit the program
        break
    elif choice=='A' :#if there any calculations he will enter the number
        number=input("please enter the number")## #there will be more space than int ?
        while True:
              
            print('**please select the base you want to convert anumber from**\nA)Decimal\nB)Binary\nC)octal\nD)hexadecimal')
            from_base=input()#he enters the system he wants to convert from
        
            
            if from_base=='A'or from_base=='B'or from_base=='C'or from_base=='D':
              while True:
                  
               print('**Please select the base you want to convert a number to **')
               print('A) Decimal\nB) Binary\nC) octal\nD) hexadecimal')
               to_base=input()#he enters the system he wants to convert to
               if to_base=='A'or to_base=='B'or to_base=='C' or to_base=='D':
                  ###all calculations is here 
                  if from_base==to_base:
                      print(number)
                  elif from_base=='A' and to_base=='B':
                      print(dec_to_bin(number))
                  elif from_base=='A' and to_base=='C':
                      print(dec_to_octal(number)) 
                  elif from_base=='A' and to_base=='D':
                      print(dec_to_hexa(number))   
                 
                  elif from_base=='B' and to_base=='A':
                      print(bin_to_dec(number))
                      
                  elif from_base=='B' and to_base=='C':
                      print(bin_to_octal(number))
                  elif from_base=='C' and to_base=='A':
                      print(octal_to_decimal(number))
                  elif from_base=='C' and to_base=='B':
                      print(octal_to_binary(number))
                  elif from_base=='C' and to_base=='D':
                      print(octal_to_hexa(number))    
                  elif from_base=='D' and to_base=='A':
                      print(hexa_to_dec(number))    
                  elif from_base=='D' and to_base=='B':
                      print(hexa_to_bin(number))    
                  elif from_base=='D' and to_base=='C':
                      print(hexa_to_oct(number))    
                      
                  break
               else :
                  print('please enter a valid choice')
              break        
            else:
               print('please enter a valid choice')
        
    else :#we will repeat the program from the begining if he chosed choice not valid at the begining of the program
        print("please chose a valid choice")
        
# fatema elzhraa ahmed mohamed elfiky 20230280
# doha fathy refaey khodary mustafa 20230197
# alaa tarek mohamed salah el den ahmed 20230064