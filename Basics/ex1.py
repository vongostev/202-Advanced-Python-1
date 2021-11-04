

def is_even(n: int) -> bool:
    """
    На вход функции is_even подается целое число. Если число четное, то возвращается True, если нет, то False. 
    Проверить работу функции с числами -240, -17, 0, 12, 131. Если число отрицательное, печатается предупреждение.
    """
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # Test is_even()
    assert is_even(-240) is True
    assert is_even(-17) is False
    assert is_even(0) is True
    assert is_even(12) is True
    assert is_even(131) is False

    print("Tests ok")
