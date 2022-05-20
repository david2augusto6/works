# SIMULAÇÃO: ESCALAS DE TEMPERATURA
# ALUNO: DAVID AUGUSTO DE OLIVEIRA E SILVA - 2115080006
# TURMA: ECP02_T01
from convert import *

escInicial = ""
escFinal = ("C", "F", "K", "R")

# TEMPERATURA NA ESCALA DE ENTRADA
while True:
    print("""Escalas de entrada:
    => Celcius (C)
    => Fahrenheit (F)
    => Kelvin (K)""")
    escInicial = input("Digite a escala desejada: ").upper()
    print("="*30)
    if escInicial in "CFK":
        break
tempInicial = float(input(f"""Digite a temperatura em {"°" if escInicial in "CF" else ""}{escInicial}: """))

print("="*30)
print("Resultado:")
print("-"*10)

for i, esf in enumerate(escFinal):
   print(f'{tempInicial}{"°" if escInicial != "K" else ""}{escInicial} => '
         f'{convert(tempInicial, escInicial, esf)}{"°" if esf != "K" else ""}{esf}')
