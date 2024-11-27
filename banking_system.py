
# Function to deposit money into an account
def deposit( account: dict, amount: float) -> None:
    account['balance'] += amount 
    return 
    
   

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    if account['balance'] > amount:
        account['balance'] -= amount 
   

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    if from_account['balance'] >= amount:
        from_account['balance'] -= amount
        to_account['balance'] += amount
    

# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    accounts[owner]['balance'] = initial_balance
    

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    accounts_list = [key for key in accounts]

    if owner in accounts_list:
        return accounts[owner]
    
    return 

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
