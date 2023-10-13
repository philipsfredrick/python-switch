import tkinter as tk
import pyodbc
import tkinter.messagebox

conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230601-1355\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

cur = conn.cursor()

window = tk.Tk()
window.title("Student Records")
window.geometry('500x300')

def inserts():
        s_name = s_name_entry.get()
        s_course_code = s_course_code_entry.get()
        s_mark = s_mark_entry.get()
        try:
            s_grade, s_employment_status = check_mark(int(s_mark))

            cur.execute('INSERT INTO Training.dbo.StudentDetail VALUES (?,?,?,?,?)',
                         (s_name, s_course_code, s_mark, s_grade, s_employment_status))

            tkinter.messagebox.showinfo('Success', 'Record inserted successfully')

            s_name_entry.delete(0, tk.END)
            s_course_code_entry.delete(0, tk.END)
            s_mark_entry.delete(0, tk.END)

            conn.commit()
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
                tkinter.messagebox.showerror('Database Error','Record not saved')
        finally:
            if conn:
                conn.close()

def update():
    s_no=s_no_update_entry.get()
    s_name = s_name_update_entry.get()
    s_course_code = s_course_code_update_entry.get()
    s_mark = s_mark_update_entry.get()
    try:
        s_grade, s_employment_status = check_mark(int(s_mark))
        s_no=(int(s_no))
        print("Before execute")

        cur.execute('UPDATE Training.dbo.StudentDetail SET s_name=?,s_course_code=?, s_mark=?,s_grade=?, s_employement_status=? WHERE s_no=?',
                    (s_name, s_course_code, s_mark, s_grade, s_employment_status, s_no))

        print("After execute")
        tkinter.messagebox.showinfo('Success', 'Record successfully updated')

        s_name_update_entry.delete(0, tk.END)
        s_course_code_update_entry.delete(0, tk.END)
        s_mark_update_entry.delete(0, tk.END)
        s_no_update_entry.delete(0,tk.END)

        conn.commit()
    except pyodbc.Error as e:
        if conn:
            conn.rollback()
            tkinter.messagebox.showerror('Database Error',str(e))
    finally:
        if conn:
            conn.close()

def show_all_record():
    
    try:
        cur.execute("SELECT * FROM Training.dbo.StudentDetail")
        records = cur.fetchall()
        text_widget = tk.Text(window)
        text_widget.grid(row=0, column=0, padx=10, pady=10)

        for record in records:
            text_widget.insert(tk.END, f"Name: {record[0]}\n")
            text_widget.insert(tk.END, f"Course Code: {record[1]}\n")
            text_widget.insert(tk.END, f"Mark: {record[2]}\n")
            text_widget.insert(tk.END, f"Grade: {record[3]}\n")
            text_widget.insert(tk.END, f"Employment Status: {record[4]}\n")
            text_widget.insert(tk.END, "-----------------------------------\n")

    except pyodbc.Error as e:
         if conn:
            conn.rollback()
            tkinter.messagebox.showerror('Database Error','Error in connection')
            
    finally:
        if conn:
            conn.close()
    pass

def delete():
    s_no=s_no_delete_entry.get()
    try:
        cur.execute('DELETE FROM Training.dbo.StudentDetail WHERE s_no=?',
                    (s_no))

        tkinter.messagebox.showinfo('Success', 'Record deleted successfully')

        s_no_delete_entry.delete(0,tk.END)

        conn.commit()
    except pyodbc.Error as e:
        if conn:
            conn.rollback()
            tkinter.messagebox.showerror('Database Error','Record not deleted')
    finally:
        if conn:
            conn.close()
    pass

def check_mark(s_mark):
    if s_mark in range(75,101):
        s_grade = "A"
        s_employment_status = "automatic employment"
    elif s_mark in range(65,75):
        s_grade = "B"
        s_employment_status = "open to work"
    elif s_mark in range(55,65):
        s_grade = "C"
        s_employment_status = "open to work"    
    elif s_mark in range(0,55):
        s_grade = "F"
        s_employment_status = "probation"
    else:
        tkinter.messagebox.showerror('title','Invalid score')
    return s_grade,s_employment_status

