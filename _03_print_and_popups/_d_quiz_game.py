from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    user_score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    name=simpledialog.askstring(title="the question", prompt="When was Jeff Bezos born")
    #      // 3.  Use an if statement to check if their answer is correct
    if name == "1964":
    #      // 4.  if the user's answer was correct, add one to their score 
        user_score += 1
        messagebox.showinfo(title="score", message="1")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    name=simpledialog.askstring(title="2nd question", prompt="Who has the most nba rings")
    if name == "Bill Russel":
        user_score += 1
    messagebox.showinfo(title="score", message="2")
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title="final score", message="your final score: "+ str(user_score))
    # Run the window's .mainloop() method
    window.mainloop()