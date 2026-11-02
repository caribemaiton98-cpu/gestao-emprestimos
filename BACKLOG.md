# BACKLOG — Gestão de Empréstimos de Equipamento Multimédia

## Visão do produto
Gerir o empréstimo de equipamentos multimédia de um laboratório universitário, incluindo catálogo e reservas com prevenção de conflitos.

Este é um backlog inicial de trabalho; confirmar e ajustar às decisões reais da equipa e da docente.

## Iteração 1 — Catálogo e reservas

### US01 — Registar equipamento
Como responsável pelo laboratório, quero registar equipamentos para que possam ser disponibilizados para empréstimo.
- O equipamento tem código, nome e categoria.
- Os campos obrigatórios não podem estar vazios.
- O código é único.
Estado: implementação incluída nesta versão; confirmar aceitação.

### US02 — Consultar catálogo
Como utilizador, quero consultar o catálogo para conhecer os equipamentos registados.
- Consultar a lista de equipamentos.
- Obter um equipamento pelo código.
Estado: implementação incluída nesta versão; confirmar aceitação.

### US03 — Criar reserva
Como estudante, quero reservar um equipamento para um período.
- A reserva identifica equipamento, utilizador, início e fim.
- A data final não pode ser anterior à inicial.
- O equipamento deve existir.
Estado: implementação incluída nesta versão; confirmar aceitação.

### US04 — Evitar conflitos
Como responsável, quero impedir reservas sobrepostas do mesmo equipamento.
- Períodos sobrepostos do mesmo equipamento são rejeitados.
- Períodos não sobrepostos são permitidos.
- Equipamentos diferentes podem ser reservados simultaneamente.
Estado: implementação incluída nesta versão; confirmar aceitação.

## Backlog futuro indicativo
- Levantamento e devolução.
- Atrasos e penalizações, conforme regras definidas pela cliente.
- Histórico por utilizador.
- Integração do módulo da docente.
- Interface e persistência, caso sejam acordadas.
