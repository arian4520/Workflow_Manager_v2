import tkinter as tk
import webbrowser
import os

# ------------------ Window ---------------------
root = tk.Tk()
root.title("Workflow Launcher")
root.geometry("550x600")
root.config(bg="black")  # dark background

# ------------------ Data -----------------------
workflow = []

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
    except:
        print("No item selected")

def run_workflow():
    for item in workflow:

        # remove unwanted quotes and spaces
        item = item.strip().replace('"', '')

        # If file/app exists → open with OS
        if os.path.exists(item):
            os.startfile(item)

        # Otherwise treat as website
        else:
            if not item.startswith("http"):
                item = "https://" + item
            webbrowser.open(item)

def save_workflow():
    name = name_entry.get()

    if name == "" or name == "Workflow name":
        print("Enter workflow name")
        return

    # save to Desktop (safe location)
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = os.path.join(desktop, name + ".txt")

    with open(filename, "w") as file:
        for item in workflow:
            file.write(item + "\n")

    print("Saved to:", filename)

def load_workflow():
    name = name_entry.get()

    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = os.path.join(desktop, name + ".txt")

    try:
        workflow.clear()
        listbox.delete(0, tk.END)

        with open(filename, "r") as file:
            for line in file:
                item = line.strip()
                workflow.append(item)
                listbox.insert(tk.END, item)

        print("Loaded:", filename)

    except:
        print("File not found")
# ------------------ UI ------------------

# Heading
heading = tk.Label(root, text="Workflow Launcher", bg="black", fg="white", font=("Arial", 20, "bold"))
heading.pack(pady=15)

# Frame for input fields
frame_input = tk.Frame(root, bg="black")
frame_input.pack(pady=10)

# URL/File Entry
entry = tk.Entry(frame_input, width=40, font=("Arial", 12), bg="#515151", fg="white")
entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(frame_input, text="Add URL/File", command=add_url, bg="#276129", fg="white", width=12)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(frame_input, text="Delete Selected", command=delete_selected, bg="#9e2017", fg="white", width=12)
delete_button.grid(row=1, column=1, padx=5, pady=5)

# Workflow Name Entry
name_entry = tk.Entry(root, width=30, font=("Arial", 12), bg="#515151", fg="white")
name_entry.pack(pady=20)
name_entry.insert(0, "Workflow name") # placeholder text

# Listbox to show workflow items
listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12), bg="#515151", fg="white")
listbox.pack()

# Frame for action buttons
frame_buttons = tk.Frame(root, bg="black")
frame_buttons.pack(pady=30)

ok_button = tk.Button(frame_buttons, text="Run Workflow", command=run_workflow, bg="#18507F", fg="white", width=15)
ok_button.grid(row=0, column=0)

save_button = tk.Button(frame_buttons, text="Save Workflow", command=save_workflow, bg="#7E561A", fg="white", width=15)
save_button.grid(row=0, column=1)

load_button = tk.Button(frame_buttons, text="Load Workflow", command=load_workflow, bg="#491153", fg="white", width=15)
load_button.grid(row=0, column=2)

# Run app
root.mainloop()