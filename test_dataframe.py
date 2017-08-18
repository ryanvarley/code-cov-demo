import pytest

import dataframe


@pytest.fixture()
def df_fixture():
    return dataframe.DataList(list(range(10)))


def test_head(df_fixture):
    assert df_fixture.head(5) == list(range(5))


def test_tail(df_fixture):
    assert df_fixture.tail(5) == list(range(5, 10))


def test_merge(df_fixture):
    assert df_fixture.merge([20, 21, 22]) == (list(range(10)) + [20, 21, 22])


def test_sample(df_fixture):
    result = df_fixture.sample(3)
    assert set(result).issubset(df_fixture.data)
