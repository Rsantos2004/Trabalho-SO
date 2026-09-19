import time
from pathlib import Path



def medir_tempo_execucao(func):
    # decorator que calcula e imprime o tempo de execução de uma função.
    # basta executar a função com o decorator @medir_tempo_execucao acima dela.
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"Tempo de execução ({func.__name__}): {fim - inicio:.4f} segundos")
        return resultado

    return wrapper


def contar_mensagens_arquivo(caminho_do_arquivo):
    """Conta quantas mensagens INFO, WARNING e ERROR há em um único arquivo."""
    contagem = 0

    return contagem


@medir_tempo_execucao
def processar_logs_threads(pasta="dados", max_workers=None):
    """Processa todos os arquivos log em paralelo usando threads."""
    diretorio = Path(pasta)
    arquivos = sorted(diretorio.glob("*.log"))

    print(f"Processando {len(arquivos)} arquivos...")
    
    return 0


def main():

    resultado = processar_logs_threads( max_workers=8)

    print("Resultado do processamento com threads:")



if __name__ == "__main__":
    main()
