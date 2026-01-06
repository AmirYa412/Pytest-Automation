class KeyAsserter:
    """Utility class for validating API response structure.

    Provides assertion helpers for verifying expected keys exist in
    API response data, with clear error messages for debugging.
    """

    @staticmethod
    def verify_expected_keys_in_response_data(response_keys: list, expected_keys: list) -> None:
        """Verify all expected keys exist in the response.

        Args:
            response_keys: Keys present in the API response
            expected_keys: Keys that must be present

        Raises:
            AssertionError: If any expected key is missing, with details about which key
        """
        for key in expected_keys:
            assert key in response_keys, (
                f"Missing expected key '{key}' in response. "
                f"Available keys: {sorted(response_keys)}"
            )
