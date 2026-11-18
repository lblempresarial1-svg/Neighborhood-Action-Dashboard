
# ==========================================
# NEIGHBORHOOD ACTION DASHBOARD
# Cadastro de ocorrencias comunitarias
# ==========================================

from collections import deque

# Categorias permitidas
CATEGORIAS = [
    "Iluminacao",
    "Limpeza",
    "Conservacao",
    "Acessibilidade"
]

# Situacoes permitidas
STATUS_VALIDOS = [
    "Aberta",
    "Em analise",
    "Concluida"
]

# Lista inicial de ocorrencias
ocorrencias = [

    {
        "id": "OC001",
        "categoria": "Iluminacao",
        "descricao": "Poste com lampada apagada",
        "local": "Praca Central",
        "data_abertura": "01/11/2026",
        "status": "Aberta"
    },
    {
        "id": "OC002",
        "categoria": "Limpeza",
        "descricao": "Acumulo de lixo na calcada",
        "local": "Rua das Flores",
        "data_abertura": "02/11/2026",
        "status": "Em analise"
    },
    {
        "id": "OC003",
        "categoria": "Acessibilidade",
        "descricao": "Calcada sem rampa",
        "local": "Avenida Principal",
        "data_abertura": "03/11/2026",
        "status": "Aberta"
    },
    {
        "id": "OC004",
        "categoria": "Conservacao",
        "descricao": "Banco danificado",
        "local": "Parque Municipal",
        "data_abertura": "04/11/2026",
        "status": "Concluida"
    },
    {
        "id": "OC005",
        "categoria": "Iluminacao",
        "descricao": "Luminaria com defeito",
        "local": "Rua do Comercio",
        "data_abertura": "05/11/2026",
        "status": "Em analise"
    },
    {
        "id": "OC006",
        "categoria": "Limpeza",
        "descricao": "Lixeira transbordando",
        "local": "Praca da Escola",
        "data_abertura": "06/11/2026",
        "status": "Aberta"
    },
    {
        "id": "OC007",
        "categoria": "Acessibilidade",
        "descricao": "Piso irregular",
        "local": "Rua das Palmeiras",
        "data_abertura": "07/11/2026",
        "status": "Em analise"
    },
    {
        "id": "OC008",
        "categoria": "Conservacao",
        "descricao": "Equipamento danificado",
        "local": "Parque Central",
        "data_abertura": "08/11/2026",
        "status": "Aberta"
    },
    {
        "id": "OC009",
        "categoria": "Iluminacao",
        "descricao": "Poste com falha",
        "local": "Rua do Lago",
        "data_abertura": "09/11/2026",
        "status": "Concluida"
    },
    {
        "id": "OC010",
        "categoria": "Limpeza",
        "descricao": "Entulho em area publica",
        "local": "Rua Horizonte",
        "data_abertura": "10/11/2026",
        "status": "Em analise"
    },
    {
        "id": "OC011",
        "categoria": "",
        "descricao": "Categoria ausente",
        "local": "Rua das Acacias",
        "data_abertura": "11/11/2026",
        "status": "Aberta"
    },
    {
        "id": "OC012",
        "categoria": "Conservacao",
        "descricao": "Calcada com rachaduras",
        "local": "Avenida do Bairro",
        "data_abertura": "12/11/2026",
        "status": "Aberta"
    }
]


# Funcao para validar uma ocorrencia

def validar_ocorrencia(ocorrencia):

    if not ocorrencia["id"] or not ocorrencia["local"]:
        return False

    if ocorrencia["categoria"] not in CATEGORIAS:
        return False

    if ocorrencia["status"] not in STATUS_VALIDOS:
        return False

    if not ocorrencia["descricao"] or not ocorrencia["data_abertura"]:
        return False

    return True


