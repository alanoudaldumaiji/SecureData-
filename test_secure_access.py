import unittest

from unittest.mock import patch



from secure_access import get_employees





class TestSecureAccess(unittest.TestCase):



    @patch("secure_access.sqlite3.connect")

    def test_viewer_is_denied_before_database_access(self, mock_connect):

        with self.assertRaises(PermissionError):

            get_employees("Viewer")



        mock_connect.assert_not_called()



    @patch("secure_access.sqlite3.connect")

    def test_unknown_role_is_denied_before_database_access(self, mock_connect):

        with self.assertRaises(PermissionError):

            get_employees("Unknown")



        mock_connect.assert_not_called()



    @patch("secure_access.sqlite3.connect")

    def test_admin_can_query_database(self, mock_connect):

        mock_cursor = mock_connect.return_value.cursor.return_value

        mock_cursor.fetchall.return_value = [

            (1, "Sara", "IT")

        ]



        result = get_employees("Admin")



        self.assertEqual(len(result), 1)

        mock_cursor.execute.assert_called_once()

        mock_connect.return_value.close.assert_called_once()





if __name__ == "__main__":

    unittest.main()