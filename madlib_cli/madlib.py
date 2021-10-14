
import re

print("""        *******************
        *******Welcome****** 
***********You are in the Madlib Game ********* 
***********We Hope You'r Ready To play With Us ******
###########################################################
""")

def read_template(path):
    """ function how read file from the url
        and return what that file have 
    """ 
    a=open(path)
    return a.read()

# this function tack a text as a parameter
def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    #split the text to the char
    x=text.split(' ')
    print(x)
    # made regex to check to check on {something} or {something}.
    reg=r"^{\w+}|\.$"
    # loop over the x and x is the array have the text after split it 
    for i in x:
        # check if the regex match it 
        if re.match(reg,i)==None :
            # assign what not matches in actual_stripped
            actual_stripped+=f"{i} "
            # other wise have two cases 
        else :
            # first case is check in this last item
            if i==x[-1]:
                actual_stripped+='{}.'
                actual_parts+=[i[1:-2]]
            # second case is check in this not last item  
            else:
                actual_parts+=[i[1:-1]]
                actual_stripped+='{} '
    # convarert actual_parts from array to tuple then return it and return actual_stripped as a string
    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)
    
# this function is revers what parse_template do   
def merge(text,tep):
    return text.format(*tep)

# this write inside my file  that founded assets/make_me_a_video_game_output_from_user.txt
def create_file(result):
    with open("assets/dark_and_stormy_night_template.txt", "w") as f:
        f.write(result)
        #dark_and_stormy_night_template
""" this function that make interact with user 
and this function will be tack it tomorrow so i will make it as a commant 
"""
def get_data():
    text = read_template("assets/dark_and_stormy_night_template.txt")
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(result)
    create_file(result)


get_data()
