
#question number one
'''
class vehical:
    def __init__(self,name,max_speed,milage):
        self.max_speed=max_speed
        self.milage=milage
        self.name=name
class bus(vehical):
    
    pass
    
    
    

s1=bus("junaid",240, 5000)
print("vehical name",s1.name,"speed",s1.max_speed,"milage",s1.milage)



'''


'''
class Person:
    
    
    def __init__(self, name, country, dbirth):
        self.name = name
        self.country = country
        self.dbirth = dbirth
    
    def calculate_age(self, today_age):
        print("The name of the person is:", self.name)
        print("The country the person belongs to is:", self.country)
        print("Hey BOY, your age is:", today_age - self.dbirth)

# Collecting data for 4 people
for i in range(4):
    name = input(f"Enter the name of person {i + 1}: ")
    country = input(f"Enter the country of person {i + 1}: ")
    dbirth = int(input(f"Enter the year of birth of person {i + 1}: "))
    today_age = int(input("Enter the current year: "))
    
    person_instance = Person(name, country, dbirth)
    person_instance.calculate_age(today_age)  # Call the calculate_age method

    
    '''
    
class Bank:
    def __init__(self):
        # Dictionary to store customers with account numbers as keys and their balances as values
        self.customers = {}

    def create_account(self, account_number, initial_balance=0):
        # Check if the account number already exists
        if account_number in self.customers:
            print("Account number already exists")
        else:
            # Create a new account with the given initial balance
            self.customers[account_number] = initial_balance
            print("Account created successfully")

    def make_deposit(self, account_number, amount):
        # Check if the account exists
        if account_number in self.customers:
            # Add the deposit amount to the customer's account balance
            self.customers[account_number] += amount
            print("Deposit successfully completed")
        else:
            print("Account does not exist")

    def make_withdrawal(self, account_number, amount):
        # Check if the account exists
        if account_number in self.customers:
            # Check if the balance is sufficient for withdrawal
            if self.customers[account_number] >= amount:
                # Subtract the withdrawal amount from the balance
                self.customers[account_number] -= amount
                print("Withdrawal successfully completed")
            else:
                print("Insufficient balance")
        else:
            print("Account number does not exist")

    def check_balance(self, account_number):
        # Check if the account exists
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist")

# Create an instance of the Bank class
bank1 = Bank()

# Loop to perform operations on the Bank class
while True:
    print("\nChoose an operation:")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        acno = input("Enter the new account number: ")
        initial_balance = float(input("Enter the initial deposit amount: "))
        bank1.create_account(acno, initial_balance)

    elif choice == '2':
        acno = input("Enter the account number: ")
        deposit_amount = float(input("Enter the amount to deposit: "))
        bank1.make_deposit(acno, deposit_amount)

    elif choice == '3':
        acno = input("Enter the account number: ")
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        bank1.make_withdrawal(acno, withdrawal_amount)

    elif choice == '4':
        acno = input("Enter the account number: ")
        bank1.check_balance(acno)

    elif choice == '5':
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice, please select a valid option.")
    
        
    



