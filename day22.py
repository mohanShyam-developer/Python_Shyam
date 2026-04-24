##'''print(len("Python"))
##print(len((1,2,3)))
##print(len([1,2,3]))
##'''
##import pyttsx3 
##
##engine=pyttsx3.init()
##
##def speak(text):
##    print(text)
##    engine.say(text)
##    engine.runAndWait()
##
##class Parents:
##    def sound(self):
##        print("waste fellow")
##
##class Dad:
##    def sound(self):
##        print("poramboka")
##
##
##class Mummy:
##    def sound(self):
##        print("bewarse yedava")
##
##a= Parents()
##b= Dad()
##c= Mummy()
##
##a.sound()
##
##
##'''class Calculator:
##    def add(self,a,b=0,c=0):
##        return a+b+c
##    
##Calc=Calculator()
##print(Calc.add(2))
##print(Calc.add(3,4))
##print(Calc.add(5,5,5))'''
##
##
##
### MULTI-BANK ATM MACHINE PROGRAM
##
##'''print("====================================")
##print("       WELCOME TO ATM MACHINE       ")
##print("====================================")
##
### Store all accounts
##accounts = {}
##
### Bank list
##banks = ["Canara Bank", "SBI", "ICICI Bank", "Union Bank"]
##
##while True:
##
##    print("\n===== MAIN MENU =====")
##    print("1. Create Account")
##    print("2. Login Account")
##    print("3. Exit")
##
##    main_choice = input("Enter your choice: ")
##
##    # CREATE ACCOUNT
##    if main_choice == "1":
##
##        print("\n===== SELECT BANK =====")
##        for i in range(len(banks)):
##            print(i+1, ".", banks[i])
##
##        bank_choice = int(input("Choose bank number: "))
##
##        if bank_choice < 1 or bank_choice > len(banks):
##            print("Invalid bank choice.")
##            continue
##
##        selected_bank = banks[bank_choice - 1]
##
##        print("\n===== CREATE ACCOUNT =====")
##
##        acc_number = input("Enter Account Number: ")
##
##        if acc_number in accounts:
##            print("Account already exists.")
##            continue
##
##        name = input("Enter Your Name: ")
##        pin = input("Create 4-digit PIN: ")
##
##        accounts[acc_number] = {
##            "name": name,
##            "pin": pin,
##            "balance": 0,
##            "bank": selected_bank,
##            "transactions": []
##        }
##
##        print("Account created successfully in", selected_bank)
##
##    # LOGIN ACCOUNT
##    elif main_choice == "2":
##
##        print("\n===== LOGIN ACCOUNT =====")
##
##        acc_number = input("Enter Account Number: ")
##        pin = input("Enter PIN: ")
##
##        if acc_number in accounts and accounts[acc_number]["pin"] == pin:
##
##            print("\nLogin Successful!")
##            print("Welcome", accounts[acc_number]["name"])
##            print("Bank:", accounts[acc_number]["bank"])
##
##            while True:
##
##                print("\n===== ATM MENU =====")
##                print("1. Check Balance")
##                print("2. Deposit Money")
##                print("3. Withdraw Money")
##                print("4. Change PIN")
##                print("5. Mini Statement")
##                print("6. Logout")
##
##                choice = input("Enter your choice: ")
##
##                # CHECK BALANCE
##                if choice == "1":
##                    print("Balance:", accounts[acc_number]["balance"])
##
##                # DEPOSIT
##                elif choice == "2":
##                    amount = float(input("Enter amount to deposit: "))
##                    accounts[acc_number]["balance"] += amount
##
##                    accounts[acc_number]["transactions"].append(
##                        "Deposited: " + str(amount)
##                    )
##
##                    print("Deposit Successful.")
##
##                # WITHDRAW
##                elif choice == "3":
##                    amount = float(input("Enter amount to withdraw: "))
##
##                    if amount > accounts[acc_number]["balance"]:
##                        print("Insufficient Balance.")
##                    else:
##                        accounts[acc_number]["balance"] -= amount
##
##                        accounts[acc_number]["transactions"].append(
##                            "Withdrawn: " + str(amount)
##                        )
##
##                        print("Please collect your cash.")
##
##                # CHANGE PIN
##                elif choice == "4":
##                    old_pin = input("Enter old PIN: ")
##
##                    if old_pin == accounts[acc_number]["pin"]:
##                        new_pin = input("Enter new PIN: ")
##                        accounts[acc_number]["pin"] = new_pin
##                        print("PIN changed successfully.")
##                    else:
##                        print("Incorrect old PIN.")
##
##                # MINI STATEMENT
##                elif choice == "5":
##
##                    print("\n===== MINI STATEMENT =====")
##
##                    if len(accounts[acc_number]["transactions"]) == 0:
##                        print("No transactions yet.")
##                    else:
##                        for t in accounts[acc_number]["transactions"]:
##                            print(t)
##
##                # LOGOUT
##                elif choice == "6":
##                    print("Logged out successfully.")
##                    break
##
##                else:
##                    print("Invalid choice.")
##
##        else:
##            print("Invalid Account Number or PIN.")
##
##    # EXIT
##    elif main_choice == "3":
##        print("Thank you for using ATM.")
##        break
##
##    else:
##        print("Invalid choice.")'''
##
##
##
##'''<!DOCTYPE html>
##<html lang="en">
##<head>
##<meta charset="UTF-8">
##<title>Multi Bank ATM</title>
##
##<style>
##
##/* ===== BODY STYLE ===== */
##
##body {
##    font-family: Arial;
##    background: linear-gradient(to right, #1d2671, #c33764);
##    display: flex;
##    justify-content: center;
##    align-items: center;
##    height: 100vh;
##}
##
##/* ===== ATM CARD ===== */
##
##.container {
##    width: 350px;
##    background: white;
##    padding: 20px;
##    border-radius: 15px;
##    box-shadow: 0 0 20px black;
##    text-align: center;
##}
##
##h2 {
##    color: #1d2671;
##}
##
##/* ===== INPUTS ===== */
##
##input, select {
##    width: 90%;
##    padding: 10px;
##    margin: 8px;
##    border-radius: 8px;
##    border: 1px solid gray;
##}
##
##/* ===== BUTTON ===== */
##
##button {
##    width: 95%;
##    padding: 10px;
##    margin: 6px;
##    background: #1d2671;
##    color: white;
##    border: none;
##    border-radius: 8px;
##    cursor: pointer;
##}
##
##button:hover {
##    background: #c33764;
##}
##
##.menu {
##    display: none;
##}
##
##.balance-box {
##    font-size: 20px;
##    font-weight: bold;
##    color: green;
##}
##
##</style>
##</head>
##
##<body>
##
##<div class="container">
##
##<h2>🏧 Multi Bank ATM</h2>
##
##<!-- CREATE ACCOUNT -->
##
##<div id="createSection">
##
##<select id="bank">
##<option>Canara Bank</option>
##<option>SBI</option>
##<option>ICICI Bank</option>
##<option>Union Bank</option>
##</select>
##
##<input type="text" id="accNumber" placeholder="Account Number">
##
##<input type="text" id="name" placeholder="Your Name">
##
##<input type="password" id="pin" placeholder="Create PIN">
##
##<button onclick="createAccount()">Create Account</button>
##
##<hr>
##
##<input type="text" id="loginAcc" placeholder="Login Account Number">
##
##<input type="password" id="loginPin" placeholder="Enter PIN">
##
##<button onclick="login()">Login</button>
##
##</div>
##
##<!-- ATM MENU -->
##
##<div id="menuSection" class="menu">
##
##<h3 id="welcomeText"></h3>
##
##<div class="balance-box">
##Balance: ₹ <span id="balance">0</span>
##</div>
##
##<input type="number" id="amount" placeholder="Enter Amount">
##
##<button onclick="deposit()">Deposit</button>
##
##<button onclick="withdraw()">Withdraw</button>
##
##<button onclick="logout()">Logout</button>
##
##</div>
##
##</div>
##
##<script>
##
##/* ===== ACCOUNT STORAGE ===== */
##
##let accounts = {};
##let currentUser = null;
##
##/* ===== CREATE ACCOUNT ===== */
##
##function createAccount() {
##
##let bank = document.getElementById("bank").value;
##let acc = document.getElementById("accNumber").value;
##let name = document.getElementById("name").value;
##let pin = document.getElementById("pin").value;
##
##if (acc in accounts) {
##    alert("Account already exists!");
##    return;
##}
##
##accounts[acc] = {
##    bank: bank,
##    name: name,
##    pin: pin,
##    balance: 0
##};
##
##alert("Account created in " + bank);
##
##}
##
##/* ===== LOGIN ===== */
##
##function login() {
##
##let acc = document.getElementById("loginAcc").value;
##let pin = document.getElementById("loginPin").value;
##
##if (acc in accounts && accounts[acc].pin == pin) {
##
##currentUser = acc;
##
##document.getElementById("createSection").style.display = "none";
##document.getElementById("menuSection").style.display = "block";
##
##document.getElementById("welcomeText").innerHTML =
##"Welcome " + accounts[acc].name +
##"<br>" + accounts[acc].bank;
##
##updateBalance();
##
##}
##else {
##alert("Invalid Login!");
##}
##
##}
##
##/* ===== UPDATE BALANCE ===== */
##
##function updateBalance() {
##
##document.getElementById("balance").innerText =
##accounts[currentUser].balance;
##
##}
##
##/* ===== DEPOSIT ===== */
##
##function deposit() {
##
##let amt = Number(document.getElementById("amount").value);
##
##accounts[currentUser].balance += amt;
##
##updateBalance();
##
##alert("Money Deposited!");
##
##}
##
##/* ===== WITHDRAW ===== */
##
##function withdraw() {
##
##let amt = Number(document.getElementById("amount").value);
##
##if (amt > accounts[currentUser].balance) {
##alert("Insufficient Balance");
##}
##else {
##accounts[currentUser].balance -= amt;
##updateBalance();
##alert("Money Withdrawn!");
##}
##
##}
##
##/* ===== LOGOUT ===== */
##
##function logout() {
##
##currentUser = null;
##
##document.getElementById("createSection").style.display = "block";
##document.getElementById("menuSection").style.display = "none";
##
##alert("Logged Out");
##
##}
##
##</script>
##
##</body>
##</html>
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
## # type: ignore'''



import pyttsx3 

engine=pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

class Parents:
    def sound(self):
        print("waste fellow")

class Dad:
    def sound(self):
        print("poramboka")


class Mummy:
    def sound(self):
        print("bewarse yedava")

a= Parents()
b= Dad()
c= Mummy()

a.sound()

