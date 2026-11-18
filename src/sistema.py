
# ==========================================
# NEIGHBORHOOD ACTION DASHBOARD
# Sistema de ocorrencias comunitarias
# Projeto academico - FIAP
# ==========================================


from ocorrencias import (    
    ocorrencias,  
    cadastrar_ocorrencia, 
    listar_ultimas_atualizacoes, 
    listar_ocorrencias,
    buscar_ocorrencia,
    filtrar_por_categoria,
    filtrar_por_status,
    atualizar_status,
    contar_por_categoria as contagem_por_categoria,
    calcular_percentuais as percentual_por_categoria,
    contar_por_status as contagem_por_status,
    calcular_percentuais_status as percentual_por_status,
    listar_historico,
    listar_fila_atendimento,
    mostrar_hierarquia,
    mostrar_matriz_indicadores,
    mostrar_pendencias,
)



def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Listar ocorrencias")
    print("2 - Buscar ocorrencia")
    print("3 - Filtrar por categoria")
    print("4 - Filtrar por status")
    print("5 - Atualizar status")
    print("6 - Exibir estatisticas")
    print("7 - Consultar historico")
    print("8 - Exibir fila de atendimento") 
    print("9 - Cadastrar nova ocorrencia")  
    print("10 - Ultimas atualizacoes")  
    print("11 - Hierarquia de ocorrencias")
    print("12 - Matriz de indicadores")
    print("13 - Indicador de pendencias") 
    print("0 - Sair")


def main():
    print("=" * 45)
    print("       NEIGHBORHOOD ACTION DASHBOARD")
    print("=" * 45)

    print("\nBem-vindo ao sistema de gestao comunitaria!")
    print("Projeto academico - FIAP")
    print("Total de registros:", len(ocorrencias))

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "1":
            listar_ocorrencias()

        elif opcao == "2":
            codigo = input("Digite o ID da ocorrencia: ")
            buscar_ocorrencia(codigo.strip())

        elif opcao == "3":
            categoria = input("Digite a categoria: ")
            filtrar_por_categoria(categoria.strip())

        elif opcao == "4":
            status = input("Digite o status: ")
            filtrar_por_status(status.strip())

        elif opcao == "5":
            codigo = input("Digite o ID da ocorrencia: ")
            novo_status = input("Digite o novo status: ")
            atualizar_status(codigo.strip(), novo_status.strip())

        elif opcao == "6":
            print("\n===== ESTATISTICAS =====")
            contagem_por_categoria()
            percentual_por_categoria()
            contagem_por_status()
            percentual_por_status()

        elif opcao == "7":
            listar_historico()

        elif opcao == "8":
            listar_fila_atendimento()

        
            
        elif opcao == "9":
            print("\n===== CADASTRAR OCORRENCIA =====")

            codigo = input("Digite o codigo: ").strip()
            categoria = input("Digite a categoria: ").strip()
            descricao = input("Digite a descricao: ").strip()
            local = input("Digite o local: ").strip()
            data = input("Digite a data de abertura: ").strip()

            cadastrar_ocorrencia(
                codigo,
                categoria,
                descricao,
                local,
                data
            ) 
        elif opcao == "10":
            listar_ultimas_atualizacoes() 
        elif opcao == "11":
            mostrar_hierarquia()

        elif opcao == "12":
            mostrar_matriz_indicadores()

        elif opcao == "13":
            mostrar_pendencias()
        elif opcao == "0":
            print("\nEncerrando o sistema. Ate logo!")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
