import unittest
from security import check_access


class TestSecureDataSecurity(unittest.TestCase):

    def test_admin_can_access_confidential(self):
        self.assertTrue(
            check_access("Admin", "Confidential")
        )

    def test_analyst_cannot_access_confidential(self):
        self.assertFalse(
            check_access("Analyst", "Confidential")
        )

    def test_viewer_cannot_access_internal(self):
        self.assertFalse(
            check_access("Viewer", "Internal")
        )

    def test_unknown_role_is_denied(self):
        self.assertFalse(
            check_access("Unknown", "Public")
        )

    def test_unknown_classification_is_denied(self):
        self.assertFalse(
            check_access("Admin", "Restricted")
)


if __name__ == "__main__":
    unittest.main()