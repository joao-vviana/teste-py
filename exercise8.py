ativPratica = float(input("Digite a nota que você tirou na atividade prática do GA: "))
ativTeorica = float(input("Digite a nota que você tirou na atividade teórica do GA: "))

grauA = (ativPratica * 0.45) + (ativTeorica * 0.55) 
print("O resultado do grau A é:", grauA)

provaLab = float(input("Digite a nota que você tirou na prova em laboratório do GB: "))
testeTeorico = float(input("Digite a nota que você tirou no teste teórico do GB: "))
trabExtra = float(input("Digite a nota que você tirou no trabalho extraclasse do: "))

grauB = (provaLab * 0.6) + (testeTeorico * 0.2) + (trabExtra * 0.2)
print("O resultado do grau B é:", grauB)

notaFinal = (grauA * 0.33) + (grauB * 0.67)
print("Sua nota final é:", notaFinal)