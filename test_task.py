from task import task
import pytest

def test_task(monkeypatch):
    test_data = ["Geoff", "Computer Science", 75]
    inputs = iter(test_data)

    # Monkeypatch input to simulate user inputs
    monkeypatch.setattr("builtins.input", lambda *args: next(inputs))

    # Test the task function and assert the result
    assert task() == (test_data[0], test_data[1], test_data[2])
