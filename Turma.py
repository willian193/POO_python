class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
    def matricular(self, nome_aluno):

        if nome_aluno in self.alunos:
            print(f"Aviso: O aluno '{nome_aluno}' já está matriculado nesta turma.")
        else:
            self.alunos.append(nome_aluno)
            print(f"Aluno '{nome_aluno}' matriculado com sucesso na turma {self.nome}.")

    def remover(self, nome_aluno):

        if nome_aluno in self.alunos:
            self.alunos.remove(nome_aluno)
            print(f"Aluno '{nome_aluno}' removido da turma.")
        else:
            print(f"Aviso: Aluno '{nome_aluno}' não foi encontrado para remoção.")

    def listar_alunos(self):

        print(f"\n--- Listagem de Alunos da Turma {self.nome} ---")
        if not self.alunos:
            print("Nenhum aluno matriculado.")
        else:

            for aluno in sorted(self.alunos):
                print(f"- {aluno}")
        print(f"Total de alunos matriculados: {len(self.alunos)}")
        print("-" * 40)

    def esta_matriculado(self, nome_aluno):

        if nome_aluno in self.alunos:
            print(f"Resultado: O aluno '{nome_aluno}' ESTÁ matriculado.")
            return True
        else:
            print(f"Resultado: O aluno '{nome_aluno}' NÃO está matriculado.")
            return False

minha_turma = Turma("DS")

print("--- 1. Matriculando 5 alunos ---")
minha_turma.matricular("Carlos")
minha_turma.matricular("Ana")
minha_turma.matricular("Eduardo")
minha_turma.matricular("Bruno")
minha_turma.matricular("Daniela")

print("\n--- 2. Tentando matricular um nome repetido ---")
minha_turma.matricular("Ana")

print("\n--- 3. Removendo 1 aluno (Eduardo) ---")
minha_turma.remover("Eduardo")

print("\n--- 4. Exibindo a listagem final ---")
minha_turma.listar_alunos()

print("--- 5. Verificando se o aluno removido ainda consta na turma ---")
minha_turma.esta_matriculado("Eduardo")