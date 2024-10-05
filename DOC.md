# Banking Dashboard Developer Test

## Architectural Design

The architectural design is based on best practices for organizing FastAPI applications in a modular and scalable structure, but adapted for smaller projects and without databases.


## FastAPI

FastAPI é o framework utilizado para construir a API. A arquitetura é assíncrona, o que otimiza o desempenho em operações de I/O, como chamadas externas para outras APIs. A API oferece endpoints organizados em módulos, o que facilita a adição de novas funcionalidades.

## Redis

Redis é utilizado como uma camada de cache em memória para o armazenamento temporário de tokens de autenticação como tokens JWT, com tempos de expiração pré-definidos, aumentando a segurança.

## Docker

Docker é utilizado para containerizar toda a aplicação, garantindo portabilidade e consistência entre os ambientes de desenvolvimento e produção. O projeto também usa Docker Compose para gerenciar múltiplos contêineres, permitindo que a aplicação FastAPI e Redis sejam executados em contêineres isolados..

## Como Rodar o Projeto:

1- Clone o repositório.

2- Execute `docker-compose up --build` para iniciar a aplicação e o Redis.
Acesse a API e a documentação automática no endereço http://localhost:8000/docs.
