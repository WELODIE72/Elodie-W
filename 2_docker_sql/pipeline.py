# Script Python destiné à afficher des arguments de ligne de commande et formater une chaîne

import sys
import pandas as pd

print(sys.argv)

day = sys.argv[1]

# formatage de la chaîne pour construire des chaînes dynamiques
print(f'job finished successfully for day = {day}')
