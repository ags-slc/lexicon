"""Integration tests for Localzone"""
from unittest import TestCase
from shutil import copyfile

import os
import pytest
from lexicon.tests.providers.integration_tests import IntegrationTests


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from define_tests.TheTests
class LocalzoneProviderTests(TestCase, IntegrationTests):
    """Integration tests for Localzone"""
    provider_name = "localzone"
    domain = "example.com"

    testpath = os.path.dirname(__file__)
    fixturepath = os.path.join(testpath, "..", "..", "..", "tests", "fixtures")
    zonefile = os.path.join(fixturepath, "db.example.com")
    testfile = os.path.join(fixturepath, "test.db.example.com")

    @pytest.fixture(scope="class", autouse=True)
    def create_testfile(self):
        """Create a zone file for testing."""
        copyfile(self.zonefile, self.testfile)
        yield
        os.remove(self.testfile)

    def _test_parameters_overrides(self):
        options = {
            "filename": self.testfile
        }

        return options

    def _test_fallback_fn(self):
        return lambda _: None

    @pytest.mark.skip(reason="localzone does not require authentication")
    def test_provider_authenticate(self):
        return

    @pytest.mark.skip(reason="localzone does not require authentication")
    def test_provider_authenticate_with_unmanaged_domain_should_fail(self):
        return
