from docx import Document

def Parser(filepath):

    document = Document(filepath)

    result = []
    stack = []

    for paragraph in document.paragraphs:
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

    return result
