password = 'A24HJ32'

print("Let's Play")
alphabet_mapping = {}

ensemble_1 = []
for i in range(0, 26):
    ensemble_1.append(i)

print(ensemble_1)

ensemble_2 = []
for i in range(0, 9):
    ensemble_2.append(i)

print(ensemble_2)

ensemble_3 = [30]
for i in range(202, 301):
    ensemble_3.append(i)

print(ensemble_3)

encrypted_passord = []
for letter in password:
    if letter == password:
        encrypted_passord += ensemble_1
        print(f'Encrypted password: {encrypted_passord}')

for number in password:
    if number == password:
        encrypted_passord += ensemble_2
        print(f'Encrypted password: {encrypted_passord}')   

print(f'encrypted_passord: {encrypted_passord}')



