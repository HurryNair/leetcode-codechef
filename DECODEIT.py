#Filename : DECODEIT.py

t = int(input())

for i in range(t):

    #Accept inputs
    n = int(input())
    s = input()

    #Declare output
    decoded_string = ""

    #extract encoded strings seperately
    #decode them individually
    #join() decoded character to 
    #resulatant string

    for i in range(0, n, 4):
        encoded_string = s[i:i+4]
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

        #check if the character is in first 8 or last 8
        if encoded_string[0] == '0':
            alphabets = alphabets[0:len(alphabets)/2]
        elif encoded_string[0] == '1':
            alphabets = alphabets[len(alphabets)/2:len(alphabets)]
        
        #check if the character is in first 4 or last 4
        if encoded_string[1] == '0':
            alphabets = alphabets[0:len(alphabets)/2]
        elif encoded_string[1] == '1':
            alphabets = alphabets[len(alphabets)/2:len(alphabets)]
        
        #check if the character is in first 2 or last 2
        if encoded_string[2] == '0':
            alphabets = alphabets[0:len(alphabets)/2]
        elif encoded_string[2] == '1':
            alphabets = alphabets[len(alphabets)/2:len(alphabets)]

        #check if the character is in first 4 or last 4
        if encoded_string[3] == '0':
            alphabets = alphabets[0:len(alphabets)/2]
        elif encoded_string[3] == '1':
            alphabets = alphabets[len(alphabets)/2:len(alphabets)]
        
        decoded_string += alphabets[0]
        
    print(decoded_string)
    



        
