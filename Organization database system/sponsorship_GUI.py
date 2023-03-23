from tkinter import *
import psycopg2

def sponsoropen():
    sponsorTK = Tk()
    sponsorTK.title = "sponsor"
    sponsorTK.geometry("500x650")

    conn = psycopg2.connect(    #need to add your own connection here
    host="localhost",
    database="aether",
    user="postgres",
    password="avaneep")
    c = conn.cursor()

    def submit():
        # Insert
        c = conn.cursor()
        c.execute("INSERT INTO sponsor(c_name,c_id,c_email,money_amount) VALUES (%s,%s,%s,%s)",
                  (str(company_name.get()),int(company_id.get()),str(company_email.get()),int(money.get())))

        conn.commit()

        # clear
        company_id.delete(0, END)
        company_name.delete(0, END)
        company_email.delete(0, END)
        money.delete(0, END)

    def query():
        c = conn.cursor()
        c.execute("SELECT * FROM sponsor")
        records = c.fetchall()
        print(records)
        print_records = ''

        for record in records:
            print_records += str(record) + "\n"

        query_label = Label(sponsorTK, text=print_records)
        query_label.grid(row=13, column=0, columnspan=2)

        conn.commit()

    def delete():
        c = conn.cursor()
        c.execute("DELETE from sponsor WHERE c_id=%s", ((delete_box.get(),)))
        conn.commit()

    def calculator():
        c = conn.cursor()
        c.execute("SELECT * FROM sponsor")
        prices = c.fetchall()
        sum = 0
        for price in prices:
            sum += int(price[3])

        calculator_label = Label(sponsorTK, text=sum)
        calculator_label.grid(row=12, column=0, columnspan=2)
        print(sum)
        conn.commit()

    # sponsor boxes
    company_id = Entry(sponsorTK, width=30)
    company_id.grid(row=0, column=1, padx=20)

    company_name = Entry(sponsorTK, width=30)
    company_name.grid(row=1, column=1, padx=20)

    company_email = Entry(sponsorTK, width=30)
    company_email.grid(row=2, column=1, padx=20)

    money = Entry(sponsorTK, width=30)
    money.grid(row=3, column=1, padx=20)

    delete_box = Entry(sponsorTK, width=30)
    delete_box.grid(row=9, column=1, padx=20)

    # sponsor labels

    company_id_label = Label(sponsorTK, text="Company ID")
    company_id_label.grid(row=0, column=0)

    compnay_name_label = Label(sponsorTK, text="Company name")
    compnay_name_label.grid(row=1, column=0)

    company_email_label = Label(sponsorTK, text="Company email")
    company_email_label.grid(row=2, column=0)

    money_label = Label(sponsorTK, text="Money")
    money_label.grid(row=3, column=0)

    delete_label = Label(sponsorTK, text="Row number")
    delete_label.grid(row=9, column=0)

    # submit button
    submit_btn = Button(sponsorTK, text="Add record to the database", command=submit)
    submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

    # querry button
    querry_button = Button(sponsorTK, text="Show records", command=query)
    querry_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    # delete button
    delete_button = Button(sponsorTK, text="Delete record", command=delete)
    delete_button.grid(row=10, column=0, columnspan=2, pady=20, padx=10, ipadx=50)

    #calculator
    calculator_button = Button(sponsorTK, text="Calculate the money", command=calculator)
    calculator_button.grid(row=11, column=0, columnspan=2, pady=20, padx=10, ipadx=50)



    conn.commit()
    sponsorTK.mainloop()

