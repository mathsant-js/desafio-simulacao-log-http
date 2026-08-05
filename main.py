endpoints = ["/login", "/produtos", "/pedidos"]

# Cada linha representa um endpoint
# Cada coluna uma requisição

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [200, 500, 502, 201, 500]
]

erros_endpoints = [0 * tamanho for tamanho in range(len(endpoints))]

def sucesso(requisicao):
    return requisicao > 199 and requisicao < 300

def maior_valor_erros():
    return max(erros_endpoints)

def get_index_mais_erros():
    index_maior_valor_erros = 0


    for i in range(len(erros_endpoints)):
        maior_valor = erros_endpoints[0]

        if erros_endpoints[i] > maior_valor:
            maior_valor = erros_endpoints[i]
            index_maior_valor_erros = i

    return index_maior_valor_erros

def calcular_porcentagem_sucesso(sucessos, index):
    return (sucessos * 100) / len(status[index]) 

def calcular_requisicoes():
    erro_sucessivo_endpoint = 0
    porcentagem_sucesso = 0

    for endpoint_index, endpoint in enumerate(status):
        erro_sucessivo_endpoint = 0

        for requisicao in endpoint:
            soma_sucesso_endpoint = 0
            soma_erros_endpoint = 0

            if sucesso(requisicao):
                soma_sucesso_endpoint += 1

            else:
                soma_erros_endpoint += 1
                erro_sucessivo_endpoint += 1

                erros_endpoints[endpoint_index] += soma_erros_endpoint

                if erro_sucessivo_endpoint == 2:
                    print(f"O endpoint {endpoints[endpoint_index]} teve dois erros seguidos")

            porcentagem_sucesso = calcular_porcentagem_sucesso(soma_sucesso_endpoint, endpoint_index)

        print(f"Porcentagem de sucesso do endpoint: {endpoints[endpoint_index]}")
        print(f"{porcentagem_sucesso}%")

    print(f"O endpoint com mais erros é o {endpoints[get_index_mais_erros()]}")

calcular_requisicoes()