#Imports
import random 

#Characters
lower = "abcdefghijklmopqrstuvwxyz" 
Upper= "ABCDEFGHIJKLMNOPQRSTUQWXYZ"
Symbols= "{}[]!@#$%^&*()_.;',/-=[]\`+_:''<>?" #Symbols
Numbers="0123456789"#Numbers
all = lower+Upper+Symbols #This adds the whole thing
len=10 #how many charapcters will be there in the password
passcode= "".join(random.sample(all,len)) #It will join the whole thing and randomley select the passcode
print("The password you generated is :",passcode) #Print the password
