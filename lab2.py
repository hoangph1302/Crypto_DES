def ChangeBinaryToDecimal(bin):
	return  int(bin, 2)
def ChangeDecimalToBinary(dec):
	return "{0:04b}".format(dec)

def ChangeBinaryToHex(bin):
	hex=''
	hex = f'{int(bin, 2):X}'
	return hex

def  Permutation(input,tablePermutation):
	output=""
	for x in range(0,len(tablePermutation)):
		output=output+input[tablePermutation[x]-1]
	return output

tablePermutation_PC1=[57, 49, 41, 33, 25, 17, 9,
                      1, 58, 50, 42, 34, 26, 18,
                      10, 2, 59, 51, 43, 35, 27,
                      19, 11, 3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15,
                      7, 62, 54, 46, 38, 30, 22,
                      14, 6, 61, 53, 45, 37, 29,
                      21, 13, 5, 28, 20, 12, 4 ]

tablePermutation_PC2=[14, 17, 11, 24, 1, 5,
                      3, 28, 15, 6, 21, 10,
                      23, 19, 12, 4, 26, 8,
                      16, 7, 27, 20, 13, 2,
                      41, 52, 31, 37, 47, 55,
                      30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53,
                      46, 42, 50, 36, 29, 32 ]


tableInitialPermutation=[58,50,42,34,26,18,10,2,
						 60,52,44,36,28,20,12,4,
						 62,54,46,38,30,22,14,6,
						 64,56,48,40,32,24,16,8,
						 57,49,41,33,25,17,9,1,
						 59,51,43,35,27,19,11,3,
						 61,53,45,37,29,21,13,5,
						 63,55,47,39,31,23,15,7]

expansion32bitTo42bit=[32,1,2,3,4,5,
			   4,5,6,7,8,9,
			   8,9,10,11,12,13,
			   12,13,14,15,16,17,
			   16,17,18,19,20,21,
			   20,21,22,23,24,25,
			   24,25,26,27,28,29,
			   28,29,30,31,32,1]

# selection function S1,S2,S3,S4,S5,S6,S7,S8
sBoxTable =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],  
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],  
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],  
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]], 
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],  
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],  
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],  
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],  
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],  
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],  
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],  
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],  
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],  
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],  
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],  
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],  
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],  
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],  
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],  
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],  
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],  
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],  
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],  
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],  
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],  
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],  
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],  
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],  
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],  
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],  
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],  
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]

PBox=[ 16,  7, 20, 21,
		29, 12, 28, 17,
		1, 15, 23, 26,
		5, 18, 31, 10,
		2,  8, 24, 14,
		32, 27,  3,  9,
		19, 13, 30,  6,
		22, 11,  4, 25 ]

finalPermutation=[ 40, 8, 48, 16, 56, 24, 64, 32,
				   39, 7, 47, 15, 55, 23, 63, 31,
				   38, 6, 46, 14, 54, 22, 62, 30,
				   37, 5, 45, 13, 53, 21, 61, 29,
				   36, 4, 44, 12, 52, 20, 60, 28,
				   35, 3, 43, 11, 51, 19, 59, 27,
				   34, 2, 42, 10, 50, 18, 58, 26,
				   33, 1, 41, 9, 49, 17, 57, 25 ]

def ChangeHexToBinary(hex):
	binary=""
	binary=format(int(hex, 16), "064b")
	return binary

def LeftShift1(input):
	output=""
	for x in range(0,27):
		output=output+input[x+1]
	output=output+input[0]
	return output

def LeftShift2(input):
	output=""
	for x in range(0,26):
		output=output+input[x+2]
	output=output+input[0]
	output=output+input[1]
	return output

def XOR(input1,input2):
	output=""
	for x in range(0,len(input1)):
		if input1[x]==input2[x]:
			output=output+"0"
		else:
			output=output+"1"
	return output

def KeyShedule(key):
	keyBin=Permutation(ChangeHexToBinary(key),tablePermutation_PC1) #56 bits of the key are selected from the initial 64 by Permuted Choice 1 (PC-1)
	arrayKey=[]
	C=keyBin[0:28] #The 56 bits are then divided into two 28-bit halves C and D
	D=keyBin[28:56]

	for x in range(1,17):
		if (x==1 or x==2 or x==9 or x==16):
			C=LeftShift1(C)
			D=LeftShift1(D)
			keyLeftShift=C+D
			arrayKey.append(Permutation(keyLeftShift,tablePermutation_PC2)) #48 subkey bits are selected by Permuted Choice 2 (PC-2)
		else:
			C=LeftShift2(C)
			D=LeftShift2(D)
			keyLeftShift=C+D
			arrayKey.append(Permutation(keyLeftShift,tablePermutation_PC2)) #48 subkey bits are selected by Permuted Choice 2 (PC-2)
	return arrayKey

