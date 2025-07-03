import pytest

from src.decorators import log  # Укажите правильный путь к модулю с декоратором


def test_log_success(capsys):
    @log()
    def test_func():
        return "success"

    test_func()
    captured = capsys.readouterr()
    assert captured.out == "test_func ok\n"


def test_log_error(capsys):
    @log()
    def test_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        test_func()

    captured = capsys.readouterr()
    assert "test_func error: ValueError. Inputs: (), {}" in captured.out


def test_log_file(tmp_path, capsys):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def test_func():
        return "success"

    test_func()
    with open(log_file) as f:
        content = f.read()
    assert content == "test_func ok\n"
