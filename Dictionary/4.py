'''Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})'''


l1 = [{'item': 'item1', 'amount': 400},
      {'item': 'item2', 'amount': 300},
      {'item': 'item1', 'amount': 750}]

d1={}

for entry in l1:
    item = entry['item']
    amount = entry['amount']

    if item in d1:
        d1[item] += amount
    else:
        d1[item] = amount

print(d1)