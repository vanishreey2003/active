import tkinter as tk
import random
import math

class SquareRootGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Square Root Guessing Game")
        
        self.score = 0
        self.attempts = 0
        
        self.label = tk.Label(master, text="Welcome to the 'Square Root Guessing Game'!\n"
                                             "Select the square root of the number below:")
        self.label.pack(pady=10)

        self.number = random.randint(1, 100)
        self.actual_sqrt = math.sqrt(self.number)
        
        self.number_label = tk.Label(master, text=f"Number: {self.number}")
        self.number_label.pack(pady=10)

        self.create_buttons()

    def create_buttons(self):
        # Generate three incorrect answers and one correct answer
        correct_answer = round(self.actual_sqrt, 2)
        options = [correct_answer]
        
        while len(options) < 4:
            wrong_answer = round(random.uniform(0, 10), 2)
            if wrong_answer not in options:
                options.append(wrong_answer)

        random.shuffle(options)

        # Create buttons for each option
        for option in options:
            button = tk.Button(self.master, text=str(option), command=lambda x=option: self.check_answer(x))
            button.pack(pady=5)

    def check_answer(self, selected):
        self.attempts += 1
        if math.isclose(selected, self.actual_sqrt, abs_tol=0.01):
            self.score += 1
            result_text = f"Correct! You've guessed the square root of {self.number} in {self.attempts} attempts.\n"
            result_text += f"Your score: {self.score}"
            self.label.config(text=result_text)
            self.reset_game()
        else:
            result_text = "Incorrect! Try again."
            self.label.config(text=result_text)

    def reset_game(self):
        # Reset game after a correct guess
        self.number = random.randint(1, 100)
        self.actual_sqrt = math.sqrt(self.number)
        self.number_label.config(text=f"Number: {self.number}")
        
        # Clear previous buttons
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        
        # Create new buttons for next round
        self.create_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = SquareRootGame(root)
    root.mainloop()
