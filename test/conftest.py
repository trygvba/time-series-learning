import pytest


@pytest.fixture
def data_dir():
    return "data"


@pytest.fixture
def unemp_file():
    return "data/unemp.rda"
