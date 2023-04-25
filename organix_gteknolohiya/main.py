from core import Prompt
from utils import recognize_speech, clc_print, print_with_delay

def main():
    prompt = Prompt()
    
    program_on = True

    while program_on == True:
        prompt.ask_task("organize", "rename", "delete", "exit")
        todo = recognize_speech()  

        while True:
            if todo == "organize":
                prompt.confirm_task("organize")
                break
            elif todo == "rename":
                prompt.confirm_task("rename")    
                break
            elif todo == "delete":
                prompt.confirm_task("delete")
                break
            elif todo == "exit":
                program_on = False
                clc_print("Bye bitch!")
                break
            else:
                print_with_delay("Invalid response. Please try again.", 2)
                break        

if __name__ == "__main__":
    main()
