
import re

print("Welcome You are in the Madlib Game")

def read_template(path):
    """ function how read file from the url
        and return what that file have 
    """ 
    a=open(path)
    return a.read()

def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    
    x=text.split(' ')
    print(x)
    reg=r"^{\w+}|\.$"
    for i in x:
        if re.match(reg,i)==None :
            actual_stripped+=f"{i} "
        else :
            if i==x[-1]:
                actual_stripped+='{}.'
                actual_parts+=[i[1:-2]]
            else:
                actual_parts+=[i[1:-1]]
                actual_stripped+='{} '
    
    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)
    
    
def merge(text,tep):
    return text.format(*tep)


parse_template("It was a {Adjective} and {Adjective} {Noun}.")