habilidades = [
    ("MATLAB", 7),
    ("Python", 6),
    ("HTML y CSS", 6),
    ("VHDL", 8),
    ("C#", 4),
    ("JavaScript", 2)
]

for i in habilidades:
    barra = "█" * i[1] + "░" * (10 - i[1])
    print(f"{i[0].ljust(12)} {barra}  {i[1]}/10") # rellena con espacios hasta 12 caracteres

promedio = sum([i[1] for i in habilidades]) / len(habilidades)
print(f"\nPromedio de habilidades: {promedio:.2f}/10")