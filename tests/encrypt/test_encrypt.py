import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError,  match="tipo inválido para key"):
        encrypt_message('valid', 'invalid')
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(42, 42)
    with pytest.raises(TypeError,  match="tipo inválido para key"):
        encrypt_message(24, 'invalid')
    assert encrypt_message('my_message', 5) == 'em_ym_egass'
    assert encrypt_message('my_message', 4) == 'egasse_m_ym'
    assert encrypt_message('my_message', 17) == 'egassem_ym'
