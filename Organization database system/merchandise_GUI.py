from tkinter import *
import psycopg2

def merchanidseopen():
    merchandiseTK = Tk()
    merchandiseTK.title = "merchandise"
    merchandiseTK.geometry("500x650")
    
    conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="aether",
    user="postgres",
    password="avaneep")
    c = conn.cursor()


    def submit():
        # Insert
        c = conn.cursor()
        c.execute("INSERT INTO merchandise(p_no,s_no,p_type,p_price) VALUES (%s,%s,%s,%s)",
                (int(produce_number.get()),int(student_number.get()),str(produce_type.get()),int(produce_price.get())))

        conn.commit()

        # clear
        produce_number.delete(0, END)
        produce_type.delete(0, END)
        produce_price.delete(0, END)
        student_number.delete(0, END)

    def query():
        c = conn.cursor()
        c.execute("SELECT * FROM merchandise")
        records = c.fetchall()
        print(records)
        print_records = ''

        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(merchandiseTK, text=print_records)
        query_label.grid(row=13, column=0, columnspan=2)

        conn.commit()


    def delete():
        c = conn.cursor()
        c.execute("DELETE from merchandise WHERE s_no=%s",(delete_box.get(),))
        conn.commit()

    # merchandise boxes
    produce_number = Entry(merchandiseTK, width=30)
    produce_number.grid(row=0, column=1, padx=20)

    produce_type = Entry(merchandiseTK, width=30)
    produce_type.grid(row=1, column=1, padx=20)

    produce_price = Entry(merchandiseTK, width=30)
    produce_price.grid(row=2, column=1, padx=20)

    student_number = Entry(merchandiseTK, width=30)
    student_number.grid(row=3, column=1, padx=20)

    delete_box = Entry(merchandiseTK, width=30)
    delete_box.grid(row=9, column=1, padx=20)

    # merchandise labels

    produce_number_label = Label(merchandiseTK, text="Produce number")
    produce_number_label.grid(row=0, column=0)

    produce_type_label = Label(merchandiseTK, text="Produce type")
    produce_type_label.grid(row=1, column=0)

    produce_price_label = Label(merchandiseTK, text="Produce price")
    produce_price_label.grid(row=2, column=0)

    student_number_label = Label(merchandiseTK, text="Student number")
    student_number_label.grid(row=3, column=0)

    delete_label = Label(merchandiseTK, text="Row number")
    delete_label.grid(row=9, column=0)

    # submit button
    submit_btn = Button(merchandiseTK, text="Add record to the database", command=submit)
    submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

    # querry button
    querry_button = Button(merchandiseTK, text="Show records", command=query)
    querry_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    # delete button
    delete_button = Button(merchandiseTK, text="Delete record", command=delete)
    delete_button.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=50)


    conn.commit()
    merchandiseTK.mainloop()