# Funcao para listar ocorrencias
def listar_ocorrencias():

    for ocorrencia in ocorrencias:

        if validar_ocorrencia(ocorrencia):

            print(
                ocorrencia["id"],
                "-",
                ocorrencia["categoria"],
                "-",
                ocorrencia["local"],
                "-",
                ocorrencia["status"]
            )

        else:
            print(
                "Registro invalido:",
                ocorrencia["id"]
            )

# ==========================================
# HISTORICO DE ATUALIZACOES
# ==========================================

historico = [
    {
        "id_ocorrencia": "OC001",
        "status_anterior": "Aberta",
        "novo_status": "Em analise",
        "data": "13/11/2026"
    },
    {
        "id_ocorrencia": "OC002",
        "status_anterior": "Em analise",
        "novo_status": "Concluida",
        "data": "13/11/2026"
    },
    {
        "id_ocorrencia": "OC003",
        "status_anterior": "Aberta",
        "novo_status": "Em analise",
        "data": "14/11/2026"
    },
    {
        "id_ocorrencia": "OC004",
        "status_anterior": "Concluida",
        "novo_status": "Em analise",
        "data": "14/11/2026"
    },
    {
        "id_ocorrencia": "OC005",
        "status_anterior": "Em analise",
        "novo_status": "Concluida",
        "data": "14/11/2026"
    },
    {
        "id_ocorrencia": "OC006",
        "status_anterior": "Aberta",
        "novo_status": "Em analise",
        "data": "15/11/2026"
    },
    {
        "id_ocorrencia": "OC007",
        "status_anterior": "Em analise",
        "novo_status": "Concluida",
        "data": "15/11/2026"
    },
    {
        "id_ocorrencia": "OC008",
        "status_anterior": "Aberta",
        "novo_status": "Em analise",
        "data": "15/11/2026"
    }
]


def listar_historico():
    print("\n===== HISTORICO DE ATUALIZACOES =====")

    for evento in historico:
        print(
            evento["id_ocorrencia"],
            "-",
            evento["status_anterior"],
            "->",
            evento["novo_status"],
            "-",
            evento["data"]
        )

def atualizar_status(codigo, novo_status):

    if novo_status not in STATUS_VALIDOS:
        print("Erro: status informado nao e valido.")
        return

    for ocorrencia in ocorrencias:

        if ocorrencia["id"] == codigo:

            if not validar_ocorrencia(ocorrencia):
                print("Erro: nao e possivel atualizar um registro invalido.")
                return

            status_anterior = ocorrencia["status"]

            if status_anterior == novo_status:
                print("A ocorrencia ja possui esse status.")
                return

            ocorrencia["status"] = novo_status

            historico.append({
                "id_ocorrencia": codigo,
                "status_anterior": status_anterior,
                "novo_status": novo_status,
                "data": "17/11/2026"
            })

            print("Status atualizado com sucesso!")
            print(status_anterior, "->", novo_status)
            return

    print("Erro: ocorrencia nao encontrada.")


def buscar_ocorrencia(codigo):

    indice = criar_indice_ocorrencias()

    ocorrencia = indice.get(codigo)

    if ocorrencia is None:
        for registro in ocorrencias:
            if registro["id"] == codigo:
                print("Erro: registro encontrado, mas possui dados invalidos.")
                return

        print("Erro: ocorrencia nao encontrada.")
        return

    print("\n===== OCORRENCIA ENCONTRADA =====")
    print("Codigo:", ocorrencia["id"])
    print("Categoria:", ocorrencia["categoria"])
    print("Descricao:", ocorrencia["descricao"])
    print("Local:", ocorrencia["local"])
    print("Data:", ocorrencia["data_abertura"])
    print("Status:", ocorrencia["status"])


def filtrar_por_categoria(categoria):

    encontrou = False

    print("\n===== FILTRO POR CATEGORIA =====")

    for ocorrencia in ocorrencias:

        if validar_ocorrencia(ocorrencia) and ocorrencia["categoria"] == categoria:

            print(
                ocorrencia["id"],
                "-",
                ocorrencia["descricao"],
                "-",
                ocorrencia["local"],
                "-",
                ocorrencia["status"]
            )

            encontrou = True

    if not encontrou:
        print("Nenhuma ocorrencia valida encontrada nessa categoria.")

