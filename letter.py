'''To replace a string with another string'''
letter='''Dear <|Name|>,
I am happy to tell you about your selection.
     You are selected.
     Have a great day ahead.
     Thanks and regards.

    Date:-<|date|>
    '''
print(letter)
name=input("Enter name \n")
date=input("Enter date \n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)
