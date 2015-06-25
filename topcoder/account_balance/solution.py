"""
You are working for the financial institution TopBank, and you have been tasked with writing a module that will take an initial account balance, along with a list of that day's transactions, and return the ending balance for the day.

Each transaction will be either a credit, which adds funds to the account, or a debit, which removes funds from the account. If a debit exceeds the available funds at the time, then the account balance will go negative. You will be given an startingBalance, the initial account balance. You will also be given a transactions, the list of transactions for the day. Each element of transactions will be in the form "type amount" (quotes added for clarity). Each type will be 'C' or 'D', for credit or debit, respectively. Each amount will be an integer between 1 and 1000000, inclusive, with no leading zeros. You are to return an representing the ending balance after processing all of the transactions.

Class: AccountBalance
Method: processTransactions
Parameters: int, String[]
Returns: int
Method signature: int processTransactions(int startingBalance, String[] transactions)

"""

class AccountBalance():
    
    def processTransactions(self,startingBalance,transactions):
        endBalance = startingBalance
        for t in transactions:
            trans = t.split()
            if trans[0] == "C":
                endBalance = endBalance + int(trans[1])
            elif trans[0] == "D":
                endBalance = endBalance - int(trans[1])
        return endBalance




if __name__ == "__main__":
    ab = AccountBalance()
    print ab.processTransactions(100, ["C 100", "D 20", "C 500", "D 50"])








