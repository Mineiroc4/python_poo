class Quiz:
    disciplina: str
    aluno: str
    __acertos: int
    __erros: int

    def __init__(self, disciplina, aluno, acertos, erros):
        self.disciplina = disciplina
        self.aluno = aluno
        self.__acertos = acertos
        self.__erros = erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def calcular_pontos(self):
        return self.__acertos - self.__erros

    def __str__(self):
        info = f'Discplina = {self.disciplina}\n'
        info += f'Aluno = {self.aluno}\n'
        info += f'Acertos = {self.__acertos}\n'
        info += f'Total de pontos = {self.calcular_pontos()}\n'
        return info
