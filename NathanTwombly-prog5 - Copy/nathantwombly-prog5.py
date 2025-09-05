# Nathan Twombly program 5

import sqlite3


def displayAllTickets(cur):
    
    sql = "SELECT * FROM tickets"
    cur.execute(sql)

    results = cur.fetchall()

    if results:
        print("%-6s %-15s %8s %5s %7s" % ('ticketID', 'Posted MPH', 'MPH Over', 'Age', 'Violator Sex'))

        for row in results:
            tid, actual_speed, posted_speed, age, violator_sex = row
            print("%-6s %-15s %8s %5s %7s" % (tid, actual_speed, posted_speed, age, violator_sex))

        print()
    else:
        print("No data found")

    print()

def addTicket(cur, conn):
    
    actual_speed = int(input('Speed of vehicle: '))
    posted_speed = int(input('Speed limit in area: '))
    age = int(input('Age of driver: '))
    violator_sex = input('Sex of driver: ')
    

    data = (None, actual_speed, posted_speed, age, violator_sex)
    sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?)"

    cur.execute(sql, data)

    conn.commit()
                       


def filterTickets(cur):

    exc = input("Enter 'Male' for Male, and 'Female' for female filter: ")
    if exc != "Male":
        exc = "Female"

    try:

        sql = "SELECT * FROM tickets WHERE violator_sex = ?"

        cur.execute(sql, (exc,))
        results = cur.fetchall()

        if results:
            print("%-6s %-18s %-8s %5s %7s" % ('ticketID', 'Posted MPH', 'MPH Over', 'Age', 'Violator Sex'))

        for row in results:
            tid, actual_speed, posted_speed, age, violator_sex = row
            print("%-6s %-18s %-8s %5s %7s" % (tid, actual_speed, posted_speed, age, violator_sex))

        print()

    except sqlite3.Error as error:
        print(str(error), 'Error occured')
        print("No data found...")


def main():
    conn = sqlite3.connect('tickets5.db')
    cur = conn.cursor()

    while True:
        print("""
            Menu options. Choose 1, 2, 3, or 4
            1. Display all Tickets
            2. Add a Ticket
            3. Filter by Offender Sex
            4. Save & Exit

        """)

        opt = input("Enter your choice, 1, 2, 3, or 4: ")

        if opt == "1":
            displayAllTickets(cur)

        elif opt == "2":
            addTicket(cur, conn)

        elif opt == "3":
            filterTickets(cur)

        elif opt == "4":
            print()
            print("goodbye")

            if conn:
                conn.close
            break

        else:
            print("Invalid entry, enter your choice again.")




main()