def filtrar_por_status(status):

    encontrou = False

    print("\n===== FILTRO POR STATUS =====")

    if status not in STATUS_VALIDOS:
        print("Erro: status informado nao e valido.")
        return

    for ocorrencia in ocorrencias:

        if validar_ocorrencia(ocorrencia) and ocorrencia["status"] == status:

            print(
                ocorrencia["id"],
                "-",
                ocorrencia["categoria"],
                "-",
                ocorrencia["descricao"],
                "-",
                ocorrencia["local"]
            )

            encontrou = True

    if not encontrou:
        print("Nenhuma ocorrencia encontrada com esse status.")

def contar_por_categoria():

    print("\n===== OCORRENCIAS POR CATEGORIA =====")

    for categoria in CATEGORIAS:

        quantidade = 0

        for ocorrencia in ocorrencias:

            if validar_ocorrencia(ocorrencia) and ocorrencia["categoria"] == categoria:
                quantidade += 1

        print(categoria, ":", quantidade)

def calcular_percentuais():

    total = 0

    for ocorrencia in ocorrencias:
        if validar_ocorrencia(ocorrencia):
            total += 1

    print("\n===== PERCENTUAL POR CATEGORIA =====")

    if total == 0:
        print("Nao existem ocorrencias validas.")
        return

    for categoria in CATEGORIAS:

        quantidade = 0

        for ocorrencia in ocorrencias:

            if validar_ocorrencia(ocorrencia) and ocorrencia["categoria"] == categoria:
                quantidade += 1

        percentual = (quantidade / total) * 100

        print(categoria, ":", round(percentual, 2), "%")

def contar_por_status():

    print("\n===== OCORRENCIAS POR STATUS =====")

    for status in STATUS_VALIDOS:

        quantidade = 0

        for ocorrencia in ocorrencias:

            if validar_ocorrencia(ocorrencia) and ocorrencia["status"] == status:
                quantidade += 1

        print(status, ":", quantidade)

def calcular_percentuais_status():

    total = 0

    for ocorrencia in ocorrencias:
        if validar_ocorrencia(ocorrencia):
            total += 1

    print("\n===== PERCENTUAL POR STATUS =====")

    if total == 0:
        print("Nao existem ocorrencias validas.")
        return

    for status in STATUS_VALIDOS:

        quantidade = 0

        for ocorrencia in ocorrencias:

            if validar_ocorrencia(ocorrencia) and ocorrencia["status"] == status:
                quantidade += 1

        percentual = (quantidade / total) * 100

        print(status, ":", round(percentual, 2), "%")

# ==========================================
# FILA DE ATENDIMENTO (FIFO)
# ==========================================

def criar_fila_atendimento():

    fila = deque()

    for ocorrencia in ocorrencias:

        if validar_ocorrencia(ocorrencia) and ocorrencia["status"] == "Aberta":
            fila.append(ocorrencia["id"])

    return fila


def listar_fila_atendimento():

    fila = criar_fila_atendimento()

    print("\n===== FILA DE ATENDIMENTO =====")

    if not fila:
        print("Nao existem ocorrencias aguardando atendimento.")
        return

    for codigo in fila:
        print("Aguardando atendimento:", codigo)
        
        
# ==========================================
# CADASTRO DE NOVAS OCORRENCIAS
# ==========================================