def insert_record():
    insert_window = tk.Toplevel(window)
    insert_window.title("Insert record")
    insert_window.geometry('500x300')
    global s_name_entry, s_course_code_entry, s_mark_entry
  
    s_name_label = tk.Label(insert_window, text="Student Name:", font=("Arial", 14))
    s_name_entry = tk.Entry(insert_window, font=("Arial", 14))
    s_name_label.pack()
    s_name_entry.pack()

    s_course_code_label = tk.Label(insert_window, text="Course Code:", font=("Arial", 14))
    s_course_code_entry = tk.Entry(insert_window, font=("Arial", 14))
    s_course_code_label.pack()
    s_course_code_entry.pack()

    s_mark_label = tk.Label(insert_window, text="Mark:", font=("Arial", 14))
    s_mark_entry = tk.Entry(insert_window, font=("Arial", 14))
    s_mark_label.pack()
    s_mark_entry.pack()

    insert_button = tk.Button(insert_window, text='Save', command=inserts)
    insert_button.configure(background='green')
    insert_button.pack()

def delete_record():
    delete_window = tk.Toplevel(window)
    delete_window.title("Delete record")
    delete_window.geometry('500x300')

    global s_no_delete_entry

    s_no_delete_label = tk.Label(delete_window, text="Student Id:", font=("Arial", 14))
    s_no_delete_entry = tk.Entry(delete_window, font=("Arial", 14))
    s_no_delete_label.pack()
    s_no_delete_entry.pack()

    delete_button = tk.Button(delete_window, text='Delete', command=delete)
    delete_button.configure(background='red')
    delete_button.pack()

def update_record():
    update_window = tk.Toplevel(window)
    update_window.title("Update record")
    update_window.geometry('500x300')

    global s_no_update_entry,s_name_update_entry, s_course_code_update_entry, s_mark_update_entry

    s_no_update_label = tk.Label(update_window, text="Student Id:", font=("Arial", 14))
    s_no_update_entry = tk.Entry(update_window, font=("Arial", 14))
    s_no_update_label.pack()
    s_no_update_entry.pack()

    
    s_name_update_label = tk.Label(update_window, text="Student Name:", font=("Arial", 14))
    s_name_update_entry = tk.Entry(update_window, font=("Arial", 14))
    s_name_update_label.pack()
    s_name_update_entry.pack()

    s_course_code_update_label = tk.Label(update_window, text="Course Code:", font=("Arial", 14))
    s_course_code_update_entry = tk.Entry(update_window, font=("Arial", 14))
    s_course_code_update_label.pack()
    s_course_code_update_entry.pack()

    s_mark_update_label = tk.Label(update_window, text="Mark:", font=("Arial", 14))
    s_mark_update_entry = tk.Entry(update_window, font=("Arial", 14))
    s_mark_update_label.pack()
    s_mark_update_entry.pack()

    update_button = tk.Button(update_window, text='Update', command=update)
    update_button.configure(background='blue')
    update_button.pack()
    
def homepage():

    insertion_button = tk.Button(window, text='Insert record', command=insert_record)
    insertion_button.grid(row=0, column=0, padx=10, pady=10)
    insertion_button.configure(background='green')

    update_button = tk.Button(window, text='Update a record', command=update_record)
    update_button.grid(row=0, column=1, padx=10, pady=10)
    update_button.configure(background='yellow')

    show_all_button = tk.Button(window, text='Show all records', command=show_all_record)
    show_all_button.grid(row=0, column=2, padx=10, pady=10)
    show_all_button.configure(background='blue')

    delete_button = tk.Button(window, text='Delete a record', command=delete_record)
    delete_button.grid(row=0, column=3, padx=10, pady=10)
    delete_button.configure(background='red')


homepage()
window.mainloop()