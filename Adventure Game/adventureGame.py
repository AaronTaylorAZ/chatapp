import tkinter as tk

def update_label_text(text):
    label.config(text=text)

# Create the main window
root = tk.Tk()
root.geometry("700x300")
root.title("Interactive Q&A")
root.resizable(False, False)
background_color = "#5c8a8a"
foreground_color = "black"
root.configure(bg=background_color)

narrator_fontstyle = ("Helvetica", 20, "bold")

# Create a label widget
label = tk.Label(root, text="Hello, Adventurer!hjd asd das dsa asd ", font=narrator_fontstyle, fg=foreground_color, bg=background_color, wraplength=2)

# Pack the label widget to add it to the main window
label.pack()

# Define a list of questions and their corresponding answers
questions_and_answers = [
    {"question": "What is your name?", "answer": "Welcome, Aaron."},
    {"question": "Where are you from?", "answer": "I am from a fara4way land.",},

]

def get_input_text():
    entered_text = entry.get()  # Get the text from the input field
    current_question_index = get_input_text.current_question_index
    if current_question_index < len(questions_and_answers):
        update_label_text(questions_and_answers[current_question_index]["answer"])
        current_question_index += 1
    else:
        update_label_text("No more questions. Thank you!")
    get_input_text.current_question_index = current_question_index

get_input_text.current_question_index = 0  # Track the current question

# Create an input field (Entry widget)
entry = tk.Entry(root, width=30)  # You can specify the width of the input field

# Create a button to trigger the input retrieval
submit_button = tk.Button(root, text="Submit", command=get_input_text)

# Pack the widgets to add them to the main window
entry.pack()
submit_button.pack()

# Start the GUI main loop
root.mainloop()
