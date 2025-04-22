import re


def validar_contato(nome, telefone, email, favorito):
    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if len(nome) < 3:
        print("Nome inválido!")
        return False
    if not telefone.isdigit():
        print("Telefone inválido!")
        return False
    elif not re.match(padrao_email, email):
        print("Email inválido!")
        return False
    elif favorito not in ["S", "N"]:
        print("Favorito inválido!")
        return False
    
    return True


def adicionar_contato(agenda, nome, telefone, email, marcar_como_favorito = "N"):
    if validar_contato(nome, telefone, email, marcar_como_favorito):
        favorito = True if marcar_como_favorito == "S" else False
        contato = { "nome": nome, "telefone": telefone, "email": email, "favorito": favorito }
        agenda.append(contato)
        print(f"Contato {nome} foi adicionado com sucesso!")
    else:
        print("Foi informado um valor inválido. Tente novamente!")

    return


def visualizar_contatos(agenda):
    print("\nLista de contatos cadastrados:")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. Nome: {nome} | Telefone: {telefone} | Email: {email} | Favorito: [{favorito}]")
    
    return


def editar_contato(agenda, indice_contato, nome, telefone, email, marcar_como_favorito = "N"):
    indice_contato_ajustado = int(indice_contato) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        if validar_contato(nome, telefone, email, marcar_como_favorito):
            favorito = True if marcar_como_favorito == "S" else False
            agenda[indice_contato_ajustado]["nome"] = nome
            agenda[indice_contato_ajustado]["telefone"] = telefone
            agenda[indice_contato_ajustado]["email"] = email
            agenda[indice_contato_ajustado]["favorito"] = favorito
            print(f"Contato {nome} foi atualizado com sucesso!")
        else:
            print("Foi informado um valor inválido. Tente novamente!")
    else:
        print("Índice do contato inválido.")
        
    return


agenda = []
while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar um novo contato")
    print("2. Visualizar a lista de contatos cadastrados")
    print("3. Editar um contato")
    print("4. Marcar/desmarcar um contato como favorito")
    print("5. Visualizar a lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    match escolha:
        case "1":
            nome = input("Digite o nome do contato (mínimo de 3 caracteres): ")
            telefone = input("Digite o telefone do contato (apenas números): ")
            email = input("Digite o email do contato (válido): ")
            marcar_como_favorito = input("Deseja marcar este contato como favorito? [S/N]: ")

            adicionar_contato(agenda, nome, telefone, email, marcar_como_favorito)
        
        case "2":
            visualizar_contatos(agenda)

        case "3":
            visualizar_contatos(agenda)
            indice_contato = input("Digite o número do contato que deseja editar: ")
            nome = input("Digite o novo nome do contato (mínimo de 3 caracteres): ")
            telefone = input("Digite o novo telefone do contato (apenas números): ")
            email = input("Digite o novo email do contato (válido): ")
            marcar_como_favorito = input("Deseja marcar este contato como favorito? [S/N]: ")
            editar_contato(agenda, indice_contato, nome, telefone, email, marcar_como_favorito)

        case "4":
            print("Funcionalidade ainda não implementada.")

        case "5":
            print("Funcionalidade ainda não implementada.")

        case "6":
            print("Funcionalidade ainda não implementada.")

        case "7":
            break

print("Programa finalizado")