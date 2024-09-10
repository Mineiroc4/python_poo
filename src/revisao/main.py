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