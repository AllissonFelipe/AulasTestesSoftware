# Introdução aos Testes de Software

<aside>
👉🏻

*“Não existe sistema sem erros!”*

*-Professor Marcos*

</aside>

## Mulher do BUG

**Grace Hopper**

- Analista de Sistemas (1940 - 1950)
- Inventou o COBOL (primeiro compilador)
- Popularizou o termo “bug” (por causa da mariposa)

![Folha do registro histórico](image.png)

Folha do registro histórico

## Diferenças entre Erro, Defeito, Falha e Exceção

| **Erro** | **Defeito** | **Falha** | **Exceção** |
| --- | --- | --- | --- |
| Causado **pelo desenvolvedor**. | Se materializa na execução. Acontece **em decorrência de um erro**. | É quando o **defeito se manifesta**, e torna-se **visível para o usuário**. | Interrupção no fluxo do programa **causada por um defeito** ou erro inesperado. Pode ser capturada e tratada. |

## Erros que levam a Defeitos

| **Tipo de Erro** | **Exemplo** |
| --- | --- |
| Erro de Sintaxe(caractere errado na linguagem) | `print("word)` |
| Erro Semântico(erro de tipo na variável) | `int idade = "word";` |
| Erro Léxico(erro de caractere inesperado) | `int n**ú**mero = 10;` |
| Erro Lógico(programa roda normal, mas logica errada no programa) | `int soma = a - b;` |
| Erro de Runtime(erro enquanto o programa está em execução. Ex: loop infinito) | `while (true) {var++;}` |
| Erro de Referência(referindo à algum atributo inexistente) | `print(textoInexistente.lenght());` |

## Padronização

*ISO (International Organization for Standardization)*

*IEC (International Electrotechnical Comission)*

- Normas ISO/IEC 29119 - Define um padrão geral de como executar o seu teste (preparação de ambiente)
- Normas ISO/IEC 2126 - Sobre qualidade de software
- Normas ISO/IEC - IEEE 829 - Gestão de documentos para testes de software.
- Normas ISO/IEC 15504 - SPICE - Busca estabelecer padrões de como testar softwares. Amplia a primeira para os negócios, uma modernização.

## Fases dos testes

### Planejamento

- Planejar de fato

### Criação de casos de teste

- Especificar cenários de testes
- Definir entradas e saídas esperadas

### Preparação do ambiente

- Preparar o ambiente de hardware e software

### Execução de testes

- Realizar os testes(Manuais e (ou) automáticos

### Correção de defeitos

- Análise e correção para cada situação encontrada

### Reteste

- Fazer o reteste para reavaliar o software (possíveis novos erros)

### Documentação

- Gerar relatórios de acompanhamento de processo

## Tipos de Testes

- **1. Manuais**
    - Realizados por testador humano
    - Necessários para interação humana complexa
    - Mapeamento das funcionalidades
- **2. Automatizados**
    - Executados via scripts
    - Para testes repetitivos
    - Usando frameworks ou scripts próprios
- **3. Funcionais**
    - Validam funcionalidades específicas
    - Testes de Unidade: componentes individuais
    - Testes de Integração: interação entre componentes
    - Testes de Sistema: software completo
    - Testes de Aceitação: validação com cliente
- **4. Não Funcionais**
    - Desempenho: velocidade, carga , stress, etc
    - Segurança: vulnerabilidades
    - Usabilidade: experiência do usuário
    - Compatibilidade: diferentes plataformas

## Documentação de testes

### Plano de teste

- Nome do projeto
- Pessoas envolvidas
- Funcionalidades ou Módulos
- Equipamentos / Softwares
- Cronograma
- Local dos Testes
- Critérios de Sucesso

## Victor Anotações

- **Aula 22/04/2025.**
    
    [gostosas.com.br](http://gostosas.com.br) (estudar depois).
    
    Funcional seria um carro, não funcional seria o carro que consome menos gasolina.
    
    [https://www.reddit.com/r/PedroDBR/comments/10l3lpd/carlinhos/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button](https://www.reddit.com/r/PedroDBR/comments/10l3lpd/carlinhos/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
    

## Q.A. (Quality Assurance)

- Prevenir problemas desde o início
- Uma função a se seguir carreira

## Programa Bug Bounty

- Programa usado para caçar bugs! Oferecido pelas empresas.
- Bounty se refere à recompensa! Ganha se achar!
- [https://www.hackerone.com/](https://www.hackerone.com/)
