import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8,
}
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2,
}


def checkWinnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for sym, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(sym)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=' | ')
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("What Would You Like To Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a Number.")
    return amount
def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Enter a Number.")
    return lines
def get_bet():
    while True:
        amount = input("What Would You Like To Bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a Number.")
    return amount



def main():
    balance=deposit()
    lines=get_num_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines

        if total_bet>balance:
            print(f"You do not have to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You Are Betting ${bet} on {lines} lines. Total bet ${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines=checkWinnings(slots,lines,bet,symbol_value)
    print(f"You Won ${winnings}")
    print(f"You Won On Lines: ", *winning_lines)


    




main()