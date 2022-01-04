word='Pakistan'
word[0] #character in position 0
'P'     #output
word[5] #character in position 5
't'     #output
word[-1] #last character
'n'     #output
word[-2] #second last character
'a'     #output
word[-6]
'k'     #output
word[0:2] #character from position 0 (included) to position 2 (excluded)
'Pa'   #output
word[2:5] # character from position 2 (included) to position 5 (excluded)
'kis'  #output
word[:2] + word[2:]
'Pakistan'  #output
word[:4] + word[4:]
'Pakistan'  #output
word[:2] #character from the beginning to position 2 (excluded)
'Pa'    #output
word[4:] #character from position 4 (included) to last character
'stan'  #output
word[-2:] #character from second last (included) to the end
'an'    #output
'j' + word[1:]
'jakistan'  #output
word[:2] + 'Pak'
'PaPak' #output
len(word) # length of the string
8   #output
print(word)
