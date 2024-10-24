import tkinter as tk
from tkinter import messagebox

MAX_GOALS = 10
MAX_SCHEMES = 10


class HealthGoal:
    def __init__(self, goal, progress=0):
        self.goal = goal
        self.progress = progress

class GovernmentScheme:
    def __init__(self, name, description, eligibility):
        self.name = name
        self.description = description
        self.eligibility = eligibility


def add_goal():
    goal_text = goal_entry.get().strip()
    if goal_text and len(goals) < MAX_GOALS:
        goals.append(HealthGoal(goal_text))
        update_goal_list()
        messagebox.showinfo("Success", "Goal added: {goal_text}")
    else:
        messagebox.showerror("Error", "Goal cannot be empty or maximum goals reached.")

def track_progress():
    selected_goal = goal_listbox.curselection()
    if selected_goal:
        index = selected_goal[0]
        progress = progress_entry.get().strip()
        if progress.isdigit() and 0 <= int(progress) <= 100:
            goals[index].progress = int(progress)
            update_goal_list()
            messagebox.showinfo("Success", "Progress updated to {progress}%")
        else:
            messagebox.showerror("Error", "Please enter a valid progress (0-100).")
    else:
        messagebox.showerror("Error", "Please select a goal to update progress.")

def update_goal_list():
    goal_listbox.delete(0, tk.END)
    for goal in goals:
        goal_listbox.insert(tk.END, f"{goal.goal}: {goal.progress}%")

def search_scheme():
    keyword = scheme_search_entry.get().strip().lower()
    result_text = ""
    for scheme in schemes:
        if keyword in scheme.name.lower() or keyword in scheme.description.lower():
            result_text += f"Scheme: {scheme.name}\nDescription: {scheme.description}\nEligibility: {scheme.eligibility}\n\n"
    if result_text:
        scheme_result_text.delete(1.0, tk.END)
        scheme_result_text.insert(tk.END, result_text)
    else:
        messagebox.showerror("Error", "No matching schemes found.")


goals = []
schemes = [
    GovernmentScheme("Maternity Benefit Scheme", "Financial support for mothers.", "For expecting mothers."),
    GovernmentScheme("Women Entrepreneurship Program", "Support for women starting a business.", "Women entrepreneurs.")
]


root = tk.Tk()
root.title("Women's Empowerment and Safety App")


tk.Label(root, text="Health Goals").grid(row=0, column=0, pady=10)

goal_entry = tk.Entry(root)
goal_entry.grid(row=1, column=0, padx=10)

tk.Button(root, text="Add Goal", command=add_goal).grid(row=1, column=1)

tk.Label(root, text="Your Goals").grid(row=2, column=0, pady=10)

goal_listbox = tk.Listbox(root, height=5)
goal_listbox.grid(row=3, column=0, columnspan=2, padx=10)

tk.Label(root, text="Progress (%)").grid(row=4, column=0)
progress_entry = tk.Entry(root)
progress_entry.grid(row=4, column=1)

tk.Button(root, text="Update Progress", command=track_progress).grid(row=5, column=0, columnspan=2, pady=10)


tk.Label(root, text="Government Schemes").grid(row=6, column=0, pady=10)

scheme_search_entry = tk.Entry(root)
scheme_search_entry.grid(row=7, column=0, padx=10)

tk.Button(root, text="Search Schemes", command=search_scheme).grid(row=7, column=1)

scheme_result_text = tk.Text(root, height=5, width=50)
scheme_result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()