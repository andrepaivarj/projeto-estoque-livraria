from avaliacao import Avaliacao

class Livro:
    livros = []

    def __init__(self,nome,autor,ano,estoque):
        self.nome = nome
        self.autor = autor
        self.ano = int(ano)
        self.estoque = int(estoque)
        self.avaliacoes = []
        Livro.livros.append(self)

    @classmethod
    def listar_livros(cls):
        print(f'\n{'Nome'.ljust(20)} | {'Autor'.ljust(20)} | {'Ano'.ljust(20)} | {'Estoque'.ljust(20)} | {'Avaliações'}')
        for livro in cls.livros:
            print(f'{livro.nome.ljust(20)} | {livro.autor.ljust(20)} | {str(livro.ano).ljust(20)} | {str(livro.estoque).ljust(20)} | {livro.media_avaliacoes} \n\n')
    
    def receber_avaliacao(self,cliente,nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente,nota)
            self.avaliacoes.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self.avaliacoes:
            return '-'
        else:
            soma_das_notas = sum(avaliacao.nota for avaliacao in self.avaliacoes)
            quantidade_de_notas = len(self.avaliacoes)
            media = round(soma_das_notas/quantidade_de_notas,1)
            return media
