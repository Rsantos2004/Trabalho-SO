from multiprocessing import Pool
from pathlib import Path
from collections import Counter
import time 


def medir_tempo_execucao(func):
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"Tempo de execução ({func.__name__}): {fim - inicio:.4f} segundos")
        return resultado

    return wrapper

def contar_mensagens_arquivo(caminho_do_arquivo):
    contagem = Counter()

    with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if "ERROR" in linha:
                contagem["ERROR"] += 1
            elif "WARNING" in linha:
                contagem["WARNING"] += 1
            elif "INFO" in linha:
                contagem["INFO"] += 1

    return contagem

@medir_tempo_execucao
def processar_logs_processos(pasta="dados", processos=None):
    diretorio = Path(pasta)
    arquivos = sorted(diretorio.glob("*.log"))  
    print(f"Processando {len(arquivos)} arquivos...")

    total = Counter()

    with Pool(processes=processos) as pool:
        for contagem in pool.map(contar_mensagens_arquivo, arquivos):
            total.update(contagem)

    return total


def main():
    resultado = processar_logs_processos()

    print("Resultado do processamento com processos:")
    print(f"Total de arquivos: {len(list(Path('dados').glob('*.log')))}")
    print(f"INFO:    {resultado['INFO']:>7}")
    print(f"WARNING: {resultado['WARNING']:>7}")
    print(f"ERROR:   {resultado['ERROR']:>7}")


if __name__ == "__main__":
    main()