endpoints = ["/login", "produtos/", "/pedidos"]

# Cada linha representa um endpoint
# Cada coluna uma requisição

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 401, 200, 500],
    [200, 200, 401, 201, 500]
]

def sucesso(requisicao):
    return requisicao > 199 and requisicao < 300

def calcular_requisicoes():
    erro_sucessivo_endpoint = 0

    for i, endpoint in enumerate(status):
        endpoint_index = i
        soma_sucesso_endpoint = 0
        soma_erros_endpoint = 0

        for requisicao in endpoint:
            erro_sucessivo_endpoint = 0

            if sucesso(requisicao):
                soma_sucesso_endpoint += 1

            else:
                soma_erros_endpoint += 1
                erro_sucessivo_endpoint += 1

                if erro_sucessivo_endpoint == 2:
                    print(f"O endpoint {endpoint_index + 1} teve dois erros seguidos")
    

calcular_requisicoes()