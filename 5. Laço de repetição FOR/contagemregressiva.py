import os
os.system("cls||clear")
import time

print("Contagem regressiva.")
for i in range(10,-1,-1):
    print(f"The bomb is planted: {i}")
    time.sleep(1)

print("BUM!")
