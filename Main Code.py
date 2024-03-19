#By:-Disandu Sanhida
#Date:-15/03/2024



import json
#import json module

# Global list to store transactions
transactions = []

#Function defined to load transactions from json file
def load_transactions():
    global transactions#calling the gloabal transactions list
    file_path = "data.json"
    #error handling ifthere isn't exsist a file in the directory
    try:
        with open(file_path, "r") as json_file:
            transactions = json.load(json_file)
    except FileNotFoundError:
        print("File not found. Creating a new file...")
        transactions = []#if file not found,initalize transactions
    #Decode json file if there isn't any data in the file when programme intilizly start
    except json.decoder.JSONDecodeError:
        print()
        transactions = []#if the file not found initalize transactions list as empty
        return
#Function defined to save transactions
def save_transactions():
    #calling the global transaction list in to the function
    global transactions
    #Ask from user to save the enterd data or not
    ans = input("Do You Want To Save Changes(yes/no): ").lower()
    if ans == "yes":
        file_path = "data.json"
        #write user enterd data to the json file
        with open(file_path, "w") as json_file:
            json.dump(transactions, json_file)
            
        print("Changes Saved Successfully...")
    elif ans == "no":
        print("Changes are not stored ")
    else:
        print("Incorrect Input please enter Yes/No")

#defining function add transactions
def add_transaction():
    print("------------------------------Add A Transaction---------------------------------")
    try:
        #prompt user for transaction amount
        amount = float(input("Enter the Transaction Amount:Rs "))
    except ValueError:#Error hadling if users enters strings to the input
        print("Strings are not supported.Enter Integers only")
        return
        #Check if the user's input is eequals to or lesser than 0
    if amount<=0:
        print("Enter a value greater than 0")
        return
    while True:
        #prompt user for tpe of transactions
        trs_type = input("Enter the Transaction Type (Income/Expense): ").lower()
        if trs_type not in ("income", "expense"):
            print("Invalid input. Please enter 'Income' or 'Expense'.")
        else:
            #prompt user for transaction purpose
            purpose = input("Enter the Transaction purpose: ")
            #prompt user for data of transaction
            date =input("Enter the date of Transaction (DD/MM/YY): ")
            #append user enterd data in the main transactions list
            transactions.append([amount, trs_type, purpose, date])
            #calling save transaction function to save the transaction details user enterd
            #save_transactions()
            save_transactions()
            break
    
#defining a function to view transactions
def view_transactions():
    print("------------------------------View Transactions---------------------------------")
    load_transactions()
    #check is there any transactions exsisting
    if not transactions:
        print("Sorry, there aren't any transactions.")
        
    else:
        #iterate through transactions list from starting 1
        for index, trans in enumerate(transactions, start=1):
            print(f"{index} Amount: {trans[0]}, Type: {trans[1]}, Purpose: {trans[2]}, Date: {trans[3]}")



#defining function to update transactions details
def update_transaction():
    load_transactions()
    #load view transaction function to view transactions list
    view_transactions()
    #defining num variable as None
    num=None
    if not transactions:
        print("There aren't any transactions to update.")
    else:
        #prompt user to enter the transaction Number
        try:
          num = int(input("\nEnter the transaction Number: "))
        except ValueError:
           print("Strings are Not Supported,Please Enter a Number to the choice")
           return

        #subtract 1 from user input
        #to select the correct transaction from transaction list
        num=num-1
        #check if user enterd number less than 0 or greater than the length of transaction list
        if num < 0 or num > len(transactions):
            print("Invalid transaction number.")
            return
        #prompt to user what he want to uodate in the transaction    
        field = input("Enter what you want to Update (amount/type/purpose/date): ").lower()
        #if user enters amount
        if field == "amount":
            try:
              #prompt user to enter the new amount
              amount = float(input("Enter the new Transaction Amount: "))
            except ValueError:
              #dispplay user if user enter amount in string
              print("Enter the Amount in Numbers")
              return
            if amount<=0:
              #assign the new amount value to the right place in the list
              print("The value Must Greater than to zero") 
              return 
            else:
              transactions[num][0] = amount
        #if user enters the type
        elif field == "type":
            #prompt user to enter the new transaction type
            trs_type = input("Enter the new Transaction Type (Income/Expense): ").lower()
            #check if user enters is only income or expense
            if trs_type not in ("income", "expense"):
                print("Invalid type. Please enter 'Income' or 'Expense'.")
                return
            #assign user enters value to the to the correct index in the list    
            transactions[num][1] = trs_type
        #if user enters the purpose    
        elif field == "purpose":
            #prompt ehter the transaction purpose
            purpose = input("Enter the new Transaction purpose: ")
            transactions[num][2] = purpose
        #check if user enters the date    
        elif field == "date":
            #prompt enter the new data of transaction
            date = input("Enter the new date of Transaction (DD/MM/YY): ")
            #choose the correct index in the list and assign enterd data in to list
            transactions[num][3] = date
        else:
            print("Invalid field.")
            return
        #calling function save transactions to save the new data
        save_transactions()




