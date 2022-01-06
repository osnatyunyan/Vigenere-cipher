# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:32:26 2020
Student: osnat yunyan
ID: 315773762
Assignment no. 4
Program: vigenere.py 
@author: osnat
"""

def add_letters(s,t):
    """The function receives two strings. If the two strings are one length 
    and represent Latin letters the function will return the sum of the letters.
    The sum of the letters will be by adding their numerical values ​​and the result translated to the appropriate letter.
 If the strings do not represent Latin letters, None will be returned"""
    letters={x:chr(ord("a")+x) for x in range (26)}
    if (len(s)==1 and len(t)==1) and (s.isalpha() and t.isalpha()):
        s ,t=s.lower() ,t.lower()
        new_letter=(ord(s)-ord("a")+ord(t)-ord("a"))%26
        return letters[new_letter]
    return None

def add_string(string1,string2):
    """Receives two strings consisting of Latin letters of different lengths 
    and returns a string where each character is the sum of the corresponding characters in the input strings."""
    for i in string2: #Goes over the string and checks that it is made up of Latin letters
        if i.isalpha() == False:
            return None
    for i in string1: #Goes over the string and checks that it is made up of Latin letters
        if i.isalpha() == False:
            return None
    newstring=''
    for i in range(min([len(string1),len(string2)])):
        newstring += add_letters(string1[i],string2[i])
    return (newstring) 

                
def vigenere_encrypt(s,k):
     """Receives a string and returns the encrypted string using an encryption key"""
     for i in k:#Check if the key is made up of Latin letters
        if not i.isalpha():
            return None
     news=''
     for i in s: #Assembling a string composed of Latin letters
        if i.isalpha():
            news+=i
     t=k
     while len(t)<len(news):
         t+=k
     return (add_string(news,t))
 
def less_letters(s,t):
    """Receives two strings consisting of Latin letters of different lengths 
    and returns a string in which each character is the difference of the corresponding characters in the input strings."""
    if not s.isalpha() or not t.isalpha() or len(t)>1 or len(s)>1:
        return None
    s=s.lower()
    t=t.lower()
    dictletter = {chr(ord('a')+i):i for i in range(26)} #Creates a dictionary where the key is a letter and the value is a number
    numdict={i:chr(ord('a')+i) for i in range(26)} #Creates a dictionary where the key is a number and the value is a letter
    new_letter= numdict[(dictletter[s]-dictletter[t]) % 26]
    return  (new_letter)
    
def vigenere_decrypt(w,k):
    """receives a string and encryption key and returns the result of decoding the string using the key"""
    for i in k: #Checks if the key is made up of Latin letters
        if not i.isalpha():
            return None
    t=k
    while len(t)<len(w):
         t+=k
    new_str=''
    for i in range (len(w)): #Goes over the original string and assembles the new string
        new_str+=less_letters(w[i],t[i])
    return (new_str)
        
def e(key,file):
    """The program encrypts the contents of the document and writes it to a new file"""
    try:
        f = open(file,'r')
        s = f.read()
        f.close()
    except IOError:
          return("File not accessible")
    f = open(file,'r')
    s = f.read()
    f.close() 
    f_vig=file.replace("txt","vig")
    new_f=open(f_vig,'w')
    new_f.write(vigenere_encrypt(s,key))
    new_f.close
    return ""
    
    
def d(key,file):
    """The program will decode the text in the file and print the decoding result to the screen"""
    try:
        f = open(file,'r')
        s = f.read()
        f.close()
    except IOError:
          return("File not accessible")
    f = open(file,'r')
    s = f.read()
    f.close()
    return (vigenere_decrypt(s,key))   
    
def main():
    """The program will implement writing and decoding a code for text files that contain Latin letters"""
    number_use= input("Please choose between e and d-  ")
    if number_use=="e":
        key=input("please write Encryption key- ")
        file=input("please write  name of file- ")
        print(e(key,file))
    if number_use=="d":
        key=input("please write Encryption key- ")
        file=input("please write name of file- ")
        print (d(key,file))
main()
        
        
        
        
        
        
        
         
            