def encrypt(plaintext,key):
	arrayKey=KeyShedule(key)
	plaintextBin=Permutation(ChangeHexToBinary(plaintext),tableInitialPermutation)
	left=plaintextBin[0:32]
	right=plaintextBin[32:64]
	permutationP="0"

	for x in range(0,16):
		if(x==0):
			print("  Key: - "+" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )
		else:
			print("  Key: "+ChangeBinaryToHex(arrayKey[x-1]) +" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )
		middle=right
		right=Permutation(right,expansion32bitTo42bit)
		keyMixing=XOR(right,arrayKey[x])  ##subkey using an XOR operation. Sixteen 48-bit subkeys—one for each round
		s=[keyMixing[0:6],keyMixing[6:12],keyMixing[12:18],keyMixing[18:24],   #the block is divided into eight 6-bit pieces before processing by the S-boxes
			 keyMixing[24:30],keyMixing[30:36],keyMixing[36:42],keyMixing[42:48]]
		substitution=''

		for i in range(0,8):
			row=''
			row=(s[i][0])
			row=row+s[i][5]
			row=ChangeBinaryToDecimal(row)
			column=''
			for j in range(1,5):
				column=column+s[i][j]
			column=ChangeBinaryToDecimal(column)

			substitution=substitution+ChangeDecimalToBinary(sBoxTable[i][row][column])

		permutationP=Permutation(substitution,PBox)

		right=XOR(left,permutationP)
		left=middle
	print("  Key: "+ChangeBinaryToHex(arrayKey[15]) +" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )

	print ("cipherText: "+ChangeBinaryToHex(Permutation((right+left),finalPermutation)))



def dencrypt(ciphertext,key):
	arrayKey=KeyShedule(key)
	ciphertextBin=Permutation(ChangeHexToBinary(ciphertext),tableInitialPermutation)
	left=ciphertextBin[0:32]
	right=ciphertextBin[32:64]
	permutationP="0"
	for x in range(0,16):
		if(x==0):
			print("  Key: - "+" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )
		else:
			print("  Key: "+ChangeBinaryToHex(arrayKey[16-x]) +" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )
		middle=right

		right=Permutation(right,expansion32bitTo42bit) #the 32-bit half-block is expanded to 48 bits using the expansion permutation
		keyMixing=XOR(right,arrayKey[15-x])
		s=[keyMixing[0:6],keyMixing[6:12],keyMixing[12:18],keyMixing[18:24],
		   keyMixing[24:30],keyMixing[30:36],keyMixing[36:42],keyMixing[42:48]]
		substitution=''
		for i in range(0,8):
			row=''
			row=(s[i][0])
			row=row+s[i][5]
			row=ChangeBinaryToDecimal(row)
			column=''
			for j in range(1,5):
				column=column+s[i][j]
			column=ChangeBinaryToDecimal(column)

			substitution=substitution+ChangeDecimalToBinary(sBoxTable[i][row][column])

		permutationP=Permutation(substitution,PBox)

		right=XOR(left,permutationP)
		left=middle
	print("  Key: "+ChangeBinaryToHex(arrayKey[0]) +" F(R,K): "+ChangeBinaryToHex(permutationP)+ "  L: "+ChangeBinaryToHex(left)+ " R: "+ChangeBinaryToHex(right)   )

	print ("Plaintext: "+ChangeBinaryToHex(Permutation((right+left),finalPermutation)))


#----------------------------------------------------main programme-------------------------------------------------------------------------------
print ("Data Encryption Standard")
option = int(input('1.encrypt \n2.decrypt\n'))
if option==1:
	print ("please enter plaintext(64bit)!")
	plaintext=input()
	print ("please enter key(64bit)!")
	key=input()
	encrypt(plaintext,key)

else:
	print ("please enter ciphertext(64bit)!")
	ciphertext=input()
	print ("please enter key(64bit)!")
	key=input()
	dencrypt(ciphertext,key)