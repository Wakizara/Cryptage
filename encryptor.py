import string
password = input("Enter a word you want to encrypt: ").lower()

print("*************Let's encrypt your password*************")

# Création de l'ensemble_1 (alphabet)
ensemble_1 = list(string.ascii_lowercase)

# Création de l'ensemble_2 (0-26)
ensemble_2 = list(range(27))

# Création de l'ensemble_3 (30-57)
ensemble_3 = list(range(30, 58))

encrypted_password = []
for char in password:
    if char in ensemble_1:
        # Étape 1: Trouver l'index inverse dans l'alphabet (a->z, b->y, etc.)
        reverse_index = 25 - ensemble_1.index(char)
        
        # Étape 2: Convertir en nombre de ensemble_2 et soustraire 5
        num_value = (reverse_index - 5) % 27  # Utilisation du modulo pour gérer les nombres négatifs
        
        # Étape 3: Multiplier par la valeur correspondante dans ensemble_3
        final_value = num_value * ensemble_3[num_value]
        
        # Ajouter le résultat avec le séparateur
        encrypted_password.append(str(final_value) + ".")
    else:
        # Pour les caractères qui ne sont pas des lettres
        encrypted_password.append("_")

# Joindre tous les éléments pour former le résultat final
result = "".join(encrypted_password)
print(f'encrypted_password: {result}')

