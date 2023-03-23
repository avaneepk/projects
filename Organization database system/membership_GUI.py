from tkinter import *
import psycopg2

def membershipopen():
    membershipTK = Tk()
    membershipTK.title = "membership"
    membershipTK.geometry("500x650")
    
    conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="aether",
    user="postgres",
    password="avaneep")
    c = conn.cursor()

    def submit():
        # Insert
        student_membership_id_e=int(student_membership_id.get())
        membership_number_e=int(membership_number.get()),
        membership_price_e=int(membership_price.get())
        membership_date_e=str(membership_date.get())

        c = conn.cursor()
        c.execute("INSERT INTO membership(m_price,exp_date,s_no,m_no) VALUES (%s,%s,%s,%s)", (membership_price_e,membership_date_e,student_membership_id_e,membership_number_e,))

        conn.commit()

        # clear
        student_membership_id.delete(0, END)
        membership_number.delete(0, END)
        membership_price.delete(0, END)
        membership_date.delete(0, END)


    def query():
        conn = psycopg2.connect(
        host="localhost",
        database="aether",
        user="postgres",
        password="avaneep")
        c = conn.cursor()
        c.execute("SELECT * FROM membership")
        records = c.fetchall()
        print(records)
        print_records = ''

        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(membershipTK, text=print_records)
        query_label.grid(row=13, column=0, columnspan=2)

        conn.commit()


    def delete():
        c = conn.cursor()
        c.execute("DELETE from membership WHERE m_no =%s", (delete_box.get(),))
        conn.commit()


    # membership boxes
    student_membership_id = Entry(membershipTK, width=30)
    student_membership_id.grid(row=0, column=1, padx=20)

    membership_number = Entry(membershipTK, width=30)
    membership_number.grid(row=1, column=1, padx=20)

    membership_price = Entry(membershipTK, width=30)
    membership_price.grid(row=2, column=1, padx=20)

    membership_date = Entry(membershipTK, width=30)
    membership_date.grid(row=3, column=1, padx=20)

    delete_box = Entry(membershipTK, width=30)
    delete_box.grid(row=9, column=1, padx=20)

    # membership labels

    student_membership_id_label = Label(membershipTK, text="Membership ID")
    student_membership_id_label.grid(row=0, column=0)

    membership_number_label = Label(membershipTK, text="Membership number")
    membership_number_label.grid(row=1, column=0)

    membership_price_label = Label(membershipTK, text="Membership price")
    membership_price_label.grid(row=2, column=0)

    membership_date_label = Label(membershipTK, text="Membership date")
    membership_date_label.grid(row=3, column=0)

    delete_label = Label(membershipTK, text="Row Number")
    delete_label.grid(row=9, column=0)

    # submit button
    submit_btn = Button(membershipTK, text="Add record to the database", command=submit)
    submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

    # querry button
    querry_button = Button(membershipTK, text="Show records", command=query)
    querry_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    # delete button
    delete_button = Button(membershipTK, text="Delete record", command=delete)
    delete_button.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=50)

    conn.commit()
    membershipTK.mainloop()
