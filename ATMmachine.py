def Process():
    print("                            WELCOME TO THE ATM MACHINE:)")
    print("                             PLEASE INSERT YOUR CARD!") 
    DailyLimit=20000
    card_inserted = input("Have you inserted your card? (yes/no): ")
    if card_inserted.lower() == "yes":
        print("CARD INSERTED SUCCESSFULLY")

        CurrentBalance=float(input("Enter your current balance: "))
        WithdrawalAmount=float(input("Enter your withdrawal amount: "))
        if WithdrawalAmount>CurrentBalance:
            print("Insufficient balance!")
            quit()
        if WithdrawalAmount>DailyLimit:
            print("Daily withdrawal limit exceeded!")
            quit()
        else:
            confirmation=input("Are you sure you want to withdraw"+ " Rs." +str(WithdrawalAmount)+" (yes/no)?")
            if confirmation=='yes':
                CurrentBalance=CurrentBalance-WithdrawalAmount
                print("A withdrawal of "+"Rs."+ str(WithdrawalAmount) +" has been made!")
                print("Your current balance is: "+str(CurrentBalance))
                return Process()
            else:
                quit()

    else:
        print("You cannot proceed without inserting your card!")
  
Process()       
