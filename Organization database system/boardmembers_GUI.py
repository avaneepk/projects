from tkinter import *
import psycopg2

def boardmembersopen():
    boardTK = Tk()
    boardTK.title = "board"
    boardTK.geometry("500x650")
    
    conn = psycopg2.connect(   #need to add your own connection here
    host="localhost",
    database="aether",
    user="postgres",
    password="avaneep")
    c = conn.cursor()


    def submit():
        # Insert
        c = conn.cursor()
        c.execute("INSERT INTO board_member(bm_fname,bm_lname,bm_email,bm_degree,bm_role,s_no) VALUES(%s,%s,%s,%s,%s,%s)",
                  (str(board_fname.get()),str(board_lname.get()),str(board_email.get()),str(board_degree.get()),str(board_role.get()), int(board_id.get())))

        conn.commit()

        # clear
        board_fname.delete(0, END)
        board_lname.delete(0, END)
        board_id.delete(0, END)
        board_degree.delete(0, END)
        board_email.delete(0, END)
        board_membership.delete(0, END)
        board_role.delete(0, END)


    def query():
        c = conn.cursor()
        c.execute("SELECT * FROM board_member")
        records = c.fetchall()
        print(records)
        print_records = ''

        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(boardTK, text=print_records)
        query_label.grid(row=13, column=0, columnspan=2)

        conn.commit()
        conn.close()


    def delete():
        c = conn.cursor()
        c.execute("DELETE from board_member WHERE s_no = %s",(delete_box.get(),))
        conn.commit()


    # board boxes
    board_fname = Entry(boardTK, width=30)
    board_fname.grid(row=0, column=1, padx=20)

    board_lname = Entry(boardTK, width=30)
    board_lname.grid(row=1, column=1, padx=20)

    board_id = Entry(boardTK, width=30)
    board_id.grid(row=2, column=1, padx=20)

    board_degree = Entry(boardTK, width=30)
    board_degree.grid(row=3, column=1, padx=20)

    board_email = Entry(boardTK, width=30)
    board_email.grid(row=4, column=1, padx=20)

    board_membership = Entry(boardTK, width=30)
    board_membership.grid(row=5, column=1, padx=20)

    board_role = Entry(boardTK, width=30)
    board_role.grid(row=6, column=1, padx=20)

    delete_box = Entry(boardTK, width=30)
    delete_box.grid(row=9, column=1, padx=20)

    # board labels

    board_fname_label = Label(boardTK, text="Board member first name")
    board_fname_label.grid(row=0, column=0)

    board_lname_label = Label(boardTK, text="Board member last name")
    board_lname_label.grid(row=1, column=0)

    board_id_label = Label(boardTK, text="Board member ID")
    board_id_label.grid(row=2, column=0)

    board_degree_label = Label(boardTK, text="Board member degree")
    board_degree_label.grid(row=3, column=0)

    board_email_label = Label(boardTK, text="Board member email")
    board_email_label.grid(row=4, column=0)

    board_membership_label = Label(boardTK, text="Board member membership")
    board_membership_label.grid(row=5, column=0)

    board_role_label = Label(boardTK, text="Board member role")
    board_role_label.grid(row=6, column=0)

    delete_label = Label(boardTK, text="Row number")
    delete_label.grid(row=9, column=0)

    # submit button
    submit_btn = Button(boardTK, text="Add record to the database", command=submit)
    submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

    # querry button
    querry_button = Button(boardTK, text="Show records", command=query)
    querry_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    # delete button
    delete_button = Button(boardTK, text="Delete record", command=delete)
    delete_button.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=50)

    conn.commit()
    boardTK.mainloop()
