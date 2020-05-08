# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:03:02 2020

@author: bharadwaj
"""

import sys

import struct

n, Input = sys.argv[1:] #taking the input
file = open(Input, "rb") #reading the input file

bytes_to_dec = [] #empty list
t = True
while t:
    m = file.read(2) #reading every 2 bytes from the input
    if  len(m) != 2:
        break
    (dec, ) = struct.unpack('>H', m) #converting those bytes to decimal
    bytes_to_dec.append(dec) #updating the list after converrting the bytes
    
max_table_size = pow(2,int(n)) #max_table_size = 2^n
next_code = 256
table_size = 256

decoded = "" #empty string
table = {i: chr(i) for i in range(table_size)} #declaring the dictionary

for code_idx, code in enumerate(bytes_to_dec):
    
    if code_idx == 0: #checking if index of code = zero
        string = table[code] 
        decoded = decoded+string
    else:
        if code not in table: # if Table[code] is not defined
            new_string = string + (string[0]) # new_string = string + string[0]
        else:
            new_string = table[code] # new_string = Table[code]
        decoded = decoded + new_string #output new_string
        if (len(table) <= max_table_size) : #if Table.size < max_table_size
            table[next_code] = string + (new_string[0]) # add string + new_string[] to table
            next_code +=1  
        string = new_string #string = new string
        
output = Input.split(".") # splitting inputfile.lzw into inputfilr and lzw
outFile = open(output[0] +"_decoded.txt", "w") #creating inputfile_decoded.txt file

for dec in decoded: 
    outFile.write(dec)  #writting everything in string decoded to inputfile_decoded.txt
    
outFile.close()
file.close()
     
        
    

 
