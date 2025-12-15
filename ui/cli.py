def ShowInTerminal(result, first_level=0):
    for item in result:
        print(first_level*" "+item["data"].text)
        ShowInTerminal(item["childrens"], first_level+1)