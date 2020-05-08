# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:53:23 2020

@author: bharadwaj
"""

import sys
import struct


string = "" #string = null
result= []  #empty list to store the data 

n, Input = sys.argv[1:] #Tking input from cmd
max_table_size = pow(2,int(n)) # max_table_size = 2^n
file= open(Input) #opening the file
D= file.read()  #reading the file
D=D.strip()

table_size = 256

table = {chr(i): i for i in range(table_size)} #initializing dictionary with ascii code for individual characters 


for symbol in D:  # while there are still input symbols
    s_s = string + symbol  
    if s_s in table: #if string+symbol is in table
     string = s_s #string = string + symbol
    else:
        result.append(table[string])  #output the code for string
        if (len(table) <= max_table_size): #if table is not full
            table[s_s] = table_size # string + symbol now has a code
            table_size += 1
        string = symbol #string = symbol
result.append(table[string]) #output the code for string
   
output = Input.split(".") # splitting the inutfile.txt into input and file
outFile = open(output[0] +".lzw", "wb") #creating inputfile.lzw

for m in result:
    outFile.write(struct.pack('>H', int(m))) #converting the values in result to 2bytes format
                                             # and writting them to inputfilr.lzw   
outFile.close()
file.close()
    
