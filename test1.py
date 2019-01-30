import sqlite3 as lite
import sys

con = None

con = lite.connect('employees.db')
cur = con.cursor()
cur.execute('CREATE TABLE Employees(Id INT, Name TEXT, PER_TYPE TEXT, COMM_STYLE TEXT, EMAIL TEXT)')
cur.execute('INSERT INTO Employees VALUES (1, "Aniya Carter", "ENTJ", "Assertive", "aniyacarter96@yahoo.com")')
cur.execute('INSERT INTO Employees VALUES (2, "Mark Farell", "INTG", "Quiet", "markfarell@email.com")')
cur.execute('INSERT INTO Employees VALUES (3, "Tommy Dinkins", "ISTJ", "Passive", "tommy@tommy.net ")')
cur.execute('INSERT INTO Employees VALUES (4, "Tina Sosa", "ISTP", "Passive-Aggressive", "tina@tina.co")')
cur.execute('INSERT INTO Employees VALUES (5, "A J", "INFJ", "Aggressive", "anemail@fRRRr.him")')

cur.execute('SELECT * FROM Employees')

total = cur.fetchall()
for row in total:
    print(row)

con.close()