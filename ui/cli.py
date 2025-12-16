import os
from colorama import Fore

class CLI:
    def __init__(self, Backend):
        self.backend = Backend()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcom to OutlineView Command Line Interface!")

        print("Enter help for show help.")
        while True:
            command = input("OVCLI: ")
            command = command.split()
            if command[0] == "help":
                self.ShowHelp()
            
            elif command[0] == "add-file":
                try:
                    command[1]
                except:
                    print(Fore.RED, f"add-file has one parametr: add-file <path>. please trye agane.", Fore.RESET)
                    continue
                else:
                    self.backend.AddFile(command[1])

            elif command[0] == "show-to-level":
                try:
                    command[1]
                except:
                    print(Fore.RED, f"show-to-level has one parametr: show-to-level <level>. please trye agane", Fore.RESET)    
                else:
                    try:
                        self.backend.document
                    except:
                        print(Fore.RED, "Not Added A File. Use add-file", Fore.RESET)
                        continue
                    else:
                        if command[1] != "all":
                            try:
                                int(command[1])
                            except:
                                print(Fore.RED, f"'{command[1]}' is not a number. please onle enter number of level or 'all' for all levels.", Fore.RESET)
                                continue
                            else:
                                self.backend.UpdateResultForShowToLevel(command[1])
                                os.system('cls' if os.name == 'nt' else 'clear')
                                self.ShowInTerminal()
                                print("\n")
                        elif command[1] == "all":
                            self.backend.UpdateResultForShowToLevel(command[1])
                            os.system('cls' if os.name == 'nt' else 'clear')
                            self.ShowInTerminal()
                            print("\n")

            elif command[0] == "exit":
                print("Good By!")
                break
            
            else:
                print(Fore.RED, f"'{command[0]}' Not Found! 'help' for show help.", Fore.RESET)

    
    def ShowHelp(self):
        print("""
This is OutlineView CLI.
help                                              show help.
exit                                              exit from cli.
add-file <word-file-path:.\example>               add a word file with path.
show-to-level <level>                             show file to <level> level with tree view.
            """)


    def ShowInTerminal(self, result=None, first_level=0):
        if result is None:
            result = self.backend.GetResult()
        
        for item in result:
            if item["data"].style.name != "Normal":
                print(first_level*" "+f"{first_level+1}- "+item["data"].text)
                self.ShowInTerminal(item["childrens"], first_level+1)
            else:
                print(first_level*" "+"~ "+item["data"].text)