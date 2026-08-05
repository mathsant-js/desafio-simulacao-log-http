endpoints: list[str] = ["/login", "/produtos", "/pedidos"]

# Cada linha representa um endpoint
# Cada coluna uma requisição

status: list[list[int]] = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [200, 500, 502, 201, 500]
]

erros_endpoints: list[int] = [0 * tamanho for tamanho in range(len(endpoints))]

def sucesso(requisicao: int) -> bool:
    """Calcula se uma requisição foi bem sucedida

    Args:
        requisicao (int): requisição de um endpoint

    Returns:
        bool: Verdadeiro para requisição bem sucedida
    """
    
    return requisicao > 199 and requisicao < 300

def get_index_mais_erros() -> int:
    """Captura o index do endpoint com mais erros

    Returns:
        int: index do endpoint com mais erros
    """
    
    index_maior_valor_erros: int = 0

    for i in range(len(erros_endpoints)):
        maior_valor = erros_endpoints[0]

        if erros_endpoints[i] > maior_valor:
            maior_valor = erros_endpoints[i]
            index_maior_valor_erros = i

    return index_maior_valor_erros

def calcular_porcentagem_sucesso(sucessos: int, index: int) -> float:
    """Calcula a porcentagem de sucesso das requisições bem sucedidas do endpoint

    Args:
        sucessos (int): quantidade de requisições bem sucedidas de um endpoint
        index (int): index do endpoint

    Returns:
        float: porcentagem de requisições bem sucedidas de um endpoint
    """
    
    return (sucessos * 100) / len(status[index]) 

def exibir_classificacao_endpoint(porcentagem_sucesso: float, erro_sucessivo: int) -> str:
    """Calcula e retorna a classificação do endpoint

    Args:
        porcentagem_sucesso (float): porcentagem de sucesso das requisições do endpoint
        erro_sucessivo (int): quantidade de erros sucessivos

    Returns:
        str: classificação baseada na quantidade de erros e porcentagem de sucesso
    """
    
    if erro_sucessivo >= 2:
        return "CRÍTICO"
    
    if porcentagem_sucesso > 80:
        return "ESTÁVEL"
    
    return "INSTÁVEL"

def percorrer_requisicoes() -> None:
    """Percorre as requisições dos endpoints"""
    
    erro_sucessivo_endpoint: int = 0

    print()
    print("==== LOG ENDPOINTS ====")

    for endpoint_index, endpoint in enumerate(status):
        print(f"ENDPOINT '{endpoints[endpoint_index]}'")
        
        erro_sucessivo_endpoint: int = 0
        soma_sucesso_endpoint: int = 0
        soma_erros_endpoint: int = 0

        for requisicao in endpoint:
            
            if sucesso(requisicao):
                soma_sucesso_endpoint += 1

            else:
                soma_erros_endpoint += 1
                erro_sucessivo_endpoint += 1

                erros_endpoints[endpoint_index] = soma_erros_endpoint

        print(f"Erros: {soma_erros_endpoint}")

        if erro_sucessivo_endpoint >= 2:
            print("Erros consecutivos: SIM")
        else:
            print("Erros consecutivos: NÃO")

        porcentagem_sucesso: float = calcular_porcentagem_sucesso(soma_sucesso_endpoint, endpoint_index)

        print(f"Porcentagem de sucesso: {porcentagem_sucesso}%")
        print(f"Classificação do Endpoint: {exibir_classificacao_endpoint(porcentagem_sucesso, erro_sucessivo_endpoint)}")
        print()

    print("==== ENDPOINT COM MAIS ERROS ====")
    print(f"ENDPOINT: '{endpoints[get_index_mais_erros()]}'")
    print(f"Quantidade de erros: {max(erros_endpoints)}")
    print()

percorrer_requisicoes()