

condição = input("Você quer continuar no jogo? \n[1] Sim \n[2] Não ")

while (condição != '1' and condição != '2'):
    condição = input("Tente novamente! \nVocê quer continuar no jogo? \n[1] Sim \n[2] Não ")

if (condição == '1'):
    print ("Vamos continuar!")
    print ('================')
elif (condição == '2'):
    print ("Agradecemos sua participação! \nVolte sempre que quiser!")

tema = input("Escolha um personagem: \n[1] Frida Kahlo - Tema: Mulheres \n[2] Martin Luther King - Tema: Pessoas Negras \n[3] Stephen Hawking - Tema: PCD's ")

while (tema != '1' and tema != '2' and tema != '3'):
    tema = input("Tente novamente! \nEscolha um prsonagem: \n[1] Frida Kahlo - Tema: Mulheres \n[2] Martin Luther King - Tema: Pessoas Negras \n[3] Stephen Hawking - Tema: PCD's")

if (tema == '1'):
    print("Você escolheu a Frida Kahlo e o seu tema é sobre Mulheres.")
    print("==========================================")
    pergunta1 = ""
    print(pergunta1)
    print("==========================================")
    input("Marque a alternativa CORRETA: \n[1] Aa duas afirmativas são verdadeiras \n[2] A afirmativa I é verdadeira e a II é falsa \n[3] A afirmativa II é verdadeira e a I é falsa \n[4] As duas afirmativas são falsas ")
    print("==========================================")
    pergunta2 = "II. A respeito do direito de greve, da proteçã ao trabalho da mulher, da alteração da relação de trabalho" + \
        '\n' + "da aplicação de justa causa e da equiparação salarial, julgue o item que se segue. Se uma empregada," + \
        '\n' + "antes do término do cumprimento de aviso prévio de desligamento sem justa causa, apresentar ao empregador" + \
        '\n' + "atestado médico probatório de que, na data da dispensa, ela já estava grávida, tal fato não lhe derá o direito" + \
        '\n' + "à estabilidade prevista no texto constitucional, pois, quando foi dado o aviso prévio, o empregador desconhecia" + \
        '\n' + "o estado gravídico da empregada."
    print(pergunta2)
else:
    print("Até logo!")