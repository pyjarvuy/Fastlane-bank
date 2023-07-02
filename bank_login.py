import random
import csv
import re
class BankCustomer:
    """
    A class representing a bank customer.
    """
    
    def __init__(self):
        """
        Initializes a new BankCustomer object.
        """
        print("saving account minimum deposit(10,000.00₹), current account minimum deposit(20,000.00₹)")
        self.balance=0
       

        

       
    def new_user(self):
        """
        Handles the new user registration process.
        
        Asks the user whether they are a new user or an existing customer. If they are a new user, it prompts for
        various customer details such as pancard, name, email, address, phone number, etc., and saves them in a CSV file.
        If they are an existing customer, it prompts for their pancard number and displays their details if found.
        """ 
        user=input ("enter you are the new user and existing customer (new/exisiting/withdraw/deposit): ")
        if user.lower()=="new":
            self.customer_pancard() # Prompt for pancard number
            self.customer_name() # Prompt for customer name
            self.customer_mailid() # Prompt for email
            self.customer_address() # Prompt for address
            self.customer_phonenumber()  # Prompt for phone number
            self.customer_custid()  # Generate custid
            self.customer_addharcard() # Prompt for Aadhar card number
            self.customer_zipcode()  # Prompt for zipcode
            self.customer_accounttype() # Prompt for account type
            self.customer_bankdetail() # Set bank details
            self.customer_accountnumber() # Generate account number
            self.customer_deposit() # Prompt for initial deposit
          

       
        

        print("new user registration")
        if user.lower()=="exisiting":
         self.exisiting_customer_login()  # Prompt for existing customer login

        elif user.lower()=="withdraw":
            import withdraw_bank
            withdraw_bank.customerwithdraw
        
        elif user.lower()=="deposit":
           import deposit_bank
           deposit_bank.customerdeposit
             
            

        else:
            print("invalid input. please enter 'new' or 'exisiting'.")

    def exisiting_customer_login(self):
        """
        Handles the existing customer login process.
        
        Prompts the user to enter their pancard number. It checks if the pancard number exists in the CSV file.
        If found, it displays the customer details. If not found, it informs the user that the pancard number is
        not found or the details are incorrect.
        """
        pancard = input("Enter your pancard number: ")
        
        fullpath = pancard + ".csv"
        try:
            with open(fullpath, "r")as file1: 
                reader = csv.reader(file1)
                header = next(reader) 
                
                for row in reader:
                    if row[0] == pancard:
                       
                       print("Login successful!")
                        
                       print("Customer Details:")
                       for i in range(len(header)):
                           print(f"{header[i]}: {row[i]}")
                       break
                else:
                    print("Pancard number not found. Please check your details.")
        except FileNotFoundError:
         print("Pancard number not found. Please check your details.")
          
    


        
        
    def customer_name(self):
        """
        Sets the customer's full name attribute.
        
        Asks the user to enter their first name, middle name, and last name. It saves the full name in the CSV file.
        """
        self.firstname=input("Enter your first name: ")
        self.middlename=input("Enter your middle name: ")
        self.lastname=input("enter your last name: ")

        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(f"{self.firstname} {self.middlename} {self.lastname},")
        print("your full name is",self.firstname,self.middlename,self.lastname)

    
###customer email attribute
    def customer_mailid(self):
        """
        Sets the customer's email attribute.
        
        Asks the user to enter their email address. It saves the email address in the CSV file.
        """
        
        self.email=(input("Enter your mail id: "))
        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(f"{self.email},")
        print("mail id",self.email)

### customer address attribute
    def customer_address(self):
        """
        Sets the customer's address attribute.
        
        Asks the user to enter their permanent address. It saves the address in the CSV file.
        """
        self.address=input("Enter your permanent address: ")

        fullpath=str(self.pancard)+".csv"
        with open(fullpath,"a+")as file1:
         address_list=self.address.split(",")
         for item in address_list:
            file1.write(item+' ')
            
            

        print("your permanent address: ",self.address+"  ")

