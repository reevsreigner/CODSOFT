import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        # Label and Entry field for password length
        self.length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to generate password
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12))
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label to display generated password
        self.password_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            
            # Define character sets for different complexities
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            symbols = string.punctuation

            # Combine character sets based on user choice for complexity
            complexity = [lowercase, uppercase, digits, symbols]

            password = ""
            for _ in range(length):
                character_set = random.choice(complexity)
                password += random.choice(character_set)

            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as ve:
            self.password_label.config(text=str(ve))
        except Exception as e:
            self.password_label.config(text=f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
