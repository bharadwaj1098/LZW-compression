# LZW-compression
The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm.
The two steps of LZW Algorithm are Encoding and decoding

ENCODING:

The endoing part of the program takes place in encoding.py

Encoding Program design:

1) First the no:- of bits and input file is taken as input
2) Then the characers in the file are read.
3) A python dictionary data structure, initialized to a of size 256.
4) This dictionary has characters as keys and ASCII values as values.
5) After this the LZW encoding algorithm is implemented.
6) The dictionary keeps updating while the encoding algorithm runs.
7) Inputfile.txt is split into "inputfile", "txt" and inputfile.lzw is formed
8) All the encoded data which is in the list "result" will be converted into 2-bytes format using " STRUCT>PACK() ".
9) The encoded data is then written into "inputfile.lzw"

Pseudocode for encoding:

MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
initialize TABLE[0 to 255] = code for individual characters
STRING = null
while there are still input symbols:
SYMBOL = get input symbol
if STRING + SYMBOL is in TABLE:
STRING = STRING + SYMBOL
else:
output the code for STRING
If TABLE.size < MAX_TABLE_SIZE: // if table is not full
add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
STRING = SYMBOL
output the code for STRING


DECODING:

The decoding part of the program takes place in decoding.py

Decoding Program design:

1) First the no:- of bits ang inputfile.lzw are taken as input.
2) Then the data in input.lzw which is in 2-bytes format is converted    to decimal format using " STRUCT.UNPACK() ."
3) All of these values are added to a list " bytes_to_dec ."
4) A python dictionary data structure, initialized to a of size 256.
5) This dictionary has ASCII values as keys and characters as values.
6) LZW decoding algorithm is implemented.
7) The string "decoded" keeps updating while the decoding algorithm runs.
8) The end result i.e; decoded at the end of iteration is written in inputfile_decoded.txt

Pseudocode for decoding:

MAX_TABLE_SIZE=2(bit_length)
initialize TABLE[0 to 255] = code for individual characters
CODE = read next code from encoder
STRING = TABLE[CODE]
output STRING
while there are still codes to receive:
CODE = read next code from encoder
if TABLE[CODE] is not defined: // needed because sometimes the
NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
else:
NEW_STRING = TABLE[CODE]
output NEW_STRING
if TABLE.size < MAX_TABLE_SIZE:
add STRING + NEW_STRING[0] to TABLE
STRING = NEW_STRING


HOW to run the code?

In command prompt open the directory in which the program is saved.
then give a input of
"python encoded.py <bit-length> <input.txt>"
The output of this code is stored in input.lzw in 16 bit format.
To run the decoding give a input of
"python decoded.py <bit-length> <input.lzw>
The decoded file will be stored in input_decoded.txt file.
The input.txt file will be same as the input_decoded.txt file.

The efficiency of the program depends on the Size of data.










