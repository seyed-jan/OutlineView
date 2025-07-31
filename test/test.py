from docx import Document

document = Document("test.docx")

for paragraph in document.paragraphs:
    print(paragraph.style.name)
    print(paragraph.text.strip())