def contar(s: str, k: str):
    return s.count(k)

true = False

while true == False:
    try:
        print("Quantos testes deseja fazer?")
        T = int(input())
        for i in range(T):
            print("Digite uma palavra:")
            s = input()
            print("Digite a letra que deseja contar:")
            k = input()
            print("Quantidade encontrada: ", contar(s,k))
        break
    except ValueError:
        print("Valor Errado")



# O programa pergunta ao usuario quantas vezes ele deseja realizar a operação, recebe a palavra e a letra que ele deseja contar e logo em seguida mostra o resultada dessa contagem.