from classes import Game, Save, Bcolors

print(Bcolors.BOLD   + "-------!! AKINATOR !!-------" + Bcolors.ENDC)

save = 1
opcao = 0

while opcao != 5:
     print("*" * 24)
     print(Bcolors.WARNING    + "Save > " + str(save) + Bcolors.ENDC)
     print("\nEntre com uma opção:")
     print(Bcolors.OKCYAN + " --- 1: Jogar")
     print(" --- 2: Ver Save")
     print(" --- 3: Mudar Save")
     print(" --- 4: Deletar Save")
     print(" --- 5: Sair do programa" + Bcolors.ENDC)     
     print("*" * 24)

     opcao = int(input("-> "))

     if opcao == 1:
        #1 --- Jogar
        jogoSalvo = Save(save).carregarSave()
        game = Game(jogoSalvo)
        game.jogar()
        Save(save,game).salvarSave()

     elif opcao == 2:
        #2 --- Ver
        jogoSalvo = Save(save).carregarSave()
        print("*" * 24)
        print("Save " + str(save) + ":")
        print(jogoSalvo)

     elif opcao == 3:
        #3 --- Mudar/Criar
        saveSelecionado = Save().listarSaves(True)
        if type(saveSelecionado) == int:
            save = saveSelecionado

     elif opcao == 4:
        #4 --- Deletar
        saveSelecionado = Save().listarSaves(False)
        if type(saveSelecionado) == int:
            Save(saveSelecionado).removerSave()

     elif opcao == 5:
        #5 --- Sair
        break

     else:
        print("Opção inválida")