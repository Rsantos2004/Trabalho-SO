# Trabalho de SO

Desenvolva um programa que processe todos os arquivos de log e contabilize a quantidade de mensagens **INFO**, **WARNING** e **ERROR**.

## Resultado esperado

**Total de arquivos:** 100

```text
INFO:     245.821
WARNING:   69.372
ERROR:     34.851
```

## Versões do programa

1. Processamento sequencial
   - Lê e processa os arquivos um por um, na ordem em que aparecem.
   - É a versão mais simples e serve como referência para comparar o desempenho das outras.

2. Processamento utilizando processos
   - Cria múltiplos processos para processar os arquivos em paralelo.
   - Cada processo trabalha de forma independente, o que pode acelerar a execução em tarefas mais pesadas de CPU.
   - Essa abordagem é útil para comparar o ganho de desempenho ao usar paralelismo em nível de processo.

3. Processamento utilizando threads
   - Usa várias threads dentro do mesmo processo para processar os arquivos simultaneamente.
   - É mais leve que criar processos e pode ser vantajoso em tarefas que envolvem mais espera de I/O, como leitura de arquivos.
   - Essa versão ajuda a observar a diferença entre concorrência com threads e com processos.

O objetivo do trabalho é analisar como cada abordagem impacta o tempo de processamento e também comparar a complexidade e o comportamento de cada técnica em sistemas operacionais.


## Gerar os arquivos

Este projeto foi desenvolvido com Python 3.11.4.

Para gerar os 100 arquivos de log, execute:

```bash
python gerador_arquivos.py
```

Esse script cria a pasta `dados/` e gera todos os arquivos necessários para o processamento.
