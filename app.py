import os #importando esta biblioteca. Não precisei baixar nada, apenas puxei

# restaurantes = ['Pizzaria Jon Cleber', "Casa de massas Fleurins", 'Teste'] #isso é uma lista
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] #esse é um dicionario dentro da lista

os.system('cls') #aqui eu estou puxando um recurso desta biblioteca "os".

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes.')
    print('3. Alterar estado do restaurante.')
    print('4. Sair.\n')

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome
    - Categoria
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes.
    ''' #aqui eu criei uma dosctring q é nada mais nada menos q uma descricao do q o programa faz. Assim o desenvolvedor vai saber o q faz sem ter q decifrar o código.

    # pass     #esse "pass" é uma instrução nula, portanto faz com que nenhum comportamento seja realizado.  # a implementação real será adicionada mais tarde
    exibir_subtitulos('Cadastrando restaurante:')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}\n')
    # restaurantes.append(nome_do_restaurante) #esse append é como o push do javascript. Ele vai ACRESCENTAR o valor pra lista
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    os.system('cls')
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n') #este f no início é necessário pra poder usar a variável desta forma.
    voltar()

def listar_restaurantes():
    exibir_subtitulos('Listando restaurantes:')
    print(f'{'Nome do restaurante:'.ljust(24)} |{'Categoria:'.ljust(22)}| {'Status:'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(22)} | {categoria_restaurante.ljust(22)} | {ativo_restaurante}') #ljust ajusta horizonatalmente. adicionando ' '.
    print('\n')
    voltar()

def alternar_estado_restaurante():
    exibir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado. \n')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #esse "not" atua como um inversor de estado. Se essa chave estiver como false, ao usar o not ele vai tornar a chave em true.
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!\n' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!\n' #ternário aqui.    
            print(mensagem)
    if not restaurante_encontrado:
        print(f'{nome_restaurante} não foi encontrado.\n')
    voltar() 

def escolher_opcao():
    try:  #esse try com except é tipo assim: "poo, tenta fazer isso daqui pra mim. Se não conseguir, faz isso aq ent(o q ta dentro do except) é um condicional bem legal"
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção {opcao_escolhida}.')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
        # OU
        #         opcao_escolhida = int(input('Escolha uma opção: '))
        # match opcao_escolhida:
        #     case 1:
        #         print('Adicionar restaurante')
        #     case 2:
        #         print('Listar restaurantes')
        #     case 3:
        #         print('Ativar restaurante')
        #     case 4:
        #         print('Finalizar app')
        #     case _:
        #         print('Opção inválida!')
    except:
        opcao_invalida()

def voltar():
    input("Pressione 'Enter' para voltar ao menu principal\n")
    main()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = ('*' * len(texto)) #len é uma função do próprio python "lengh"
    print(linha)
    print(texto)
    print(f'{linha}\n')

def finalizar_app():  #aqui estou definindo uma funçaõ. o "def" é como escrever "function" no javascript
    os.system('cls') #aqui eu estou puxando um recurso desta biblioteca "os".
    print('Encerrando o programa...\n')

def opcao_invalida():
    exibir_subtitulos('Opção inválida.')
    voltar()

def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""") 
#aqui eu copiei e colei esse texto no site fsimbols q tem formatações legais para textos em terminais

if __name__ == '__main__': #aqui eu defini que o main pode ser chamado quando eu quiser. Nele eu estou chamando as devidas funções e organizando o código.
    main()
