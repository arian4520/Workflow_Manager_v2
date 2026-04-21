import tkinter as tk
import webbrowser
import os

# ------------------ Window ---------------------
root = tk.Tk()
root.title("Workflow Launcher")
root.geometry("700x700")
root.config(bg="black")

# ------------------ Data -----------------------
workflow = []

# ------------------ Helper ---------------------
def get_script_folder():
    return os.path.dirname(os.path.abspath(__file__))

# ------------------ FUNCTIONS ------------------

def add_url():
    text = entry.get()
    if text != "":
        workflow.append(text)
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def delete_selected():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        workflow.pop(index)
    except IndexError:
        print("No item selected")

def run_workflow():
    for item in workflow:
        item = item.strip().replace('"', '')

        if os.path.exists(item):
            os.startfile(item)   # Windows only
        else:
            if not item.startswith("http"):
                item = "https://" + item
            webbrowser.open(item)

def save_workflow():
    name = name_entry.get()

    if name == "" or name == "Workflow name":
        print("Enter workflow name")
        return

    try:
        folder = get_script_folder()
        filename = os.path.join(folder, name + ".txt")

        with open(filename, "w") as file:
            for item in workflow:
                file.write(item + "\n")

        print("Saved to:", filename)

    except Exception as e:
        print("Error:", e)

def load_workflow():
    name = name_entry.get()

    try:
        folder = get_script_folder()
        filename = os.path.join(folder, name + ".txt")

        workflow.clear()
        listbox.delete(0, tk.END)

        with open(filename, "r") as file:
            for line in file:
                item = line.strip()
                workflow.append(item)
                listbox.insert(tk.END, item)

        print("Loaded:", filename)

    except Exception as e:
        print("Error:", e)

# ------------------ UI ------------------

heading = tk.Label(root, text="Workflow Launcher",
                   bg="black", fg="white",
                   font=("Arial", 20, "bold"))
heading.pack(pady=15)

frame_input = tk.Frame(root, bg="black")
frame_input.pack(pady=10)

entry = tk.Entry(frame_input, width=40, font=("Arial", 12),
                 bg="#515151", fg="white")
entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(frame_input, text="Add URL/File",
                       command=add_url, bg="#276129",
                       fg="white", width=12)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(frame_input, text="Delete Selected",
                          command=delete_selected, bg="#9e2017",
                          fg="white", width=12)
delete_button.grid(row=1, column=1, padx=5, pady=5)

name_entry = tk.Entry(root, width=30, font=("Arial", 12),
                      bg="#515151", fg="white")
name_entry.pack(pady=20)
name_entry.insert(0, "Workflow name")

listbox = tk.Listbox(root, width=60, height=15,
                     font=("Arial", 12),
                     bg="#515151", fg="white")
listbox.pack()

frame_buttons = tk.Frame(root, bg="black")
frame_buttons.pack(pady=30)

ok_button = tk.Button(frame_buttons, text="Run Workflow",
                      command=run_workflow, bg="#18507F",
                      fg="white", width=15)
ok_button.grid(row=0, column=0)

save_button = tk.Button(frame_buttons, text="Save Workflow",
                        command=save_workflow, bg="#7E561A",
                        fg="white", width=15)
save_button.grid(row=0, column=1)

load_button = tk.Button(frame_buttons, text="Load Workflow",
                        command=load_workflow, bg="#491153",
                        fg="white", width=15)
load_button.grid(row=0, column=2)

# ------------------ Run ------------------
root.mainloop()