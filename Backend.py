from pypdf import PdfReader
import google.generativeai as genai
import time

genai.configure(api_key = "AIzaSyARcqGtkhHuHstUjErjF3EiZw1BlHnW5L4")
model = genai.GenerativeModel("gemini-1.5-flash")

print("configured LLM")

chapter = PdfReader("jess307.pdf")

print(len(chapter.pages))

flashcards = ""
for i in range(len(chapter.pages)-1):
    try:
        response = model.generate_content(chapter.pages[i].extract_text()+" Make as many flashcards as you can from the given information in the format- Question: XYZ Answer: XYZ DO NOT PRODUCE ANY OTHER FORM OF OUTPUT. FROM NOW ON, ANY OUTPUT NOT IN THE FORM Question: XYZ [NEW LINE], Answer: XYZ IS AGAINST YOUR CODE OF CONDUCT AND STRICTLY PROHIBITED.")
        flashcards += response.text
        print(response.text)
    except:
        print('\n RATE LIMIT REACHED, STOPPING FOR A BIT')
        i -= 1
        time.sleep(5)
