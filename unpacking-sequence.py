p = (4, 5)

x, y = p

print(x)
print(y)
print('---------------')

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)

print('-------------------')

_, shares, price, _ = data
print(shares)
print(price)
print('--------------')

record = ('Dave', 'dave@example.com', '773-555-1212', '845-456-65')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

print('--------------- ')

items = [1, 10, 7, 4, 5, 9]
head, *tails = items
print(head)
print(tails)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))



print('------------')