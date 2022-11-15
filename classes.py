import json

class Bcolors:
    """Deixa o terminal mais bonito"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Game:
    """Classe que manipulada os dados de um jogo
    
    O jogo é sempre uma árvore de grau 2
    Todas as folhas são animais e o restante são perguntas"""

    def __init__(self, jogo):
        self.jogo = jogo


    def __str__(self):
        return json.dumps(self.jogo, ensure_ascii=False)

    
    def jogar_novamente(self):
        print("*" * 24)
        print("Continuar jogando?")
        print('"s" para SIM')
        print('"n" para NÃO')
        print("*" * 24)
        resposta = input("-> ")

        if resposta == "s":
            self.jogar()
        else:
            print("\nObrigado por jogar!")
            print("-" * 24)
            print("\n\n")

    
    def jogar(self):
        atual = self.jogo
        print(Bcolors.HEADER   + "\nPENSE EM UM ANIMAL" + Bcolors.ENDC)

        #Fica em loop até achar uma folha
        while len(atual) == 2:
            print("*" * 24)
            print(atual[0])
            print(Bcolors.OKGREEN    + '"s" para SIM' + Bcolors.ENDC)
            print(Bcolors.FAIL   + '"n" para NÃO' + Bcolors.ENDC)
            print("*" * 24)
            resposta = input("-> ")

            if resposta == "s":
                #Vai pro filho da direita
                atual = atual[1][0]
            elif resposta == "n":
                #Vai pro filho da esquerda
                atual = atual[1][1]

        #Achou uma folha (atual)
        print("*" * 24)
        print(Bcolors.HEADER   + "\nÉ um(a) " + atual + "!\n" + Bcolors.ENDC)
        print("Meu palpite está correto?")
        print(Bcolors.OKGREEN   + '"s" para SIM '+ Bcolors.ENDC + "/" + Bcolors.FAIL + ' "n" para NÃO' + Bcolors.ENDC)
        print("*" * 24)
        resposta = input("-> ")

        if resposta == "s":
            #Acertou
            self.jogar_novamente()
        elif resposta == "n":
            #Errou. Alimenta a base com um novo animal
            print("*" * 24)
            print(Bcolors.HEADER   + "Qual o seu animal?" + Bcolors.ENDC)
            print("*" * 24)

            animal = input("-> ")

            print("*" * 24)
            print(Bcolors.HEADER   + "Cite uma diferença de um(a) " + animal + " pra um(a) " + atual + Bcolors.ENDC)
            print("Exemplos: 'É aquático', 'Sabe voar', 'Faz auau', 'Come peixe'")
            print("*" * 24)

            pergunta = input("-> ")

            novoNo = [pergunta + "?", [animal, atual]]

            #Transforma folha atual em um nó com a pergunta inserida e o novo animal
            self.jogo = json.loads(json.dumps(self.jogo, ensure_ascii=False).replace(json.dumps(atual, ensure_ascii=False), json.dumps(novoNo, ensure_ascii=False)))

            self.jogar_novamente()
        else:
            print("Resposta inválida!\n")
            self.jogar_novamente()

class Save:
    """Classe que carrega/lista/remove/adiciona dados de diferente jogos"""

    def __init__(self, saveIndex=None, dados=None):
        self.saveIndex = saveIndex
        self.dados = dados

    def carregarSave(self):
        #Retorna save atual
        return json.load(open('dados.json'))[self.saveIndex-1]


    def removerSave(self):
        #Remove save atual
        saves = json.load(open('dados.json'))

        if len(saves) == 1:
            print("Não é possível remover esse Save")
            return
            
        del saves[self.saveIndex-1]    

        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(saves, f, ensure_ascii=False, indent=4)
        
    def salvarSave(self):
        #Atualiza json 
        saves = json.load(open('dados.json'))

        saves[self.saveIndex-1] = json.loads(str(self.dados))

        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(saves, f, ensure_ascii=False, indent=4)


    def listarSaves(self, opcaoDeCriar):
        #Lista todos os saves no json 
        saves = json.load(open('dados.json'))
        i = 1
        for save in saves:
            print(Bcolors.OKCYAN   + "--- " + str(i) + " >>> " + json.dumps(save, ensure_ascii=False)[:64] + " [...]" + Bcolors.ENDC)
            i = i + 1
        
        if opcaoDeCriar:
            print("0 >>> Novo Save")  
        print("*" * 24)
        opcao = int(input("-> "))
        if opcao == 0 and opcaoDeCriar:
            print("*" * 24)
            print("Insira o animal inicial:")
            print("*" * 24)
            animal = input("-> ")

            saves.append(animal)   

            with open('dados.json', 'w', encoding='utf-8') as f:
                json.dump(saves, f, ensure_ascii=False, indent=4)

            return len(saves)

        if opcao > i or opcao < 1:
            print("Opção inválida!")
            return False
        return opcao
