import tkinter as tk

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x350")

        self.label = tk.Label(root, text="Enter Password:", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(root, show='*', font=("Helvetica", 14))
        self.password_entry.pack(pady=10)

        self.show_password_var = tk.IntVar()
        self.show_password_check = tk.Checkbutton(root, text="Show Password", variable=self.show_password_var, command=self.toggle_password_visibility, font=("Helvetica", 12))
        self.show_password_check.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Strength", command=self.check_strength, font=("Helvetica", 14))
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def check_strength(self):
        password = self.password_entry.get()
        strength, feedback = self.assess_password_strength(password)
        self.result_label.config(text=f"Strength: {strength}\n{feedback}")

    def assess_password_strength(self, password):
        length_criteria = len(password) >= 8
        upper_criteria = any(char.isupper() for char in password)
        lower_criteria = any(char.islower() for char in password)
        digit_criteria = any(char.isdigit() for char in password)
        special_criteria = any(char in "!@#$%^&*()-_+=<>?:" for char in password)

        strength = "Weak"
        feedback = "Your password should include:"

        criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

        if criteria_met == 5:
            strength = "Very Strong"
            feedback = "Excellent password!"
        elif criteria_met == 4:
            strength = "Strong"
            feedback = "Good job! You can make it even stronger."
        elif criteria_met == 3:
            strength = "Moderate"
            feedback += "\n- Uppercase and lowercase letters\n- Numbers\n- Special characters"
        elif criteria_met == 2:
            feedback += "\n- At least 8 characters\n- Uppercase and lowercase letters\n- Numbers\n- Special characters"
        else:
            feedback += "\n- At least 8 characters\n- Uppercase and lowercase letters\n- Numbers\n- Special characters"

        return strength, feedback

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()
