# Sumbitted by:
# Huzaifa Qureshi
# Rollno:
# F21BSEEN1E02022
# Semester:
# 5th
# Section:
# E1
# Sumbitted by:
# Muhammad Saim Sajid
# Rollno:
# F21BSEEN1E02025
# Semester:
# 5th
# Section:
# E1
# Project:
# Scheme of Study Management In Tkinter
# Sumbitted To:
# Sir Nauman





# To install All The packages just type 

# "pip install -r requirements.txt" 

# in the terminal of vscode or whichever IDE you are Using

import tkinter as tk
import re

class SOSManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scheme Of Study Manager")

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        teacher_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Teacher", menu=teacher_menu)
        teacher_menu.add_command(label="Sir Nauman", command=lambda: self.select_teacher(1))
        teacher_menu.add_command(label="Sir Rafaqat Kazmi", command=lambda: self.select_teacher(2))
        teacher_menu.add_command(label="Ma'am Sunnia", command=lambda: self.select_teacher(3))

        self.semesters = {}

        subject_label = tk.Label(self.root, text="Subject Name:")
        subject_label.grid(row=0, column=0)

        self.subject_entry = tk.Entry(self.root, width=100)
        self.subject_entry.grid(row=0, column=1, columnspan=3)

        course_code_label = tk.Label(self.root, text="Course Code:")
        course_code_label.grid(row=1, column=0)

        self.course_code_entry = tk.Entry(self.root, width=100)
        self.course_code_entry.grid(row=1, column=1, columnspan=3)

        teacher_name_label = tk.Label(self.root, text="Teacher Name:")
        teacher_name_label.grid(row=2, column=0)

        self.teacher_name_entry = tk.Entry(self.root, width=100)
        self.teacher_name_entry.grid(row=2, column=1, columnspan=3)

        description_label = tk.Label(self.root, text="Description:")
        description_label.grid(row=3, column=0)

        self.description_entry = tk.Entry(self.root, width=100)
        self.description_entry.grid(row=3, column=1, columnspan=3)

        add_button = tk.Button(self.root, text="Add", command=self.add_item)
        add_button.grid(row=4, column=0)

        remove_button = tk.Button(self.root, text="Remove", command=self.remove_item)
        remove_button.grid(row=4, column=1)

        edit_button = tk.Button(self.root, text="Edit", command=self.edit_item)
        edit_button.grid(row=4, column=2)

        save_button = tk.Button(self.root, text="Save", command=self.save_sos)
        save_button.grid(row=4, column=3)

        sort_button = tk.Button(self.root, text="Sort", command=self.sort_items)
        sort_button.grid(row=4, column=4)

        self.sos_listbox = tk.Listbox(self.root, width=60)
        self.sos_listbox.grid(row=5, column=0, columnspan=5)

        semester_label = tk.Label(self.root, text="Select Semester:")
        semester_label.grid(row=6, column=0)

        self.selected_semester = tk.StringVar(self.root)
        self.semester_listbox = tk.OptionMenu(self.root, self.selected_semester, *self.get_semester_options())
        self.semester_listbox.grid(row=6, column=1, columnspan=2)

        load_button = tk.Button(self.root, text="Load Subjects", command=self.load_subjects)
        load_button.grid(row=6, column=3, columnspan=2)

        try:
            with open("sos.txt", "r") as f:
                for line in f:
                    self.sos_listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

        self.sos_listbox.bind("<Double-Button-1>", self.edit_item)

        self.get_semester_options()
        self.root.mainloop()

    def get_semester_options(self):
        return [f"Semester {i}" for i in range(1, 9)]

    def add_item(self):
        subject_name = self.subject_entry.get()
        description = self.description_entry.get()
        course_code = self.course_code_entry.get()
        teacher_name = self.teacher_name_entry.get()

        if subject_name and description and course_code and teacher_name:
            selected_semester = self.selected_semester.get()
            if selected_semester:
                course_info = f"{subject_name}: {description} ({course_code}, {teacher_name})"
                self.semesters.setdefault(selected_semester, []).append(course_info)
                self.update_sos_listbox()
                self.save_sos()

            self.subject_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            self.course_code_entry.delete(0, tk.END)
            self.teacher_name_entry.delete(0, tk.END)

    def remove_item(self):
        selected_item = self.sos_listbox.get(tk.ANCHOR)
        if selected_item:
            self.sos_listbox.delete(tk.ANCHOR)
            self.save_sos()

    def edit_item(self):
        selected_item = self.sos_listbox.get(tk.ANCHOR)
        if selected_item:
            subject_name, description, rest_info = selected_item.split(": ", 2)
            course_code, teacher_name = re.search(r'\((.*?)\, (.*?)\)', rest_info).groups()

            self.subject_entry.insert(0, subject_name)
            self.description_entry.insert(0, description)
            self.course_code_entry.insert(0, course_code)
            self.teacher_name_entry.insert(0, teacher_name)

            self.sos_listbox.delete(tk.ANCHOR)

    def save_sos(self):
        sos_items = self.sos_listbox.get(0, tk.END)
        with open("sos.txt", "w") as f:
            for item in sos_items:
                f.write(f"{item}\n")

    def sort_items(self):
        items = self.sos_listbox.get(0, tk.END)
        sorted_items = sorted(items)

        self.sos_listbox.delete(0, tk.END)
        for item in sorted_items:
            self.sos_listbox.insert(tk.END, item)

    def update_sos_listbox(self):
        self.sos_listbox.delete(0, tk.END)
        selected_semester = self.selected_semester.get()
        if selected_semester:
            courses = self.semesters.get(selected_semester, [])
            for course in courses:
                self.sos_listbox.insert(tk.END, course)

    def load_subjects(self):
        selected_semester = self.selected_semester.get()
        if selected_semester:
            self.sos_listbox.delete(0, tk.END)
            courses = self.semesters.get(selected_semester, [])
            for course in courses:
                self.sos_listbox.insert(tk.END, course)

    def select_teacher(self, teacher_number):

        print(f"Selected Teacher {teacher_number}")

 
        self.sos_listbox.delete(0, tk.END)


        if teacher_number == 1:

            self.semesters = {"Semester 1": ["Subject1: Description1 (Code1, Sir Nauman)"],
                          "Semester 2": ["Subject2: Description2 (Code2, Sir Nauman)"]}
        elif teacher_number == 2:

            self.semesters = {"Semester 1": ["Subject3: Description3 (Code3, Sir Rafaqat Kazmi)"],
                          "Semester 2": ["Subject4: Description4 (Code4, Sir Rafaqat Kazmi)"]}
        elif teacher_number == 3:
 
            self.semesters = {"Semester 1": ["Subject5: Description5 (Code5, Ma'am Sunnia)"],
                          "Semester 2": ["Subject6: Description6 (Code6, Ma'am Sunnia)"]}

        self.update_sos_listbox()

if __name__ == "__main__":
    sos_manager = SOSManager()
