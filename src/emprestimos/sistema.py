from .equipamento import Equipamento
from .reserva import Reserva


class SistemaEmprestimos:
    def __init__(self):
        self._equipamentos: dict[str, Equipamento] = {}
        self._reservas: list[Reserva] = []

    def registar_equipamento(self, equipamento: Equipamento) -> None:
        if not isinstance(equipamento, Equipamento):
            raise TypeError("É necessário fornecer um Equipamento.")
        if equipamento.codigo in self._equipamentos:
            raise ValueError(f"Já existe um equipamento com o código {equipamento.codigo}.")
        self._equipamentos[equipamento.codigo] = equipamento

    def consultar_catalogo(self) -> tuple[Equipamento, ...]:
        return tuple(self._equipamentos.values())

    def obter_equipamento(self, codigo: str) -> Equipamento:
        try:
            return self._equipamentos[codigo]
        except KeyError:
            raise KeyError(f"Equipamento não encontrado: {codigo}") from None

    def reservar(self, reserva: Reserva) -> None:
        if not isinstance(reserva, Reserva):
            raise TypeError("É necessário fornecer uma Reserva.")
        if reserva.codigo_equipamento not in self._equipamentos:
            raise KeyError(f"Equipamento não encontrado: {reserva.codigo_equipamento}")
        for existente in self._reservas:
            if reserva.sobrepoe(existente):
                raise ValueError("Conflito: o equipamento já está reservado nesse período.")
        self._reservas.append(reserva)

    def consultar_reservas(self, codigo_equipamento: str | None = None) -> tuple[Reserva, ...]:
        if codigo_equipamento is None:
            return tuple(self._reservas)
        return tuple(r for r in self._reservas if r.codigo_equipamento == codigo_equipamento)
