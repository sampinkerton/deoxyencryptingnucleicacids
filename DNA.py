import argparse
import random
import hashlib

A = "00"
T = "01"
G = "10"
C = "11"

nt = ["A", "T", "G", "C"]

def bin2dna(s):
	re = ""
	for i in range(0, len(s), 2):
		if s[i] + s[i+1] == A:
			re += "A"
		if s[i] + s[i+1] == T:
			re += "T"
		if s[i] + s[i+1] == G:
			re += "G"
		if s[i] + s[i+1] == C:
			re += "C"
	return re

def dna2bin(s):
	bin = ""
	for i in s:
		if i == "A":
			bin += "00"
		if i == "T":
			bin += "01"
		if i == "G":
			bin += "10"
		if i == "C":
			bin += "11"
	return(bin)


def str2bin(s):
	return ''.join(format(ord(i), '08b') for i in s)

def bin2str(s):
	return ''.join( chr( int( s[i : i+8], 2) ) for i in range(0, len(s), 8))

def dna2str(s):
	bin = dna2bin(s)
	return bin2str(bin)

def str2dna(s):
	bin = str2bin(s)
	return bin2dna(bin)

def makeintron(l):
	return ''.join(nt[random.randint(0,3)] for i in range(int(l)))

def decstr(s, pw):
	hash = hashlib.md5()
	hash.update(pw.encode())
	hashed = hash.hexdigest()

	total = len(s)
	placeh = 0
	i = 0
	place = 0
	re = ""
	while i < total:
		ntidecount = int("0x" + hashed[placeh], 16)
		if i % 2 == 0:
			re += s[place:place + ntidecount]
		i += 1
		place += ntidecount
		placeh += 1
		placeh %= len(hashed)
	bin = ""

	for i in re:
		if i == "A":
			bin += "00"
		if i == "T":
			bin += "01"
		if i == "G":
			bin += "10"
		if i == "C":
			bin += "11"
	return ''.join( chr( int( bin[i : i+8], 2) ) for i in range(0, len(bin), 8))


def encstr(s, pw):
	bDNA = str2bin(s)
	sDNA = bin2dna(bDNA)
	pwmd5 = hashlib.md5(pw.encode())
	hash = pwmd5.hexdigest()
	re = ""
	lengthoffinal = len(sDNA)
	#add padding since I literally have no idea how to deal with it running out of chars

	sDNA += "                               "

	placeh = 0
	i = 0
	while i < lengthoffinal:
		ntidecount = int("0x" + hash[placeh], 16)
		if placeh % 2 == 0:
			re += sDNA[i:i+ntidecount]
			i += ntidecount
		if placeh % 2 == 1:
			re += makeintron(ntidecount)
		placeh += 1
		placeh %= len(hash)
	return re

parser = argparse.ArgumentParser()

parser.add_argument("option", help="Choose what you want to do | e/d : encode/decode without key | de = decrypt | en = encrypt || for options e and d, write anything into the key argument. Why? It's because i'm bad at python.")
parser.add_argument("file", help= "File to be de/encoded/crypted", type=argparse.FileType('r'))
parser.add_argument("key", help ="Key to be used for en/decryption")



args = parser.parse_args()

if args.option == "e":
	print(str2dna(args.file.read()))

elif args.option =="d":
	print(dna2str(args.file.read()))

elif args.option == "de":
	print(decstr(args.file.read(),args.key))

elif args.option == "en":
	print(encstr(args.file.read(),args.key))

