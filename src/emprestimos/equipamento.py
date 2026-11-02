from dataclasses import dataclass


@dataclass(frozen=True)
class Equipamento:
    codigo: str
    nome: str
    categoria: str

    def __post_init__(self):
        for campo, valor in (
            ("código", self.codigo),
            ("nome", self.nome),
            ("categoria", self.categoria),
        ):
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(f"O {campo} não pode estar vazio.")
