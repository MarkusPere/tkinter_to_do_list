import tkinter as tk
import functions

window = tk.Tk()
window.title("TaskVault")
window.geometry('500x300')

left_frame = tk.Frame(window, width=200, height=250)
right_frame = tk.Frame(window, width=250, height=250)

left_frame.pack(side=tk.LEFT, padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

description_label = tk.Label(left_frame, text="Description:")
description_label.grid(row=0, column=0, sticky="w")
description_input = tk.Text(left_frame, height=5, width=20)
description_input.grid(row=1, column=0, columnspan=2)

difficulty_label = tk.Label(left_frame, text="Difficulty:")
difficulty_label.grid(row=2, column=0, sticky="w")
difficulty_input = tk.Scale(
    left_frame,
    from_=1,
    to=5,
    orient=tk.HORIZONTAL,
    length=200,
    tickinterval=1,
    resolution=1
)
difficulty_input.grid(row=3, column=0, columnspan=2)

add_button = tk.Button(left_frame, text='Add task', command=lambda: functions.add_task(description_input, difficulty_input, task_text))
add_button.grid(row=4, column=0, columnspan=2)

task_text = tk.Text(right_frame)
task_text.pack()

functions.provide_text(task_text)

window.mainloop()