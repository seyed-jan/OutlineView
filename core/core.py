from colorama import Fore
import os
from docx import Document

class Core:
    def __str__(self):
        return "Outline view BackEnd"

    def AddFile(self, FilePath):
        if os.path.exists(FilePath):
            self.FilePath = FilePath

            self.document = Document(self.FilePath)

            result = []
            stack = []

            for paragraph in self.document.paragraphs:
                node = {"data": paragraph, "childrens": []}

                while\
                stack and\
                stack [-1]["data"].style.name >= node["data"].style.name and\
                node["data"].style.name != "Normal":
                    stack.pop()
                
                if not stack:
                    result.append(node)
                else:
                    stack[-1]["childrens"].append(node)
                
                stack.append(node)

                self.OriginalResult = result
        else:
            print(Fore.RED, f"'{FilePath}' Not Found or it is wrong! please trye agane.", Fore.RESET)
    
    
    def GetResult(self):
        return self.result

    def UpdateResultForShowToLevel(self, level, OriginalResult=None, current_level=1):
        if OriginalResult is None:
            OriginalResult = self.OriginalResult
        fresult = []
        if level != "all":
            for node in OriginalResult:
                if node["data"].style.name == "Normal":
                    continue
                new_node = {
                    "data": node["data"],
                    "childrens": []
                }

                if current_level < int(level):
                    new_node["childrens"] = self.UpdateResultForShowToLevel(
                    level,
                    node["childrens"],
                    current_level + 1
                )

                fresult.append(new_node)
            if current_level == 1:
                self.result = fresult
        elif level == "all":
            self.result = self.OriginalResult
        return fresult