budgetDict = [{
    "category": "food", 
    "amount": 0,   
},{
    "category": "cloths", 
    "amount": 0,
},{
    "category": "entertainment", 
    "amount": 0,
}]

class Budget:
    
    def __init__(self):
        pass
    
    def deposit(self):
        print("Budget Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        print("4. exit")
        selectedbudget = int(input("select your budget \n"))
        
        if selectedbudget == 1:
            print("FOOD BALANCE: ",budgetDict[0]["amount"])
            dq = int(input("do you want to deposit to food balance? 1(yes), 2(no) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[0]["amount"] + deposit
                budgetDict[0]["amount"] = budgetDict[0]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[0]["amount"])
                wq = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()
                    
                elif wq == 1:
                    self.transfer()
                
                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day")
                    
            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                
                
                
                                
        elif selectedbudget == 2:
            print("CLOTH BALANCE: ",budgetDict[1]["amount"])
            dq = int(input("do you want to deposit to cloth balance? 1(yes), 2(no) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[1]["amount"] + deposit
                budgetDict[1]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[1]["amount"])
                wq = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()
                    
                elif wq == 1:
                    self.transfer()
                
                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day")
                    

            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                
                
                
        elif selectedbudget == 3:
            print("CLOTH BALANCE: ",budgetDict[2]["amount"])
            dq = int(input("do you want to deposit to cloth balance? 1(yes), 2(no) \n"))
            if dq == 1:
                deposit = int(input("Enter Amount\n"))
                deposit1 = budgetDict[2]["amount"] + deposit
                budgetDict[2]["amount"] = budgetDict[1]["amount"] + deposit
                print("NEW BALANCE: ",budgetDict[2]["amount"])
                wq = int(input("do you want to  1(transfer), 2(withdraw), 3(quit)\n"))
                if wq == 2:
                    self.withdrawfromBudget()
                    
                elif wq == 1:
                    self.transfer()
                
                elif wq == 3:
                    exit()
                else:
                    print("Have a Nice Day")
                    

            else:
                print("invalid Selection\nSELECT A VALID OPTION")
                self.deposit()
                    
        elif selectedbudget == 4:
            print("have a nice day!!!")
            exit()
                    

        else:
            print("Have a Nice Day")
                
                    
    def withdrawfromBudget(self):
        print(budgetDict)
        print("withdraw Options")
        print("1. Food")
        print("2. cloth")
        print("3. entertainment")
        print("4. exit")
        selectedbudgetOption = int(input("select withdraw Options \n"))
        
        if selectedbudgetOption == 1:
            print("FOOD BALANCE: ",budgetDict[0]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[0]["amount"]:
                print("Fnsuficent Funds")
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
            
            else:
                withdraw1 = budgetDict[0]["amount"] - withdraw
                budgetDict[0]["amount"] = budgetDict[0]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("FOOD NEW BALANCE: ",budgetDict[0]["amount"])
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
                
        elif selectedbudgetOption == 2:
            print("CLOTH BALANCE: ",budgetDict[1]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[1]["amount"]:
                print("Fnsuficent Funds")
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
            
            else:
                withdraw1 = budgetDict[1]["amount"] - withdraw
                budgetDict[1]["amount"] = budgetDict[1]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("CLOTH NEW BALANCE: ",budgetDict[1]["amount"])
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
                
        elif selectedbudgetOption == 3:
            print("ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
            withdraw = int(input("Enter Amount You Want To Withdraw\n"))
            if withdraw > budgetDict[2]["amount"]:
                print("Fnsuficent Funds")
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
            
            else:
                withdraw1 = budgetDict[2]["amount"] - withdraw
                budgetDict[2]["amount"] = budgetDict[2]["amount"] - withdraw
                print("Withdrawal Sucessful")
                print("ENTERTAINMENT NEW BALANCE: ",budgetDict[2]["amount"])
                wq = int(input("would you like to return home 1(yes), 2(no)"))
                if wq == 1:
                    self.deposit()
                else:
                    print("have a nice day")
                    exit()
                    
        elif selectedbudgetOption == 4:
            print("have a nice day!!!")
            exit()
            
        else:
            print("invalid Selection\nSELECT A VALID OPTION")
            self.deposit()
            
            
            
    def transfer(self):
        print(budgetDict)
        print("Transfer Options")
        print("1.From  Food")
        print("2.From cloth")
        print("3.From entertainment")
        print("4. exit")
        selectTFoption = int(input("select destination\n"))
        
        if selectTFoption == 1:
            print("FOOD BALANCE: ",budgetDict[0]["amount"])
            tf = int(input("1.(TF to Cloth), 2.(TF to Entertainment)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[0]["amount"]:
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    print("NEW CLOTH BALANCE: ",budgetDict[1]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("have a nice day!!")
                        exit()
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif tf ==2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[0]["amount"]:
                    tfamount1 = budgetDict[0]["amount"] - tfamount
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] - tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("have a nice day!!")
                        exit()
                    
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
        elif selectTFoption ==2:
            print("CLOTH BALANCE: ",budgetDict[1]["amount"])
            tf = int(input("1.(TF to Entertainment), 2.(TF to Food)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    tfamount2 = budgetDict[2]["amount"] + tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW CLOTH BALANCE: ",budgetDict[1]["amount"])
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                        
                    else:
                        print("have a nice day!!")
                        exit()
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif tf ==2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[1]["amount"]:
                    tfamount1 = budgetDict[1]["amount"] - tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] - tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW CLOTH BALANCE: ",budgetDict[1]["amount"])
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("have a nice day!!")
                        exit()
                    
                else:
                    print("insufficent funds")
                    print("CLOTH BALANCE: ",budgetDict[1]["amount"])
                    self.deposit()
                    
        elif selectTFoption ==3:
            print("ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
            tf = int(input("1.(TF to cloth), 2.(TF to Food)\n"))
            if tf == 1:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[2]["amount"]:
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    budgetDict[1]["amount"] = budgetDict[1]["amount"] + tfamount
                    tfamount2 = budgetDict[1]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    print("NEW CLOTH BALANCE: ",budgetDict[1]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("have a nice day!!")
                        exit()
                    
                else:
                    print("insufficent funds")
                    print("FOOD BALANCE: ",budgetDict[0]["amount"])
                    self.deposit()
                    
            elif tf ==2:
                tfamount = int(input("Enter Amount\n"))
                if tfamount <= budgetDict[2]["amount"]:
                    tfamount1 = budgetDict[2]["amount"] - tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    budgetDict[2]["amount"] = budgetDict[2]["amount"] - tfamount
                    budgetDict[0]["amount"] = budgetDict[0]["amount"] + tfamount
                    tfamount2 = budgetDict[0]["amount"] + tfamount
                    print("TF SUCESSFUL!!!")
                    print("NEW ENTERTAINMENT BALANCE: ",budgetDict[2]["amount"])
                    print("NEW FOOD BALANCE: ",budgetDict[0]["amount"])
                    aq = int(input("do you wan to TF again? 1(ye) 2(no)\n"))
                    if aq == 1:
                        self.transfer()
                    else:
                        print("have a nice day!!")
                        exit()
                    
                else:
                    print("insufficent funds")
                    print("CLOTH BALANCE: ",budgetDict[1]["amount"])
                    self.deposit()
                    
        elif selectTFoption ==4:
            print("have a nice day!!!")
            exit()
            
        else:
            print("have a nice day!!!")
          
    
transaction = Budget()       
transaction.deposit()