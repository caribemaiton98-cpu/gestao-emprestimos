import pytest
from emprestimos import Equipamento, SistemaEmprestimos


def test_criar_equipamento_com_dados():
    equipamento = Equipamento("CAM001", "Câmara Canon", "Câmara")
    assert equipamento.codigo == "CAM001"
    assert equipamento.nome == "Câmara Canon"
    assert equipamento.categoria == "Câmara"


@pytest.mark.parametrize("dados", [
    ("", "Câmara", "Câmara"),
    ("CAM1", "", "Câmara"),
    ("CAM1", "Câmara", ""),
])
def test_equipamento_rejeita_campos_vazios(dados):
    with pytest.raises(ValueError):
        Equipamento(*dados)


def test_registar_e_consultar_catalogo():
    sistema = SistemaEmprestimos()
    camera = Equipamento("CAM001", "Câmara Canon", "Câmara")
    sistema.registar_equipamento(camera)
    assert sistema.consultar_catalogo() == (camera,)


def test_nao_permite_codigo_duplicado():
    sistema = SistemaEmprestimos()
    sistema.registar_equipamento(Equipamento("CAM001", "Câmara Canon", "Câmara"))
    with pytest.raises(ValueError, match="Já existe"):
        sistema.registar_equipamento(Equipamento("CAM001", "Outra câmara", "Câmara"))
