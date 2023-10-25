import pandas as pd
import random
class ListaAluno:
    def listar(self):
        self.lista_df = pd.read_excel("alunos.xlsx")
        print(self.lista_df)

    def excluir_alunos(self):
        while True:
            falta=int(input("Deseja excluir um aluno da tabela?\n1-Para sim\n2-Para não\n"))
            if falta == 1:
                aluno=int(input("Digite o código do aluno que faltou: "))
                self.lista_df = self.lista_df.drop(aluno, axis=0)
                print("Aluno excluido com sucesso")
                print(self.lista_df)
            else:
                break
    def adicionar_aluno(self):
        while True:
            aluno = int(input("Gostaria de adicionar um aluno?\n1-Para adicionar\n2-Para não\n"))
            if aluno == 1:
                nome = input("Digite o nome do aluno: ")
                habilidade = input("Digite sua habilidade: ")

                novo_aluno = pd.DataFrame({'Nome': [nome], 'Habilidade': [habilidade]})

                if self.lista_df is None:
                    self.lista_df = novo_aluno
                else:
                    self.lista_df = pd.concat([self.lista_df, novo_aluno], ignore_index=True)

                print(f"Aluno {nome} adicionado com sucesso")
                print(self.lista_df)
            else:
                break
    def grupos(self):
        grupo_count = int(input("Quantos grupos você quer formar: "))
        alunos = self.lista_df['Nome'].tolist()
        random.shuffle(alunos)
        grupos = {f"Grupo {i+1}": [] for i in range(grupo_count)}

        alunos_por_grupo = len(alunos) // grupo_count

        for grupo in grupos:
            for _ in range(alunos_por_grupo):
                aluno = alunos.pop()
                grupos[grupo].append(aluno)

        grupo_atual = 1
        while alunos:
            aluno = alunos.pop()
            grupos[f"Grupo {grupo_atual}"].append(aluno)
            grupo_atual = (grupo_atual % grupo_count) + 1

        for grupo, alunos in grupos.items():
            print(f"{grupo}: {', '.join(alunos)}")
class Menu:
    def __init__(self):
        self.lista = ListaAluno()

    def interface(self):
        self.lista.listar()
        self.lista.excluir_alunos()
        self.lista.adicionar_aluno()
        self.lista.grupos()
Menu().interface()