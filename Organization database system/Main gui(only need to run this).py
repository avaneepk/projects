from membership_GUI import *
from boardmembers_GUI import *
from sponsorship_GUI import *
from merchandise_GUI import *
from tkinter import *
import psycopg2

root = Tk()
root.title = "student"
root.geometry("500x650")

conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="aether",
    user="postgres",
    password="avaneep")
c = conn.cursor()


# submit function
def submit():
    # Insert
    c = conn.cursor()
    student_fname_e= str(student_fname.get())
    student_lname_e= str(student_lname.get()),
    student_id_e= int(student_id.get())
    student_degree_e=str(student_degree.get())
    student_email_e=str(student_email.get())
    student_membership_e=int(student_membership.get())
    c.execute("INSERT INTO student(s_fname,s_lname,m_no,s_no,s_degree,s_email) VALUES (%s,%s,%s,%s,%s,%s)",
              (student_fname_e,student_lname_e,student_membership_e,student_id_e,student_degree_e,student_email_e))

    conn.commit()

    # clear
    student_fname.delete(0, END)
    student_lname.delete(0, END)
    student_membership.delete(0, END)
    student_id.delete(0, END)
    student_degree.delete(0, END)
    student_email.delete(0, END)



# delete function
def delete():
    record_id=(delete_box.get())
    c = conn.cursor()
    c.execute("DELETE FROM student WHERE s_no =%s", (delete_box.get(),))
    conn.commit()


# query function
def query():
    c = conn.cursor()
    c.execute("SELECT * FROM student")
    records = c.fetchall()
    print(records)
    print_records = ''

    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()



# update command for button
def updatecommand():
    c = conn.cursor()
    record_id = delete_box.get()
    
    student_fname_editor_e=str(student_fname_editor.get())
    student_lname_editor_e=str(student_lname_editor.get())
    student_id_editor_e=int(student_id_editor.get())
    student_degree_editor_e=str(student_degree_editor.get())
    student_email_editor_e=str(student_email_editor.get())
    student_membership_editor_e=int(student_membership_editor.get())

    c.execute("UPDATE student SET s_fname=%s,s_lname=%s,m_no=%s,s_no=%s,s_degree=%s,s_email=%s WHERE s_no=%s",
              (student_fname_editor_e,student_lname_editor_e,student_membership_editor_e,student_id_editor_e,student_degree_editor_e,student_email_editor_e,record_id))


    edit.destroy()
    conn.commit()


# update function
def update():
    global edit
    edit = Tk()
    edit.title = "Student update"
    edit.geometry("400x400")
    record_id =(delete_box.get())

    c.execute("SELECT * FROM student where s_no = %s", (record_id,))
    records = c.fetchall()

    # global variables
    global student_fname_editor
    global student_lname_editor
    global student_membership_editor
    global student_id_editor
    global student_degree_editor
    global student_email_editor

    # boxes
    student_fname_editor = Entry(edit, width=30)
    student_fname_editor.grid(row=0, column=1, padx=20)

    student_lname_editor = Entry(edit, width=30)
    student_lname_editor.grid(row=1, column=1, padx=20)

    student_id_editor = Entry(edit, width=30)
    student_id_editor.grid(row=3, column=1, padx=20)

    student_degree_editor = Entry(edit, width=30)
    student_degree_editor.grid(row=4, column=1, padx=20)

    student_email_editor = Entry(edit, width=30)
    student_email_editor.grid(row=5, column=1, padx=20)

    student_membership_editor = Entry(edit, width=30)
    student_membership_editor.grid(row=2, column=1, padx=20)

    # Labels
    student_fname_label_editor = Label(edit, text="First name")
    student_fname_label_editor.grid(row=0, column=0)

    student_lname_label_editor = Label(edit, text="Last name")
    student_lname_label_editor.grid(row=1, column=0)

    student_id_label_editor = Label(edit, text="ID")
    student_id_label_editor.grid(row=3, column=0)

    student_degree_label_editor = Label(edit, text="Degree")
    student_degree_label_editor.grid(row=4, column=0)

    student_email_label_editor = Label(edit, text="Email")
    student_email_label_editor.grid(row=5, column=0)

    student_membership_label_editor = Label(edit, text="Membership")
    student_membership_label_editor.grid(row=2, column=0)

    for record in records:
        student_fname_editor.insert(0, record[0])
        student_lname_editor.insert(0, record[1])
        student_id_editor.insert(0, record[3])
        student_degree_editor.insert(0, record[4])
        student_email_editor.insert(0, record[5])
        student_membership_editor.insert(0, record[2])

    # save button
    save_button = Button(edit, text="Save record", command=updatecommand)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=50)


# Student boxes ( option 1 )
student_fname = Entry(root, width=30)
student_fname.grid(row=0, column=1, padx=20)

student_lname = Entry(root, width=30)
student_lname.grid(row=1, column=1, padx=20)

student_id = Entry(root, width=30)
student_id.grid(row=3, column=1, padx=20)

student_degree = Entry(root, width=30)
student_degree.grid(row=4, column=1, padx=20)

student_email = Entry(root, width=30)
student_email.grid(row=5, column=1, padx=20)

student_membership = Entry(root, width=30)
student_membership.grid(row=2, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20)


#Student labels ( option 1 )
student_fname_label = Label(root, text="Student first name")
student_fname_label.grid(row=0, column=0)

student_lname_label = Label(root, text="Student last name")
student_lname_label.grid(row=1, column=0)

student_id_label = Label(root, text="Student ID")
student_id_label.grid(row=3, column=0)

student_degree_label = Label(root, text="Student degree")
student_degree_label.grid(row=4, column=0)

student_email_label = Label(root, text="Student email")
student_email_label.grid(row=5, column=0)

student_membership_label = Label(root, text="Student membership")
student_membership_label.grid(row=2, column=0)

delete_label = Label(root, text="Row Number")
delete_label.grid(row=9, column=0)


# submit button students

submit_btn = Button(root, text="Add record to the database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

# Querry button students
querry_button = Button(root, text="Show records", command=query)
querry_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

# Delete button students
delete_button = Button(root, text="Delete record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=50)

# Update button students
update_button = Button(root, text="Update record", command=update)
update_button.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=50)

#open membership screen
membership_button = Button(root, text="Membership", command=membershipopen)
membership_button.grid(row=14, column=0, columnspan=2, pady=5, padx=10, ipadx=50)

#open board members screen
boardmembers_button = Button(root, text="Board members", command= boardmembersopen)
boardmembers_button.grid(row=15, column=0, columnspan=2, pady=5, padx=10, ipadx=50)


#open sponsorship screen

sponsorship_button = Button(root, text="Sponsors", command= sponsoropen)
sponsorship_button.grid(row=16, column=0, columnspan=2, pady=5, padx=10, ipadx=50)

#open merchandise screen

merchandise_button = Button(root, text="Merchandise", command= merchanidseopen)
merchandise_button.grid(row=17, column=0, columnspan=2, pady=5, padx=10, ipadx=50)

conn.commit()
root.mainloop()
