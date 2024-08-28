
def animal():
    op1, op2, op3= map(str, input().split())

    if op1 =='vertebrado':
        if op2 == 'ave':
            if op3 == 'carnivoro':
                print('aguia')
            else:
                print('pomba')
        else:
            if op3 == 'onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        if op2 == 'inseto':
            if op3 == 'hematofago':
                print("pulga")
            else:
                print("lagarta")
        else:
            if op3 == 'hematofago':
                print("sanguessuga")
            else:
                print("minhoca")
def tempevent():
    horacomeco = []
    horafim = []
    horacmc, minutocmc, segundocmc, horaf, minutof, segundof = 0,0,0,0,0,0


    dia, day = map(str,input().split())

    horacomeco = input().split()

    diafim, dayfim = map(str, input().split())

    horafim = input().split()

    day = int(day)
    dayfim = int(dayfim)
    horacmc = int(horacomeco[0])
    minutocmc = int(horacomeco[2])
    segundocmc = int(horacomeco[4])
    horaf = int(horafim[0])
    minutof = int(horafim[2])
    segundof = int(horafim[4])
    qtdhoras, qtdminutos, qtdsegundos, qtddias = 0,0,0,0

    if horacmc > horaf:
        qtddias = (dayfim - day)-1
        qtdhoras = ((horacmc - horaf)-24)*-1
        if minutocmc > minutof:
            qtdminutos = ((minutocmc - minutof)-60)*-1
        else:
            qtdminutos = (minutocmc - minutof)*-1
        if segundocmc > segundof:
            qtdsegundos = ((segundocmc - segundof)-60)*-1
        else:
            qtdsegundos = (segundocmc - segundof)*-1
        
            

    else:
        qtddias = dayfim - day
        qtdhoras = horacmc - horaf  
        if minutocmc > minutof:
            qtdminutos = ((minutocmc - minutof)-60)*-1
        else:
            qtdminutos = (minutocmc - minutof)*-1
        if segundocmc > segundof:
            qtdsegundos = ((segundocmc - segundof)-60)*-1
        else:
            qtdsegundos = (segundocmc - segundof)*-1
        
    print(f'{qtddias} dia(s)')
    print(f'{qtdhoras} hora(s)')
    print(f'{qtdminutos} minuto(s)')
    print(f'{qtdsegundos} segundo(s)')


contador = 0
nmrcasos = int(input())
itens = ['pedra', 'papel', 'tesoura', 'lagarto', 'Spock']
sheld = [nmrcasos]
raj = [nmrcasos]
for i in range(nmrcasos):
    sheld.append(i), sheld.append(i) = map(str, input().split())
for i in range(nmrcasos):
    #Caso Sheld pega pedra
    if sheld[i] == 'pedra':
        if sheld[i] == raj[i]:
            print(f'Caso #{contador+1}: De novo!')
        elif raj[i] == itens[2] or raj[i] == itens[3]:
            print(f'Caso #{contador+1}: Bazinga!')
        else:
            print(f'Caso #{contador+1}: Raj trapaceou!')
    elif sheld[i] == 'papel':
        if sheld[i] == raj[i]:
            print(f'Caso #{contador+1}: De novo!')
        elif raj[i] == itens[0] or raj[i] == itens[4]:
            print(f'Caso #{contador+1}: Bazinga!')
        else:
            print(f'Caso #{contador+1}: Raj trapaceou!')
    elif sheld[i] == 'tesoura':
        if sheld[i] == raj[i]:
            print(f'Caso #{contador+1}: De novo!')
        elif raj[i] == itens[1] or raj[i] == itens[3]:
            print(f'Caso #{contador+1}: Bazinga!')
        else:
            print(f'Caso #{contador+1}: Raj trapaceou!')
    elif sheld[i] == 'lagarto':
        if sheld[i] == raj[i]:
            print(f'Caso #{contador+1}: De novo!')
        elif raj[i] == itens[1] or raj[i] == itens[4]:
            print(f'Caso #{contador+1}: Bazinga!')
        else:
            print(f'Caso #{contador+1}: Raj trapaceou!')
    elif sheld[i] == 'Spock':
        if sheld[i] == raj[i]:
            print(f'Caso #{contador+1}: De novo!')
        elif raj[i] == itens[0] or raj[i] == itens[2]:
            print(f'Caso #{contador+1}: Bazinga!')
        else:
            print(f'Caso #{contador+1}: Raj trapaceou!')
    contador += 1





































"""if sheld == 'pedra' and (raj == itens[2] or raj == itens[3]):
        print(f'Caso #{contador+1}: Bazinga!')
    elif sheld == raj:
        print(f'Caso #{contador+1}: De novo!')
    elif raj == itens[1] or itens[4]:
        print(f'Caso #{contador+1}: Raj trapaceou!')
    #Caso sheld pega papel
    if sheld == 'papel' and (raj == itens[0] or raj == itens[4]):
        print(f'Caso #{contador+1}: Bazinga!')
    elif sheld == raj:
        print(f'Caso #{contador+1}: De novo!')
    elif raj == itens[2] or itens[3]:
        print(f'Caso #{contador+1}: Raj trapaceou!')
    #Caso sheld pega tesoura
    if sheld == 'tesoura' and (raj == itens[1] or raj == itens[3]):
        print(f'Caso #{contador+1}: Bazinga!')
    elif sheld == raj:
        print(f'Caso #{contador+1}: De novo!')
    elif raj == itens[0] or itens[4]:
        print(f'Caso #{contador+1}: Raj trapaceou!')
    #Caso sheld pega lagarto
    if sheld == 'lagarto' and (raj == itens[1] or raj == itens[4]):
        print(f'Caso #{contador+1}: Bazinga!')
    elif sheld == raj:
        print(f'Caso #{contador+1}: De novo!')
    elif raj == itens[2] or itens[0]:
        print(f'Caso #{contador+1}: Raj trapaceou!')
    #Caso sheld pega Spock
    if sheld == 'Spock' and (raj == itens[2] or raj == itens[0]):
        print(f'Caso #{contador+1}: Bazinga!')
    elif sheld == raj:
        print(f'Caso #{contador+1}: De novo!')
    elif raj == itens[1] or itens[3]:
        print(f'Caso #{contador+1}: Raj trapaceou!')"""