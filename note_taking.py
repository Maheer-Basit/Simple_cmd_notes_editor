import os 
os.getcwd()
def main():
    is_active = True
    while is_active:
        file, event = user_input()
        output_file = open(f"{file}.txt", "a")
        input_file = open(f"{file}.txt", "r")

        if event == "view":
            view_notes(input_file)
        elif event == "write":
            add_notes(output_file, file)
        elif event == "search":
            search_notes(input_file)
        elif event == "delete":
            delete_note(input_file)
        elif event == "exit":
            is_active == False
            break
        
    
def user_input():
    file_selection = input("Enter the file you wish to select: ")
    user_selection = input("Enter what you would like to do with the file (options are view, write, search, delete): ").strip(" ")
    return file_selection, user_selection

def add_notes(output_file, file):
    user_input = input("Enter your input: ")
    output_file.write(user_input + "\n")
    output_file.close()


def view_notes(input_file):
    contents = input_file.read()
    print(contents)
    input_file.close()
    

def search_notes(input_file):
    word = input("Enter the word you are searching for: ")
    contents = input_file.read()
    if word in contents:
        print(word)
    input_file.close()


def delete_note(input_file):

    word = input("Enter the word you want to delete: ")
    contents = input_file.read()
    if word in contents.split():
        contents = contents.replace(word, "")
        contents = contents.replace("  ", " ")
    print(contents)
    input_file.close()

main()