from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Reserva:
    codigo_equipamento: str
    utilizador: str
    data_inicio: date
    data_fim: date

    def __post_init__(self):
        if not isinstance(self.codigo_equipamento, str) or not self.codigo_equipamento.strip():
            raise ValueError("O código do equipamento não pode estar vazio.")
        if not isinstance(self.utilizador, str) or not self.utilizador.strip():
            raise ValueError("O utilizador não pode estar vazio.")
        if not isinstance(self.data_inicio, date) or not isinstance(self.data_fim, date):
            raise TypeError("As datas da reserva devem ser objetos date.")
        if self.data_fim < self.data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")

    def sobrepoe(self, outra: "Reserva") -> bool:
        return (
            self.codigo_equipamento == outra.codigo_equipamento
            and self.data_inicio <= outra.data_fim
            and outra.data_inicio <= self.data_fim
        )
