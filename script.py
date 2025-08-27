def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

def menu_operacoes(entidade):
    print(f"\n=== [{entidade.upper()}] MENU DE OPERAÇÕES ===")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")

while True:
    menu_principal()
    escolha = input("Escolha uma opção (1-6): ")

    if escolha == "6":
        print("Encerrando o sistema...")
        break

    entidades = {
        "1": "Estudantes",
        "2": "Professores",
        "3": "Disciplinas",
        "4": "Turmas",
        "5": "Matrículas"
    }

    entidade = entidades.get(escolha)
    if entidade:
        while True:
            menu_operacoes(entidade)
            operacao = input("Escolha uma operação (1-5): ")

            if operacao in ["1", "2", "3", "4"]:
                print(f"Você escolheu a operação '{operacao}' para a entidade '{entidade}'.")
            elif operacao == "5":
                print(f"\nVoltando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
