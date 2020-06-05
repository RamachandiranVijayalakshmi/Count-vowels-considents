#count the number of vowels & considents,words,white spaces in a line of txt.
def string(a):
    b=a.lower()
    length=len(b)
    print('length of your line',length)
    s=b.split()
    space=b.count(' ')
    c=0
    e=0
    d=["a","e","i","o","u"]
    for i in b:
       if i in d:
          c=c+1
       else:               
          e=e+1
    print("Number of vowels in given sentence is:",c)  
    print('Number of considents in given sentence is:',(e-space))    
    print('Number of whitespace in given sentence is:',space)
    print('Number of words in given sentence is:',len(s))
f=str(input('Enter your line of string:'))#dont enter the special charactrs and numbers
string(f)
