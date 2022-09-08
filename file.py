fl=input("Enter the file name")
with open(fl) as file:
    text=file.read()
    count=0
    for char in text:
        if(char=='a'||char=='e'|| char=='i'|| char=='o' ||char=='u')
        count+=1
        print("The number of vowel= ", count)