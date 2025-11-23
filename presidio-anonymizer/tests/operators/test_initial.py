import pytest

from presidio_anonymizer.operators import Initial

def test_correct_name():
    assert Initial().operator_name() == "initial"