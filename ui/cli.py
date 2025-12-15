import os
from colorama import Fore

class CLI:
    def __init__(self, ParserFunction):
        self.parser = ParserFunction
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcom to OutlineView Command Line Interface!")

        print("Enter help for show help.")
        while True:
            command = input("OVCLI: ")
            command = command.split()
            if command[0] == "help":
                self.ShowHelp()
            
            if command[0] == "add-file":
                try:
                    command[1]
                except:
                    print(Fore.RED, f"add-file has one parametr: add-file <path>. please trye agane.", Fore.RESET)
                    continue
                else:    
                    self.AddFile(command[1])

            if command[0] == "show-to-level":
                try:
                    command[1]
                except:
                    print(Fore.RED, f"show-to-level has one parametr: show-to-level <level>. please trye agane", Fore.RESET)    
                else:
                    try:
                        self.result
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
                                self.ShowLevels(command[1])
                        elif command[1] == "all":
                            self.ShowLevels(command[1])

            if command[0] == "exit":
                print("Good By!")
                break
    
    def ShowHelp(self):
        print("""
This is OutlineView CLI.
help                                    show help.
exit                                    exit from cli.
add-file <word-file-path>               add a word file with path.
show-to-level <level:.\example>         show file to <level> level with tree view.
        """)

    def AddFile(self, path):
        if os.path.exists(path):
            self.FilePath = path
            self.result = self.parser(path)
        else:
            print(Fore.RED, f"'{path}' Not Found or it is wrong! please trye agane.", Fore.RESET)


    def FilterByLevel(self, result, level, current_level=1):
        fresult = []
        for node in result:
            if node["data"].style.name == "Normal":
                continue
            new_node = {
                "data": node["data"],
                "childrens": []
            }

            if current_level < level:
                new_node["childrens"] = self.FilterByLevel(
                node["childrens"],
                level,
                current_level + 1
            )

            fresult.append(new_node)
        return fresult

    def ShowLevels(self, level):
        os.system('cls' if os.name == 'nt' else 'clear')
        if level == "all":
            self.ShowInTerminal(self.result)
        else:
            fresult = self.FilterByLevel(self.result, int(level))
            self.ShowInTerminal(fresult)
        print("\n")

    def ShowInTerminal(self, result, first_level=0):
        for item in result:
            if item["data"].style.name != "Normal":
                print(first_level*" "+"~ "+item["data"].text)
                self.ShowInTerminal(item["childrens"], first_level+1)
            else:
                print(first_level*" "+"- "+item["data"].text)