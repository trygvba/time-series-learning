import pytest
import utils
import pandas as pd


def test_read_data(unemp_file):
    data = utils.read_rdata(unemp_file)
    assert data is not None
    assert len(data["unemp"]) > 20
