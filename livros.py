class Livro:
    livros = []

    def __init__(self,nome,autor,ano,estoque):
        self.nome = nome
        self.autor = autor
        self.ano = int(ano)
        self.estoque = int(estoque)
        Livro.livros.append(self)

    @classmethod
    def listar_livros(cls):
        print(f'{'Nome'.ljust(50)} | {'Autor'.ljust(30)} | {'Ano'.ljust(30)} | {'Estoque'}')
        for livro in cls.livros:
            print(f'{livro.nome.ljust(50)} | {livro.autor.ljust(30)} | {str(livro.ano).ljust(30)} | {livro.estoque}\n\n')