##customer phone number attribute
    def customer_phonenumber(self):
        """
        Sets the customer's phone number attribute.
        
        Asks the user to enter their phone number. It validates the phone number and saves it in the CSV file.
        """
        while True:
            self.phonenumber=input("Enter your phone number: ")
            if re.match(r'^\d{10}$',self.phonenumber):
             fullpath=str(self.pancard)+".csv"
             with open(fullpath,"a+")as file1:
              file1.write(",")
              file1.write(f"{self.phonenumber},")
              print("phone number:",self.phonenumber)
             break
            else:
             print("Invalid phone number. please enter 10-digit number")
            
        
        

       
    def customer_pancard(self):
        """
        Sets the customer's pancard attribute.
        
        Asks the user to enter their pancard number. It creates a new CSV file with the pancard number as the filename.
        """
        self.pancard=input("Enter your pancard number: ")

        header=["pancard","fullname","email","address","contact","custid","addhar card","zipcode","account type","bank detail","account number","deposit"]
        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+",newline='')
        writer=csv.writer(file1)
        writer.writerow(header)
        
        

        file1.write(f"{self.pancard},")
        

        print("pancard no.: ",self.pancard)

###customer aadhar card attribute
    def customer_addharcard(self): 
      """
        Sets the customer's Aadhar card attribute.
        
        Asks the user to enter their Aadhar card number. It validates the number and saves it in the CSV file.
        """
      while True:
         self.addharcard=(input("Enter your 12 digit addhar number: "))
         if re.match(r'^\d{12}$',self.addharcard):
             fullpath=str(self.pancard)+".csv"
             file1=open(fullpath,"a+")
             file1.write(f"{self.addharcard},")
             print("addhar no.:",self.addharcard)

             break
         else:
          print("Invalid aadhar number. please enter 12-digit number")    

         
## customer zipcode attribute
    def customer_zipcode(self):
        """
        Sets the customer's zipcode attribute.
        
        Asks the user to enter their zip code. It saves the zip code in the CSV file.
        """
        self.zipcode=int(input("enter your zip code: "))

        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(f"{self.zipcode},")
    

        print("zipcode: ",self.zipcode)

#### customer account type attribute        
    def customer_accounttype(self):
        """
        Sets the customer's account type attribute.
        
        Asks the user to choose between saving (1) or current (2) account types. It saves the account type in the CSV file.
        """
        self.accounttype=int(input("choice saving(1) or current(2) account: "))

        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(f"{self.accounttype},")
        

        if self.accounttype==1:
            print("congo your saving account is created")
        elif self.accounttype==2:
            print("congo your current account is created")
        else:
            print("pls select correct bank account")

### cutomer bank detail attribute
    def customer_bankdetail(self):
        """
        Sets the customer's bank detail attribute.
        
        Sets the customer's bank name, branch, and IFSC code. It saves the bank details in the CSV file.
        """
        self.bankdetail={"bankname":"it bank",
                         "branch":"mahim",
                         "ifcs code":"0016"
                         }
        
        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        for key,value in self.bankdetail.items():
            file1.write(f"{key}:{value}' '")
        

        print("bank detail:",self.bankdetail)

###customer account number of 12 digit attribute
    def customer_accountnumber(self):
        """
        Sets the customer's account number attribute.
        
        Generates a random 12-digit account number and saves it in the CSV file.
        """
        self.accountnumber=random.randint(100000000000,999999999999)

        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(",")
        file1.write(f"{self.accountnumber},")
        

        print("your account no.: ",self.accountnumber)
               
###customer custid of 6 digit attribute
    def customer_custid(self):
        """
        Sets the customer's custid attribute.
        
        Generates a random 6-digit custid and saves it in the CSV file.
        """
        self.custid=random.randint(100000,999999)
        fullpath=str(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        
        file1.write(f"{self.custid},")
        print("custid :",self.custid)
    


##customer deposit attribute
    def customer_deposit(self):
        """
        Sets the customer's deposit attribute.
        
        Asks the user to enter the amount they want to deposit. It updates the customer's balance and saves the deposit
        amount in the CSV file.
        """
        self.amount=float(input("Enter your amount : "))
        self.balance+=self.amount

        fullpath=(self.pancard)+".csv"
        file1=open(fullpath,"a+")
        file1.write(f"{self.amount},")
        
        print("amount deposited ",self.amount)
     
    print("  ┌────────────────┐  ")
    print("  │  ╭┼┼╮          │  ")
    print("  │  ╰┼┼╮          │  ")
    print("  │  ╰┼┼╯          │  ")
    print("  │                │  ")
    print("  │ F A S T L A N E│  ")
    print("  │    B A N K     │  ")
    print("  │                │  ")
    print("  │                │  ")
    print("  │                │  ")
    print("  │                │  ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ")
    print("  │ ║│┃┃║║│┃║│║┃│  │  ")
    print("  │                │  ")
    print("  └────────────────┘  ")


### creating object of class
b=BankCustomer()

###calling function with THE class object

b.new_user()

