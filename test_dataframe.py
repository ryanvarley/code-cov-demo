import pytest

import dataframe


@pytest.fixture()
def df_fixture():
    return dataframe.DataList(list(range(10)))


def test_merge(df_fixture):
    assert df_fixture.merge([20, 21, 22]) == (list(range(10)) + [20, 21, 22])

