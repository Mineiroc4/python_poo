from Quiz import *

if __name__ == "__main__":

    q1 = Quiz(10, 5) #5 pontos
    print(q1)

    q2 = Quiz2A(15, 3)#3 pontos
    print(q2)

    q3 = Quiz3A(15,3)#9 pontos
    print(q3)

    lista_quiz = [q1,q2,q3]

    aluno1 = Aluno(1,"Rafael", lista_quiz)
    print(aluno1)

    aluno2 = Aluno(2, "Rafael2", lista_quiz)

    aluno3 = Aluno(1, "RafaelFake", lista_quiz)

    poo = Disciplina("POO", "Ferauche", 2024,2)
    poo.add_aluno(aluno1)
    poo.add_aluno(aluno2)
    '''
    teste para causar erro de aluno já existente caso tente inserir um aluno com mesma matrícula ou instanciar o mesmo aluno novamente.
    poo.add_aluno(aluno3)
    '''
    print(poo)