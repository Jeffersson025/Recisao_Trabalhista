print("\n*****************Recisao trabalhista******************\n")

salario = float(input("Digite o valor do salario: "))
tmp = int(input("\nDigite a quantidade de meses trabalhados: "))
fgts = 0.08 * salario * tmp
decTerc = (salario / 12) * tmp
ferias = (salario / 12) * tmp
UmTerco = ferias/3
total = fgts + decTerc + ferias

print("\nSua recisão de trabalho é de: R$ {:.2f}\n".format(total))

print('1 - detalhes: \n2 - Sair: ')
mais = input('Digite uma opção para continuar: ')
if mais == '1':
    print('\nFgts: {:.2f} \nDecimo terceiro: {:.2f}\nFerias: {:.2f}\nUm terco de ferias: {:.2f}\n\nTOTAL: {:.2f}'.format(fgts, decTerc, ferias, UmTerco, total))
input("\npressione qualquer tecla para encerrar...\n")