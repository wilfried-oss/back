import numpy as np
import array

poids = [120, 60, 58]
taille = [1.8, 1.8, 1.5]
# on veut calculer avec les deux elements lindice de masse corporelle imc
np_poids = np.array(poids)
np_taille = np.array(taille)

imc = np_poids / np_taille ** 2

print(imc)