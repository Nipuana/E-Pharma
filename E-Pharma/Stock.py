import sqlite3
from tkinter import *

#a function to navigate to UI1
def ui():
    root.destroy()
    import ui1

def update_database_schema():
    # Connect to the database
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()

    # Add a new column 'purpose' to the 'medicines' table
    cursor.execute("ALTER TABLE medicines ADD COLUMN purpose TEXT")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def view_records():
    conn = sqlite3.connect("medicine_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    records = cursor.fetchall()
    conn.close()

    draw_table(records)

def draw_table(records):
    # Clear previous drawings
    canvas.delete("all")

    # Draw horizontal lines
    for i in range(len(records) + 1):
        canvas.create_line(50, 50 + 30 * i, 550, 50 + 30 * i, fill="black")

    # Draw vertical lines
    for x in (50, 250, 400, 550):
        canvas.create_line(x, 50, x, 50 + 30 * len(records), fill="black")

    # Draw headers
    headers = ["Medicine Name", "Quantity", "Expiry Date", "Purpose"]
    for i, header in enumerate(headers):
        canvas.create_text(150 * (i+1), 25, text=header, font=("Arial", 10, "bold"))

    # Draw records
    for i, record in enumerate(records):
        for j, value in enumerate(record[1:]):  # Exclude the ID
            canvas.create_text(150 * (j+1), 50 + 30 * i + 15, text=value)


# Create the main window
root = Tk()
root.config(bg='#C0C0C0')  # Light gray background
root.title("Medicine Database Admin Area")
root.geometry("850x500")
root.resizable(False, False)  # Disable resizing

# Entry fields for adding new records
entry_style = {"font": ("Arial", 12), "bg": '#D3D3D3', "fg": '#333333', "borderwidth": 0}  # Modified entry style

labels = ["Medicine Name", "Quantity", "Expiry Date", "Purpose"]
entries = {}

for i, label in enumerate(labels):
    entry_label = Label(root, text=f"{label}:", font=("Arial", 12), bg='#707070', fg='white')
    entry_label.place(x=180, y=120 + 40 * i)
    entries[label] = Entry(root, **entry_style)
    entries[label].place(x=320, y=120 + 40 * i)

# Listbox to display records with Scrollbar
listbox_frame = Frame(root)
listbox_frame.place(x=550, y=50)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL, width=4)  # Set the width here
listbox = Listbox(listbox_frame, width=40, height=20, bg="#595959", fg="white", selectbackground="#AED6F1", borderwidth=0, yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT, fill=Y)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Canvas for drawing table-like structure
canvas = Canvas(root, width=700, height=500, bg="white")
canvas.place(x=50, y=50)

# Button for going back to the home screen
home_button = Button(root, text="Home",  font=("Arial", 12), bg="#3CB371", fg="white", padx=20,command=ui)
home_button.place(x=750, y=10)

# Directly call view_records to show data immediately
view_records()

# Run the Tkinter event loop
root.mainloop()
