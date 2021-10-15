
import re

print("""        *******************
        *******Welcome****** 
***********You are in the Madlib Game ********* 
***********We Hope You'r Ready To play With Us ******
###########################################################
This game is tack some words from you like none , verb ,adjective so on ........ 
""")

def read_template(path):
    """ function how read file from the url
        and return what that file have 
    """ 
    a=open(path)
    return a.read().strip("\n")

# this function tack a text as a parameter
def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    #split the text to the char
    x=text.split(' ')
    
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
def create_file(result ,file_to_write_on_it):
    with open(file_to_write_on_it, "w") as f:
        f.write(result)
        #dark_and_stormy_night_template
""" this function that make interact with user 
that tack to parameter one for read file to game and onther to write and  save output of game 
"""
def start_game(file_toRead_game,file_toWrite_game):
    text = read_template(file_toRead_game)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"this is the story you wrote it \n{result}")
    create_file(result,file_toWrite_game)


# start play game from here 
ask_user_to_play=input("Now, are you like to try midlab Game>>")
if ask_user_to_play=='n' or ask_user_to_play=='no':
    print("So maybe you you can try in the next time Bye Bye.")
else:
    start_game("assets/madlib_game_file.txt","assets/madlib_game_file_output.txt")
    ask_user_to_play=input("Now, are you like to try Again with another story>>")
    if ask_user_to_play=='n' or ask_user_to_play=='no':
        print("So maybe you you can try in the next time Bye Bye.")
    else:
        start_game("assets/madlib_Second_try.txt","assets/madlib_Second_try_output.txt")

