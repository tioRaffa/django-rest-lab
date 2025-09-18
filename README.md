# Estudo Aprofundado em API com Django REST Framework

## Visão Geral
Este projeto foi concebido como uma plataforma de aprendizado prático e aprofundado em Django e Django REST Framework (DRF). Em vez de focar em um único domínio, ele é composto por múltiplos aplicativos (`apps`), onde cada um serve como um caso de uso para explorar diferentes conceitos e desafios no desenvolvimento de APIs. 

O objetivo central é solidificar o conhecimento em temas como a construção de views personalizadas, consumo de APIs de terceiros, modelagem de dados complexa, serialização avançada e tratamento de erros, utilizando cada app como um laboratório para uma funcionalidade específica.

## Objetivos de Estudo e Implementação
O código foi estruturado para servir como um exemplo prático dos seguintes conceitos:

- **Implementação de Views com `APIView`**: O projeto utiliza `APIView` de forma consistente em vez de `ModelViewSet` ou `Generic Views`. Essa escolha foi deliberada para obter controle total sobre a lógica de cada endpoint, permitindo a implementação de fluxos complexos, como o enriquecimento de dados a partir de APIs externas antes de salvar no banco de dados.

- **Consumo de APIs Externas**: Os apps `movies_app`, `google_books_app`, `currency_app` e `weather_app` demonstram como interagir com APIs de terceiros. A lógica de requisição, tratamento de erros e processamento dos dados de resposta está claramente implementada.

- **Modelagem de Dados Complexa**: O `movies_app` e o `google_books_app` são exemplos de modelagem com relacionamentos `ManyToManyField` (para gêneros, atores, diretores) e `ForeignKey`, refletindo estruturas de dados do mundo real.

- **Serialização Avançada (Nested Serializers)**: Para fornecer uma representação rica dos dados, foram implementados serializers aninhados. O `MoviesSerializer`, por exemplo, exibe os detalhes completos de diretores, elenco e gêneros em uma única resposta JSON. A lógica de escrita (criação e atualização) é tratada de forma customizada nos métodos `.create()` e `.update()` dos serializers para gerenciar os relacionamentos complexos.

- **Tratamento de Exceções e Validação**: O projeto inclui tratamento para diferentes cenários de erro, como IDs não encontrados, falhas na comunicação com APIs externas e erros de validação de dados de entrada, retornando respostas claras para o cliente da API.

### Destaques da Implementação

- **Consumo de API Externa**: Nos apps `movies_app` e `google_books_app`, o processo de cadastro (`POST`) é um fluxo de trabalho orquestrado: 
  1. O cliente envia um ID externo (ex: `tmdb_id` ou `google_book_id`).
  2. A `APIView` valida a existência desse ID no banco de dados para evitar duplicatas.
  3. Um módulo de serviço (`service` ou `api`) é chamado para buscar os dados detalhados na API externa (TMDB ou Google Books).
  4. Os dados recebidos são pré-processados e formatados para se alinharem à estrutura do `Serializer`.
  5. O `Serializer` é instanciado com os dados formatados, validado e, por fim, o método `.save()` orquestra a criação do objeto principal e de todos os seus objetos relacionados (atores, diretores, etc.).

- **Modelagem de Dados**: A estrutura do `movies_app` é um bom exemplo de normalização. Em vez de armazenar nomes de diretores ou gêneros como texto simples no modelo do filme, eles são mantidos em tabelas separadas (`DirectorModel`, `Gender`) e conectados via `ManyToManyField`. Isso evita redundância e torna as consultas mais eficientes.

- **Serialização Avançada**: O `MoviesSerializer` e o `BookSerializer` demonstram uma abordagem comum e poderosa no DRF: usar serializers aninhados para leitura (`GET`) e campos como `PrimaryKeyRelatedField` para escrita (`POST`, `PATCH`). Isso permite que o cliente envie apenas os IDs dos objetos relacionados ao criar ou atualizar um recurso, enquanto a resposta da API continua sendo rica e detalhada.

---

## Estrutura do Projeto
Cada app no projeto foi desenvolvido para ser um módulo independente, focado em um conjunto de funcionalidades ou em um objetivo de estudo específico.

### Detalhes do App: `movies_app`
- **Propósito**: Principal app de estudo. Demonstra a integração com uma API externa (TMDB), modelagem complexa e serialização aninhada.
- **Lógica**: Permite buscar, listar e cadastrar filmes. O cadastro é feito a partir de um `tmdb_id`, automatizando a população de dados no banco de dados local. Os modelos `MoviesModels`, `DirectorModel`, `AuthorModel`, `Gender`, entre outros, são interligados para criar um esquema de dados robusto. O `MoviesSerializer` gerencia a complexidade de criar e atualizar esses múltiplos objetos de uma só vez.

### Detalhes do App: `google_books_app`
- **Propósito**: Similar ao `movies_app`, serve como um segundo exemplo complexo de consumo de API (Google Books) e serialização.
- **Lógica**: A funcionalidade é quase idêntica à do `movies_app`, reforçando o padrão de design utilizado. Ele possui seus próprios modelos (`BookModel`, `AuthorModel`, `CategoryModel`) e um `BookSerializer` que lida com a criação de livros e seus autores/categorias associados.

### Detalhes do App: `book`, `contatos`, `cursos`, `ToDoList`
- **Propósito**: Servir como exemplos de APIs de CRUD (Create, Read, Update, Delete) mais tradicionais.
- **Lógica**: Cada um desses apps implementa `APIView`s para fornecer endpoints para operações básicas. O app `cursos`, por exemplo, demonstra um relacionamento `ForeignKey` simples entre `Course` e `Avaliação`.

### Detalhes do App: `currency_app` e `weather_app`
- **Propósito**: Exemplos mínimos e focados de consumo de API externa sem persistência de dados.
- **Lógica**: Cada app expõe um único endpoint `GET`. Eles recebem parâmetros de consulta (como cidade ou moedas), fazem uma chamada a uma API externa, e retornam a resposta diretamente ao cliente, sem interagir com o banco de dados.

## Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **django-phonenumber-field**: Para validação e formatação de números de telefone.
- **requests**: Biblioteca padrão para realizar as chamadas HTTP às APIs externas.
- **python-decouple**: Para gerenciar chaves de API e outras configurações sensíveis de forma segura.