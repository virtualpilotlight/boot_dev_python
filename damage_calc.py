import math
from tabulate import tabulate

weapons = [["Sword", 5], ["Axe", 7], ["Wand", 4]]
results = []

for weapon in weapons:
  name = weapon[0]
  damage = weapon[1]
  power_attack = math.pow(damage, 2)
  results.append([name, damage, power_attack])

headers = ["Weapon", "Damage", "Power Attack"]
output = tabulate(results, headers)
print(output)