from livros import Livro

def estoque_atual(livros): 
    if not livros:
        print('Catálogo vazio.')
    else:
        Livro.listar_livros()

def subtracao_material(livros):
    nome_livro = input('Qual livro foi vendido? ')
    quantidade = int(input('Quantos livros foram tirados do catálogo? '))
    for livro in livros:
        if livro.nome.lower() == nome_livro.lower():
            livro.estoque -= quantidade
            estoque_atual(livros)
            return
    print('Livro não encontrado no catálogo.')

def adicao_material(livros):
    nome_livro = input('Qual livro chegou ao estoque? ')
    quantidade = int(input('Quantos livros novos chegaram? '))
    for livro in livros:
        if livro.nome.lower() == nome_livro.lower():
            livro.estoque += quantidade
            estoque_atual(livros)
            return
    print('Livro não encontrado no catálogo.')

def adicao_livros_catalogo(livros):
    nome_livro = input('Qual livro novo chegou ao estoque? ') 
    nome_autor = input('Qual o nome do autor do livro? ')
    ano_livro = input('Qual o ano de lançamento do livro? ')
    quant_livro_novo = int(input('Quantos exemplares chegaram ao estoque? '))
    novo_livro = Livro(nome=nome_livro,autor=nome_autor,ano=ano_livro,estoque=quant_livro_novo)
    livros.append(novo_livro)
    estoque_atual(livros)
    
def main():
    livros = []
    while True:
        menu = input(
            'Menu App Livraria\n'
            'Selecione a opção:\n'
            '(1) para acessar o catálogo de livros atual\n'
            '(2) para adicionar um livro novo ao catálogo\n'
            '(3) Adicionar livros ao estoque\n'
            '(4) Subtrair livros do estoque\n'
            '(F) para desativar o programa.\n'
            'Digite a opção: '
        ).upper()

        if menu == '1':
            estoque_atual(livros)
        elif menu == '2':
            adicao_livros_catalogo(livros)
        elif menu == '3':
            adicao_material(livros)
        elif menu == '4':
            subtracao_material(livros)
        elif menu == 'F':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()