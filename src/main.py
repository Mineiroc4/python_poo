from frota import *
import pickle
def operar_carro(carro : Carro):
        print('1- Ligar motor')
        print('2- Desligar motor')
        print('3- Acelerar')

        op = 0
        while op not in (1, 2, 3):
            op = int(input("Digite as opcoes[1-3]: "))

        if op == 1:
            carro.ligar()
        elif op == 2:
            carro.desligar()
        elif op == 3:
            v = float(input("Informe a velocidade: "))
            t = float(input("Informe o tempo: "))
            carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Quantos Litros tem no tanque'))
    cm = float(input('Qual consumo médio do carro: '))
    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    litros = float(input('Quantos Litros tem no tanque'))
    cm = float(input('Qual consumo médio do carro: '))
    kms = float(input('Digite com quantos Kms: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, litros, cm)

    carros = {}
    carros[id(carro1)] = carro1
    carros[id(carro2)] = carro2

    try:
        with open('carros.pkl', 'wb') as arquivo:
            carros = pickle.dump(carros, arquivo)
    except Exception as e:
        print(e)

    try:
        with open('carros.pkl', 'rb') as arquivo:
            carros = pickle.load(arquivo)
    except Exception as e:
        print(e)

    while carro1.getOdometro() < 600 and carro2.getOdometro() < 600 and (carro1.getTanque() >0 or carro2.getTanque()>0):
        try:
            op = 0
            while op not in (1,2):
                op = int(input("Qual carro [1,2]? "))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Informações atuais do carro')
            print(carro1)
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    print(carro1)
    print(carro2)