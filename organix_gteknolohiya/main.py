from core import Prompt
from utils import recognize_speech, clc_print, print_with_delay

def main():
    prompt = Prompt()
    
    program_on = True

    while program_on == True:
        prompt.ask_task("organize", "rename", "delete", "exit")
        response = recognize_speech()  

        while True:
            if "organize" in response:
                prompt.confirm_task("organize")
                break
            elif "rename" in response:
                prompt.confirm_task("rename")    
                break
            elif "delete" in response:
                prompt.confirm_task("delete")
                break
            elif "exit" in response:
                program_on = False
                clc_print("Bye bitch!")
                break
            else:
                print_with_delay("Invalid response. Please try again.", 2)
                break        

if __name__ == "__main__":
    main()
