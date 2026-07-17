import pytest
from login_utilities import try_login

def test_try_login_with_correct_credentials_return_true():
    # Arrange
    email_input = 'a@gmail'
    password_input = '123'
    # Act
    result = try_login(email_input, password_input)
    # Assert
    assert result

def test_try_login_with_incorrect_credentials_return_true():
    # Arrange
    email_input = 'b@gmail'
    password_input = '323'
    # Act & Assert
    with pytest.raises(ValueError):
        try_login(email_input, password_input)

#Preguntar cual seria la diferencia y mejora entre tenar try & except dentro del codigo a tener un unit testing
#es bueno tener ambos implementados?
