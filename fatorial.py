class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def obter_salario(self):
        return self.__salario

    def aumentar_salario(self, percentual):
        self.__salario += self.__salario * (percentual / 100)

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus

    def obter_salario(self):
        return super().obter_salario() + self.bonus

funcionario = Funcionario("João", "Desenvolvedor", 3000)
gerente = Gerente("Maria", "Gerente de Projetos", 5000, 1000)

print("Salário inicial do funcionário:", funcionario.obter_salario())
print("Salário inicial do gerente:", gerente.obter_salario())

funcionario.aumentar_salario(10)
gerente.aumentar_salario(10)

print("Salário do funcionário após aumento:", funcionario.obter_salario())
print("Salário do gerente após aumento:", gerente.obter_salario())