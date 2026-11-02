# Gestão de Empréstimos de Equipamento Multimédia

Núcleo de domínio em Python para um projeto académico de gestão de equipamentos multimédia.

## Funcionalidades desta versão
- Registo de equipamentos com código único, nome e categoria.
- Consulta do catálogo.
- Reservas com datas válidas.
- Prevenção de sobreposição de reservas do mesmo equipamento.
- Reservas simultâneas de equipamentos diferentes.
- Consulta das reservas.

Esta versão ainda não inclui interface web, base de dados persistente, levantamento/devolução, penalizações nem integração do módulo da docente.

## Preparação (Windows / PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate
python -m pip install -e ".[dev]"
python -m pytest -v
```

## Estrutura
- `src/emprestimos/`: código do domínio.
- `tests/`: testes automatizados.
- `BACKLOG.md`: backlog inicial.
- `docs/retro-1.md`: modelo a completar com factos reais.
- `docs/declaracao-IA-anexo-II.md`: rascunho para conferir com o Anexo II oficial.

Importante: os commits e o rasto de TDD devem corresponder ao processo realmente seguido. Não apresentem um commit posterior como se o teste tivesse sido escrito antes do código.
