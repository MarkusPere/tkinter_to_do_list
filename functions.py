import tkinter as tk

def add_task(description_input, difficulty_input, task_text):
    description = description_input.get("1.0", tk.END).strip()
    difficulty = difficulty_input.get()

    with open('ulesanded.txt', 'a') as fail:
        fail.write(f'Description: {description}, Difficulty: {difficulty}\n')
    
    with open('ulesanded.txt', 'r') as fail:
        lines = fail.readlines()
        if lines:
            last_task = lines[-1]
            task_text.insert(tk.END, last_task)
    
    description_input.delete("1.0", tk.END)

def provide_text(task_text):
    task_text.delete(1.0, tk.END)
    with open('ulesanded.txt', 'r') as fail:
        for task in fail:
            task_text.insert(tk.END, task)