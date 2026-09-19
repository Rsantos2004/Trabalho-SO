import os
import random
from datetime import datetime, timedelta

PASTA = "dados"

QUANTIDADE_ARQUIVOS = 100
LINHAS_MIN = 1000
LINHAS_MAX = 5000

NIVEIS = ["INFO", "WARNING", "ERROR"]

MENSAGENS = {
    "INFO": [
        "Usuario conectado",
        "Usuario desconectado",
        "Login realizado com sucesso",
        "Arquivo recebido",
        "Arquivo processado",
        "Requisicao recebida",
        "Requisicao concluida",
        "Sessao iniciada",
        "Sessao encerrada",
        "Operacao realizada com sucesso"
    ],

    "WARNING": [
        "Memoria acima de 80%",
        "Conexao lenta",
        "Tentativa de acesso repetida",
        "Espaco em disco abaixo de 20%",
        "Tempo de resposta elevado",
        "Numero elevado de requisicoes"
    ],

    "ERROR": [
        "Falha ao acessar banco",
        "Arquivo nao encontrado",
        "Conexao com banco perdida",
        "Erro ao processar requisicao",
        "Falha de autenticacao",
        "Erro interno do servidor",
        "Falha ao gravar arquivo"
    ]
}


def gerar_linha(data):
    nivel = random.choices(
        NIVEIS,
        weights=[70, 20, 10]
    )[0]

    mensagem = random.choice(MENSAGENS[nivel])

    data_formatada = data.strftime("%Y-%m-%d %H:%M:%S")

    return f"{data_formatada} {nivel} {mensagem}\n"


def gerar_arquivo(numero):
    nome = f"servidor_{numero:03d}.log"
    caminho = os.path.join(PASTA, nome)

    quantidade_linhas = random.randint(
        LINHAS_MIN,
        LINHAS_MAX
    )

    data = datetime(2026, 1, 1)

    with open(caminho, "w", encoding="utf-8") as arquivo:

        for _ in range(quantidade_linhas):
            arquivo.write(gerar_linha(data))

            # Avança alguns segundos
            data += timedelta(
                seconds=random.randint(1, 30)
            )

    return nome, quantidade_linhas


def main():

    os.makedirs(PASTA, exist_ok=True)

    print("Gerando arquivos...\n")

    total_linhas = 0

    for i in range(1, QUANTIDADE_ARQUIVOS + 1):

        nome, linhas = gerar_arquivo(i)

        total_linhas += linhas

        print(
            f"{nome} -> {linhas} linhas"
        )

    print("\nGeracao concluida!")
    print(f"Arquivos: {QUANTIDADE_ARQUIVOS}")
    print(f"Total de linhas: {total_linhas}")


if __name__ == "__main__":
    main()