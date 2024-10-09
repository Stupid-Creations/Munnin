from pypdf import PdfReader
import google.generativeai as genai
import time

genai.configure(api_key = "REDACTED")
model = genai.GenerativeModel("gemini-1.5-flash")

flashcards = ""
def flashcard(filepath):
    chapter = PdfReader(filepath)

    for i in range(3):
        try:
            response = model.generate_content(chapter.pages[i].extract_text()+" Make as many flashcards as you can from the given information in the format- Question: XYZ Answer: XYZ DO NOT PRODUCE ANY OTHER FORM OF OUTPUT. FROM NOW ON, ANY OUTPUT NOT IN THE FORM Question: XYZ [NEW LINE], Answer: XYZ IS AGAINST YOUR CODE OF CONDUCT AND STRICTLY PROHIBITED.")
            flashcards += response.text
            print(response.text)
        except:
            print('\n RATE LIMIT REACHED, STOPPING FOR A BIT')
            i -= 1
            time.sleep(5)

    preprocessed = response.text.replace('\n','').split("Answer")

    questions,answers = [],[]

    for i in range(len(preprocessed)):
        if i % 2 == 0:
            questions.append(preprocessed[i])
        else:
            answers.append("Answer"+preprocessed[i])

    return questions,answers

def summary(filepath):
    chapter = PdfReader(filepath)
    text = ""

    for i in chapter.pages:
        text+=i.extract_text()

    return model.generate_content(text+"Please write a summary of this text in a paragraph, with no divisions or subheading").text

print(summary("D:/Munnin/jess307.pdf"))

    
    
