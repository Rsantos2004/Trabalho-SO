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


## Passo a passo do trabalho

1. Clone o repositório para sua máquina local.
2. Verifique se há uma versão do Python 3 instalada e disponível no terminal.
3. Abra os arquivos principais do projeto e entenda a estrutura do código, como `gerador_arquivos.py`, `process.py` e `threads.py`.
4. Edite os arquivos iniciais conforme a lógica do programa, definindo como os logs serão lidos e processados.
5. Gere os arquivos de log com o comando abaixo:

```bash
python gerador_arquivos.py
```

6. Confirme que a pasta `dados/` foi criada e que os 100 arquivos foram gerados corretamente.
7. Implemente a versão sequencial para contar as mensagens `INFO`, `WARNING` e `ERROR`.
8. Implemente a versão utilizando processos e execute-a para comparar o tempo de processamento.
9. Implemente a versão utilizando threads e execute-a também para analisar o desempenho.
10. Registre os tempos de execução de cada uma das versões em uma tabela ou seção do README.
11. Compare os resultados e identifique qual abordagem foi mais rápida e por quê.
12. Atualize o README com a descrição do projeto, instruções de execução, resultados obtidos e as conclusões finais.

## Gerar os arquivos

O projeto foi testado com Python 3.11.4, mas, em geral, versões do Python 3 também devem funcionar corretamente, desde que o ambiente tenha as bibliotecas padrão necessárias.

Para gerar os 100 arquivos de log, execute:

```bash
python gerador_arquivos.py
```

Esse script cria a pasta `dados/` e gera todos os arquivos necessários para o processamento.


