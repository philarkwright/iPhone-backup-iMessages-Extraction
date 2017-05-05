from prettytable import PrettyTable
import sqlite3

conn = sqlite3.connect('3d0d7e5fb2ce288813306e4d4636395e047a3d28')
c = conn.cursor()

def tablename():
	x = PrettyTable(["Table name"])
	x.align = "l"
	for row in c.execute("SELECT  name  FROM  sqlite_master  WHERE  type='table'"):
		x.add_row(row)
	print x

def messages():
	x = PrettyTable(["Account", "Message"])
	x.align = "l"
	for row in c.execute("SELECT  account, text  FROM  message"):
			x.add_row(row)
	print x


## Text menu in Python
      
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Show Tables"
    print "2. Show Messages"
    print "3. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-3]: ")
    if choice==1:     
        tablename()
    elif choice==2:
    	messages()
    elif choice==3:
        print "Exiting...."
        loop=False 
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
