# deoxyencryptingnucleicacids
A really, really bad way to encrypt your text.

### A general description of the scheme
Encoding: The ascii plaintext is first converted into binary, then it is encoded into DNA nucleotides two bits at a time, where a 00 is encoded into an A, a 01 is encoded into a T, a 10 is encoded into a G, and an 11 is encoded into a C.

Encrypting 1: The program then interlaces random data between the encoded real data. To determine where, it uses a key which is hashed with the MD5 algorithm.

Encrypting 2: The first hex digit of the hash determines how many "real" nucleotides are going to be first in the encrypted text. Then the second digit determines how many "fake" nucleotides are included after that. This repeats until it runs out of hash, then it starts over from the beginning of the hash if necessary.

### The Python Script
I wanted to turn it into a command line tool, so i did.

Use: DNA.py [mode: e, d, en, de] [file] [key]

The mode determines what the program does. e and d encode and decode the file, respectively, as described in Encoding. Since I don't know how to use python, to use this mode a key must still be specified but it is not used. 

en and de decrypt the file with the given key, as described in Encrypting 1 and 2.


This scheme was created for Killer Queen CTF 2021. Competitors were tasked with reverse engineering the scheme.