def cadastrar_ocorrencia(codigo, categoria, descricao, local, data_abertura):

    if not codigo or not categoria or not descricao or not local or not data_abertura:
        print("Erro: todos os campos sao obrigatorios.")
        return

    if categoria not in CATEGORIAS:
        print("Erro: categoria invalida.")
        return

    for ocorrencia in ocorrencias:
        if ocorrencia["id"] == codigo:
            print("Erro: ja existe uma ocorrencia com esse codigo.")
            return

    nova_ocorrencia = {
        "id": codigo,
        "categoria": categoria,
        "descricao": descricao,
        "local": local,
        "data_abertura": data_abertura,
        "status": "Aberta"
    }

    ocorrencias.append(nova_ocorrencia)

    print("Ocorrencia cadastrada com sucesso!")
    print("Codigo:", codigo)
    print("Status inicial: Aberta")


# ==========================================
# PILHA DE ATUALIZACOES (LIFO)
# ==========================================

def listar_ultimas_atualizacoes():
    print("\n===== ULTIMAS ATUALIZACOES =====")

    pilha = []

    for evento in historico:
        pilha.append(evento)

    if not pilha:
        print("Nao existem atualizacoes registradas.")
        return

    while pilha:
        evento = pilha.pop()

        print(
            evento["id_ocorrencia"],
            "-",
            evento["status_anterior"],
            "->",
            evento["novo_status"],
            "-",
            evento["data"]
        )


# ==========================================
# DICIONARIO DE CONSULTA POR ID
# ==========================================

def criar_indice_ocorrencias():
    indice = {}

    for ocorrencia in ocorrencias:
        if validar_ocorrencia(ocorrencia):
            indice[ocorrencia["id"]] = ocorrencia

    return indice 


# ==========================================
# HIERARQUIA DE OCORRENCIAS
# ==========================================

def mostrar_hierarquia():
    bairro = "Bairro Modelo"

    hierarquia = {bairro: {}}

    for categoria in CATEGORIAS:
        hierarquia[bairro][categoria] = []

    for ocorrencia in ocorrencias:
        if validar_ocorrencia(ocorrencia):
            categoria = ocorrencia["categoria"]
            hierarquia[bairro][categoria].append(ocorrencia["id"])

    print("\n===== HIERARQUIA DE OCORRENCIAS =====")
    print("Bairro:", bairro)

    for categoria, codigos in hierarquia[bairro].items():
        print("\nCategoria:", categoria)

        for codigo in codigos:
            print(" -", codigo) 
            
            
# ==========================================
# MATRIZ DE INDICADORES
# ==========================================

def mostrar_matriz_indicadores():

    matriz = []

    for categoria in CATEGORIAS:
        linha = []

        for status in STATUS_VALIDOS:
            quantidade = 0

            for ocorrencia in ocorrencias:
                if (validar_ocorrencia(ocorrencia)
                        and ocorrencia["categoria"] == categoria
                        and ocorrencia["status"] == status):
                    quantidade += 1

            linha.append(quantidade)

        matriz.append(linha)

    print("\n===== MATRIZ DE INDICADORES =====")
    print(f'{"Categoria":<18} {"Aberta":<10} {"Em analise":<12} {"Concluida":<10}')

    for i in range(len(CATEGORIAS)):
        print(f"{CATEGORIAS[i]:<18} {matriz[i][0]:<10} {matriz[i][1]:<12} {matriz[i][2]:<10}")


# ==========================================
# INDICADOR DE PENDENCIAS
# ==========================================

def mostrar_pendencias():

    total_validas = 0
    pendencias = 0

    for ocorrencia in ocorrencias:
        if validar_ocorrencia(ocorrencia):
            total_validas += 1

            if (ocorrencia["status"] == "Aberta"
                    or ocorrencia["status"] == "Em analise"):
                pendencias += 1

    print("\n===== INDICADOR DE PENDENCIAS =====")
    print("Total de ocorrencias validas:", total_validas)
    print("Ocorrencias pendentes:", pendencias)

    if total_validas > 0:
        percentual = (pendencias / total_validas) * 100
        print("Percentual de pendencias:", round(percentual, 2), "%")
    else:
        print("Nao existem ocorrencias validas.")


