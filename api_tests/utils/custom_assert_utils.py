

class KeyAsserter:
    @staticmethod
    def verify_expected_keys_in_response_data(response_keys, expected_keys):
        try:
            for key in expected_keys:
                assert key in response_keys, key    # If missing, raised in report
        except Exception as e:
            raise Exception(e)