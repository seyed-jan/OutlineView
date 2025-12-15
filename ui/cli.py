import os
class CLI:
    def __init__(self, result):
        self.result = result
        while True:
            level = input("Enter number of Level for show ('all' for show all levels and body texts, 'end' for end):")
            if level != "all" and level != "end":
                try:
                    int(level)
                except:
                    from colorama import Fore
                    print(Fore.RED, f"'{level}' is not a number. please onle enter number of level.", Fore.RESET)
                    continue
            if level == "end":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Good By.")
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            self.ShowLevels(level)
    
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
        if level == "all":
            self.ShowInTerminal(self.result)
        else:
            fresult = self.FilterByLevel(self.result, int(level))
            self.ShowInTerminal(fresult)

    def ShowInTerminal(self, result, first_level=0):
        for item in result:
            print(first_level*" "+item["data"].text)
            self.ShowInTerminal(item["childrens"], first_level+1)