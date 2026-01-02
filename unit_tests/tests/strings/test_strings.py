import pytest
from unit_tests.src.strings.convert_string import ConvertString

pytestmark = pytest.mark.unit


class TestConvertString:
    def test_convert_string_to_upper(self):
        string = "hello world"
        converted_string = ConvertString(string).convert_string_to_upper()
        assert "HELLO WORLD" == converted_string

    def test_convert_string_to_lower(self):
        string = "HELLO WORLD"
        converted_string = ConvertString(string).convert_string_to_lower()
        assert "hello world" == converted_string