import math
ângulo = float(input('Digite o Ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print (f'O seno, cosseno e tangente do ângulo são respectivos: {seno:.2f}, {cosseno:.2f}, {tangente:.2f}.')