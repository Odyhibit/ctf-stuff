from log_utilities import *


with open("Payments/payments.log", "r") as log_file:
    state_totals = {}  # state: occurrence_count
    purchase_id = ""
    transactions = 0
    top_transaction = 0.0
    get_id = False  # should we collect purchase id from response

    for line in log_file:
        if 'Request:' in line:
            price = get_text_between(line, 'currencyID="USD">', '<')
            state = get_text_between(line, '<ebl:StateOrProvince>', '<')
            transactions += 1
            price = float(price)
            add_or_create(state_totals, state)
            if price > top_transaction:
                top_transaction = price
                get_id = True
        if 'Response:' in line and get_id:
            purchase_id = get_text_between(line, '<TransactionID>', '<')
            get_id = False

    print(f"there are {in_green(transactions)} transactions in the log")
    print(f"the transaction id of the largest purchase is {in_green(purchase_id)}")
    print(f"{in_green(max(state_totals, key=state_totals.get))} had the most purchases")


"""
Q1 How many transactions are contained in the log?
Q2 What is the transaction ID of the largest purchase made in the log?
Q3 Which state made the most number of purchases?
"""