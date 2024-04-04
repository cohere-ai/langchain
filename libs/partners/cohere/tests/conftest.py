import pytest


@pytest.fixture(scope='module')
def vcr_config():
    return {
        # IMPORTANT: Filter out the Authorization header from stored replay test data.
        "filter_headers": [('Authorization', None)],
    }
