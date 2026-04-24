# brinquedoteca_api

O objetivo é desenvolver uma API REST com aquitetura em camadas, focando em raciocínio lógico, modelagem e regras de negócio.

Descrição das responsabilidades de domain, schemas, repositories, services, api/routes, main.py.
Modelos de Domínio

Detalhes das entidades Criança, Brinquedo, Emprestimo, e o fluxo de empréstimos.
Regras de Negócio Implementadas

Lista com as regras, como validações de idade, disponibilidade, limites de empréstimos, conflito de horários, multas e bloqueio.
Endpoints

Lista de endpoints mínimos com verbos, caminhos e propósito.
Persistência

Implementação em memória para fins didáticos. Possibilidade de migrar para SQLite com SQLAlchemy no futuro.
Como rodar

Passos para instalar dependências, rodar a API, e comandos de teste rápido.
Como testar regras de negócio

Exemplos de cenários de teste (empréstimo bem-sucedido, falha por idade, falha por conflito, atraso gerando multa, bloqueio após 3 atrasos).
Observações

Extensões futuras sugeridas (persistência real, autenticação, validações adicionais, endpoints extras como filtro de empréstimos por status, etc.)

