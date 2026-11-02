# BACKLOG — Gestão de Empréstimos de Equipamento Multimédia

## Visão do produto

Gerir o empréstimo de equipamentos multimédia de um laboratório universitário, incluindo o catálogo de equipamentos e a gestão de reservas com prevenção de conflitos.

## Iteração 1 — Catálogo e reservas

### US01 — Registar equipamento

Como responsável pelo laboratório, quero registar equipamentos para que possam ser disponibilizados para empréstimo.

Critérios de aceitação:

* O equipamento tem código, nome e categoria.
* Os campos obrigatórios não podem estar vazios.
* O código é único.

Estado: Implementado e coberto por testes automatizados.

### US02 — Consultar catálogo

Como utilizador, quero consultar o catálogo para conhecer os equipamentos registados.

Critérios de aceitação:

* Consultar a lista de equipamentos.
* Obter um equipamento pelo código.

Estado: Implementado e coberto por testes automatizados.

### US03 — Criar reserva

Como estudante, quero reservar um equipamento para um período.

Critérios de aceitação:

* A reserva identifica equipamento, utilizador, início e fim.
* A data final não pode ser anterior à inicial.
* O equipamento deve existir.

Estado: Implementado e coberto por testes automatizados.

### US04 — Evitar conflitos

Como responsável, quero impedir reservas sobrepostas do mesmo equipamento.

Critérios de aceitação:

* Períodos sobrepostos do mesmo equipamento são rejeitados.
* Períodos não sobrepostos são permitidos.
* Equipamentos diferentes podem ser reservados simultaneamente.

Estado: Implementado e coberto por testes automatizados.

## Backlog futuro indicativo

As seguintes funcionalidades ficam para iterações futuras, conforme a prioridade e as regras a definir:

* Levantamento e devolução de equipamentos.
* Gestão de atrasos e penalizações.
* Histórico de empréstimos por utilizador.
* Integração do módulo da docente.
* Interface de utilizador e persistência de dados, caso sejam acordadas.
