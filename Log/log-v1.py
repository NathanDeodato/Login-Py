# Colors
verde = '\033[32m'
vermelho = '\033[31m'
ciano = '\033[36m'
branco = '\033[37m'

def log():
    try:
        print(ciano + "=-" * 25 + branco)
        print(ciano + "-- Logar --".center(50))
        
        # Credenciais correstas
        user = "NT"
        password = "Deodato12"

        # Credenciais do input
        txtuser = str(input(ciano + "User: "))
        txtpass = str(input("Password: "))

        # Confirmação de credenciais
        okuser = "Ok"
        inuser = "Incorrect"

        okpass = "Ok"
        inpass = "Incorrect"

        print(ciano + "=-" * 25 + branco)

        # Verificando credenciais
        if txtuser == "NT":
            print(verde + f"User: {okuser}" + branco)
        else:
            print(vermelho + f"User: {inuser}" + branco)

        if txtpass == "Deodato12":
            print(verde + f"Password: {okpass}" + branco)
        else:
            print(vermelho + f"Password: {inpass}" + branco)

    except Exception as erro:
        pass
    else:
        pass


usuario = 1
# Loop do log
while True:
    print(ciano + "=-" * 25)
    print("-- Loguin v1--".center(50))
    print("=-" * 25 + branco)
    
    print(ciano + "[ 1 ] Loguin")
    print(ciano + "[ 2 ] Exit")
    
    print(ciano + "=-" * 25)

    # Opção do usuario
    usuario = str(input(ciano + "Option: "))

    # Opções
    if usuario == "1":
        log()
    elif usuario == "2":
        print(ciano + "Sistem log exit...")
        print(ciano + "=-" * 25)
        break
    else:
        print(vermelho + "Option ERRO!")
