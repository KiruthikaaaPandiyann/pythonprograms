str=input()
s=str.lower()
l=ord(s)
if(l>=97 and l<=122):
    if(s=='a' or s=='e' or s=='i' or s=='o' or s=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
