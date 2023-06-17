import tkinter as tk
from tkinter import ttk
import json
import subprocess

data_file = r'food json.txt'

def start_action():
    print("Start button clicked")
    light_label.config(bg="green")
    status_label.config(text="Turned On")

    # Execute the "FINAL CODE Solution.py" script
    subprocess.Popen(["python", r"FINAL CODE Solution.py"])
    print("hey!")

def stop_action():
    print("Stop button clicked")
    light_label.config(bg="red")
    status_label.config(text="Turned Off")

def load_data():
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def update_table():
    key = key_entry.get()
    value = value_entry.get()

    # Update the table
    table.insert("", tk.END, values=(key, value))

    # Update the data dictionary
    data[key] = value

    # Save the modified data to the JSON file
    with open(data_file, 'w') as file:
        json.dump(data, file)

    # Clear the input fields
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)

def remove_item():
    # Get the selected item
    selected_item = table.selection()
    if selected_item:
        key = str(table.item(selected_item)['values'][0])

        # Remove the item from the table
        table.delete(selected_item)

        # Remove the item from the data dictionary
        if key in data:
            del data[key]

        # Save the modified data to the JSON file
        with open(data_file, 'w') as file:
            json.dump(data, file)

# Create the main Tkinter window
window = tk.Tk()
window.title("Table Example")
window.resizable(False, False)  # Disable window resizing

# Create a frame to hold the start and stop buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create the light indicator
light_label = tk.Label(button_frame, bg="red", width=10, height=2)
light_label.pack(side=tk.LEFT, padx=5)

# Create the status label
status_label = tk.Label(button_frame, text="Turned Off")
status_label.pack(side=tk.LEFT, padx=5)

# Create the start button
start_button = tk.Button(button_frame, text="Start", command=start_action)
start_button.pack(side=tk.LEFT, padx=5)

# Create the stop button
stop_button = tk.Button(button_frame, text="Stop", command=stop_action)
stop_button.pack(side=tk.LEFT, padx=5)

# Create a frame to hold the table
table_frame = tk.Frame(window)
table_frame.pack()

# Create a table using the Treeview widget
table = ttk.Treeview(table_frame, columns=("Key", "Value"), show="headings")
table.column("Key", width=200)  # Increase width for Key column
table.column("Value", width=400)  # Increase width for Value column
table.heading("Key", text="Key")
table.heading("Value", text="Value")
table.pack()

# Load data from the JSON file and populate the table
data = load_data()
for key, value in data.items():
    table.insert("", tk.END, values=(key, value))

# Create a frame to hold the input fields and button
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create the key input field
key_label = tk.Label(input_frame, text="Key:")
key_label.grid(row=0, column=0, padx=5)
key_entry = tk.Entry(input_frame, width=30)  # Increase width for key_entry
key_entry.grid(row=0, column=1, padx=5)

# Create the value input field
value_label = tk.Label(input_frame, text="Value:")
value_label.grid(row=1, column=0, padx=5)
value_entry = tk.Entry(input_frame, width=30)  # Increase width for value_entry
value_entry.grid(row=1, column=1, padx=5)

# Create the update button
update_button = tk.Button(window, text="Update", command=update_table)
update_button.pack(pady=5)

# Create the remove button
remove_button = tk.Button(window, text="Remove", command=remove_item)
remove_button.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()	