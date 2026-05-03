# 🌌 Star Wars Knowledge Engine (Prolog)

Este projeto utiliza **Lógica de Primeira Ordem (Prolog)** para modelar e analisar dados do universo Star Wars. A base de conhecimento relaciona **personagens, espécies e planetas**, permitindo responder perguntas complexas por meio de inferência lógica e agregação de dados.

---

## 🧠 Modelagem

A base foi construída a partir de três principais predicados:

- personagem(Nome, Especie, Planeta)
- especie(Nome, Classificacao, Lifespan)
- planeta(Nome, Populacao)

### 📌 Observações:
- Valores unknown representam informação desconhecida, não entidades reais.
- Algumas queries ignoram esses valores para manter a consistência lógica.

---

## ❓ Perguntas implementadas

### 1️⃣ Planetas com mais mamíferos

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

### 2️⃣ Planetas com maior diversidade de espécies

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
### 3️⃣ Planetas com maior expectativa de vida média

Calcula a média do `average_lifespan` das espécies presentes em cada planeta.

- Média calculada por espécie distinta, evitando viés por quantidade de personagens  
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

## ⚙️ Como executar

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

--- 

## 🧩 Decisões de projeto

- Utilização de `unknown` para representar ausência de informação, em vez de criar entidades artificiais  
- Filtragem de dados desconhecidos diretamente nas queries (ex: `Planeta \= unknown`)  
- Uso de agregações (`findall`, `setof`) para contagem e análise de dados  
- Remoção de duplicatas com `setof` e `sort` para garantir resultados corretos  
- Cálculo de média baseado em espécies distintas, evitando viés causado pela quantidade de personagens  
- Reutilização de predicados auxiliares (ex: `especie_no_planeta`) para manter o código modular e organizado  

---

## 🚀 Conclusão

Este projeto demonstra como a Lógica de Primeira Ordem pode ser utilizada para modelar conhecimento estruturado e realizar inferências sobre dados inter-relacionados.

A partir de uma base contendo personagens, espécies e planetas do universo Star Wars, foi possível construir queries capazes de responder perguntas não triviais envolvendo agregação, comparação e cálculo.

As soluções implementadas exploram conceitos importantes como reutilização de predicados, filtragem de dados e remoção de duplicatas, mostrando na prática o poder da programação lógica na análise de dados.