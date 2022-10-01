import pytest
from main import check_password
from main import check_email
from main import check_password_equal
from main import check_credentials


def email_test1():
    email = "test@gmail.com"
    assert check_email(email) is True


def email_test2():
    email = "test_site.com"
    assert check_email(email) is True


def email_test3():
    email = "test1234@gmail.com"
    assert check_email(email) is False


def test_check_password1():
    password = "Qwert1234"
    assert check_password(password) is True


def test_check_password2():
    password = "qwert"
    assert check_password(password) is False


def test_check_password3():
    password = "QWERT55"
    assert check_password(password) is False


def test_check_password4():
    password = "Qwerty"
    assert check_password(password) is False


def test_check_password5():
    password = "551234"
    assert check_password(password) is False


def test_check_password6():
    password = "Qwerty$£@55"
    assert check_password(password) is True


def test_check_password7():
    password = "Qwerty$£@"
    assert check_password(password) is False


def test_check_password8():
    password = "Qwert5@"
    assert check_password(password) is True


def test_password_equal1():
    password1 = "Qwert1234"
    password2 = "Qwert1234"
    assert check_password_equal(password1, password2) is True


def test_password_equal2():
    password1 = "Qwert1234"
    password2 = "Qwert1234"
    assert check_password_equal(password1, password2) is True


def test_password_equal3():
    password1 = "Qwert1234"
    password2 = "Qwert234"
    assert check_password_equal(password1, password2) is False


def test_check_credentials1():
    password1 = "Qwert1234"
    password2 = "Qwert1234"
    email = "test@gmail.com"
    assert (check_password_equal(password1, password2)
            and check_email(email)) is True


def test_check_credentials2():
    password1 = "Qwert1234"
    password2 = "Qwert234"
    email = "test@gmail.com"
    assert (check_password_equal(password1, password2)
            and check_email(email)) is False


def test_check_credentials3():
    password1 = "Qwert1234"
    password2 = "Qwert1234"
    email = "test1234@gmail.com"
    assert (check_password_equal(password1, password2)
            and check_email(email)) is False
