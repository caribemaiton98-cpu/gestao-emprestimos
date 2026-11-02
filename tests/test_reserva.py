from datetime import date
import pytest
from emprestimos import Equipamento, Reserva, SistemaEmprestimos


def preparar_sistema():
    sistema = SistemaEmprestimos()
    sistema.registar_equipamento(Equipamento("CAM001", "Câmara Canon", "Câmara"))
    sistema.registar_equipamento(Equipamento("MIC001", "Microfone", "Áudio"))
    return sistema


def test_criar_reserva_com_datas_validas():
    reserva = Reserva("CAM001", "aluno1", date(2026, 11, 3), date(2026, 11, 5))
    assert reserva.data_inicio == date(2026, 11, 3)
    assert reserva.data_fim == date(2026, 11, 5)


def test_reserva_rejeita_data_fim_anterior():
    with pytest.raises(ValueError, match="anterior"):
        Reserva("CAM001", "aluno1", date(2026, 11, 5), date(2026, 11, 3))


def test_reserva_rejeita_utilizador_vazio():
    with pytest.raises(ValueError, match="utilizador"):
        Reserva("CAM001", " ", date(2026, 11, 3), date(2026, 11, 5))


def test_reservar_e_consultar():
    sistema = preparar_sistema()
    reserva = Reserva("CAM001", "aluno1", date(2026, 11, 3), date(2026, 11, 5))
    sistema.reservar(reserva)
    assert sistema.consultar_reservas() == (reserva,)


def test_nao_reserva_equipamento_inexistente():
    sistema = preparar_sistema()
    reserva = Reserva("XYZ", "aluno1", date(2026, 11, 3), date(2026, 11, 5))
    with pytest.raises(KeyError, match="não encontrado"):
        sistema.reservar(reserva)


def test_impede_reservas_sobrepostas_no_mesmo_equipamento():
    sistema = preparar_sistema()
    sistema.reservar(Reserva("CAM001", "aluno1", date(2026, 11, 3), date(2026, 11, 5)))
    conflito = Reserva("CAM001", "aluno2", date(2026, 11, 5), date(2026, 11, 7))
    with pytest.raises(ValueError, match="Conflito"):
        sistema.reservar(conflito)


def test_permite_reservas_no_mesmo_periodo_para_equipamentos_diferentes():
    sistema = preparar_sistema()
    sistema.reservar(Reserva("CAM001", "aluno1", date(2026, 11, 3), date(2026, 11, 5)))
    outra = Reserva("MIC001", "aluno2", date(2026, 11, 3), date(2026, 11, 5))
    sistema.reservar(outra)
    assert outra in sistema.consultar_reservas()


def test_permite_reservas_sem_sobreposicao():
    sistema = preparar_sistema()
    sistema.reservar(Reserva("CAM001", "aluno1", date(2026, 11, 3), date(2026, 11, 5)))
    seguinte = Reserva("CAM001", "aluno2", date(2026, 11, 6), date(2026, 11, 8))
    sistema.reservar(seguinte)
    assert len(sistema.consultar_reservas("CAM001")) == 2
