# Star Wars Knowledge Engine (Prolog)

Este projeto utiliza **Lógica de Primeira Ordem (Prolog)** para modelar e analisar dados do universo Star Wars. A base de conhecimento relaciona **personagens, espécies e planetas**, permitindo responder perguntas complexas por meio de inferência lógica e agregação de dados.

---

## Modelagem

A base foi construída a partir de três principais predicados:

- personagem(Nome, Especie, Planeta)
- especie(Nome, Classificacao, VidaMedia)
- planeta(Nome, Populacao)

### Observações:
- Valores unknown representam informação desconhecida, não entidades reais.
- Algumas queries ignoram esses valores para manter a consistência lógica.

---

##  Perguntas implementadas

### 1️ - Planetas com mais mamíferos

Conta quantos personagens pertencem a espécies classificadas como mammal em cada planeta.

- Utiliza filtragem e agregação (findall, length)
- Considera apenas planetas conhecidos

Exemplo:

```prolog
?- planetas_empatados_mamiferos(Planetas, Total).
```

Saída:

```prolog
Planetas = [tatooine, corellia],
Total = 5.
```

### 2 - Planetas com maior diversidade de espécies

Conta quantas espécies distintas existem em cada planeta.

- Utiliza `setof` para remover duplicatas  
- Mede diversidade biológica por planeta  

Exemplo:

```prolog
?- planetas_empatados_especies(Planetas, Total).
```

Saída:

```prolog
Planetas = [tatooine],
Total = 4.
```
### 3 - Planetas com maior expectativa de vida média

Calcula a média do `average_lifespan` das espécies presentes em cada planeta.

- Média calculada por espécie distinta
- Utiliza agregação e cálculo numérico (`sum_list`, `length`, `is`)  

Exemplo:

```prolog
?- planetas_maior_media_lifespan(Planetas, Media).
```

Saída:

```prolog
Planetas = [kashyyyk],
Media = 400.0.
```

---

## Como executar

1. Abra o Prolog (ex: SWI-Prolog)

2. Carregue o arquivo:

```bash
swipl starwars.pl
```

3. Execute as queries:

```prolog
?- planetas_empatados_mamiferos(P, T).
?- planetas_empatados_especies(P, T).
?- planetas_maior_media_lifespan(P, T).
```

### Fonte dos dados

Os dados utilizados foram extraídos de um único dataset do universo Star Wars.

Apesar de estarem organizados em arquivos separados (`characters`, `species` e `planets`), todos fazem parte da mesma base original e foram utilizados de forma integrada para enriquecer a modelagem e permitir consultas mais expressivas.

Foram selecionados apenas 8 atributos relevantes, combinando variáveis qualitativas (nome, espécie, planeta, classificação) e quantitativas (população e expectativa de vida), atendendo ao requisito do projeto.
