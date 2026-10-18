import unittest

from unittest.mock import patch

from audit_logger import log_access





class TestAuditLogger(unittest.TestCase):



    @patch("audit_logger.logger.info")

    def test_allowed_access_is_logged(self, mock_info):

        log_access("Admin", "Employee Directory", True)



        mock_info.assert_called_once_with(

            "Role=%s | Resource=%s | Status=%s",

            "Admin",

            "Employee Directory",

            "ALLOWED"

        )



    @patch("audit_logger.logger.info")

    def test_denied_access_is_logged(self, mock_info):

        log_access("Viewer", "Employee Directory", False)



        mock_info.assert_called_once_with(

            "Role=%s | Resource=%s | Status=%s",

            "Viewer",

            "Employee Directory",

            "DENIED"

        )





if __name__ == "__main__":

    unittest.main()