#defining function to delete transactions
def delete_transaction():
    load_transactions()
    #call the function view transaction to view the list of transactions exsisting
    view_transactions()
    #assing the value None to the num variable
    num=None
    #display error message if there isn't any transactions in the lust
    if not transactions:
        print("There isn't any Transactions to delete")
    else:
            
        try:
            #prompt user to enter the transactions number to delete
            num = int(input("Enter the Transaction Number to delete: "))
            num=num-1
            #check if user enterd number is less than 0 or greater than the length of the list
            if num < 0 or num >= len(transactions):
            
                print("Invalid transaction number.")
                return
            #deleting the transaction from the corresponds to user enterd numer    
            del transactions[num]
            # calling the save_transaction function
            save_transactions()
        #Error handling if user input strings for the amount    
        except ValueError:
            print("Strings are not Supported,Please Enter a Number")
        
            
#defining the display summary 
def display_summary():
    load_transactions()
    global transactions
    print("------------------------------ Disaplay Summary-------------------------------")
    #initalizing total_incomes
    total_incomes=0
    #Initializing total_expenses
    tot_expenses=0
    #Initializing count_E
    count_E=0
    #Initializing Count_I
    count_I=0
    #Check if there any transactions in the transactions list
    if not transactions:
        print("There aren't any transactions to display Summary.")
    else:    
        #Iterate through out the transactions list
        for i in transactions:
            #cehck if index 1 in the list equals to income
            if i[1]=="income":
                #if it equals to income tot_income adding it into total incomes
               total_incomes=total_incomes+i[0]
               count_I+=1
            #if it equals to expense 
            else:
               #adding the amount into tot_expenses
               tot_expenses=tot_expenses+i[0]  
               count_E+=1 
        #Display use to Total income
        print(f"Your total Income:Rs{total_incomes}") 
        #Display user total expenses
        print(f"Your expenses is:Rs{tot_expenses} ") 
        #Displaying the No of Expenses
        print(f"No of Expenses is: {count_E}")
        #Displaying the No of Incomes
        print(F"No of Incomes is:{count_I}")
        #Display to user the net balance
        print(f"Your netbalance is:Rs{total_incomes-tot_expenses}")             
            


#Defining main menu Function
def main_menu():
    #call function to load transactions
    load_transactions()

    while True:
        #print main menu header
        print("\n-----------------------Personal Finance Tracker---------------------------") 
        #disaplay add transaction as option 01
        print("(1) Add Transaction")
        #disaplay view transaction as 2
        print("(2) View Transactions")
        #display update transactioon as 3
        print("(3) Update Transaction")
        #disaplay delete transaction as option 4
        print("(4) Delete Transaction")
        #display display summary as option 5
        print("(5) Display Summary")
        #display exit as option 6
        print("(6) Exit\n")
        #prompt user to enter the choice
        choice = input("Enter your choice: ")
      

        #call the add transaction function if user enters one
        if choice == '1':
            add_transaction()
        #call the view transaction function if user enters one    
        elif choice == '2':
            view_transactions()
        #call the update transaction function if user enters one
        elif choice == '3':
            update_transaction()
        #call the delete transaction function if user enters one    
        elif choice == '4':
            delete_transaction()
        #call the display function if user enters one    
        elif choice == '5':
            display_summary()
        #if user enters 6 exit from the program   
        elif choice == '6':
            save_transactions()
            print("Data Saved...")
            print("Exiting program...")
           
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
