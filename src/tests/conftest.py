import pytest
from PyQt5.QtWidgets import QApplication


@pytest.fixture(scope="session")
def app(qapp):
    return qapp
