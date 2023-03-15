from websites import User
import unittest
from mock import MagicMock, patch
from firebase_admin import db



class TestMyClass(unittest.TestCase):

    @patch('my_module.db')
    def test_get_id_rtdb(self, mock_db):
        # Setup
        mock_ref = MagicMock()
        mock_ref.get.return_value = 12345
        mock_db.reference.return_value = mock_ref

        # Create instance of MyClass
        my_instance = User()

        # Call the function being tested
        result = my_instance.get_id_rtdb()

        # Assert the expected result
        self.assertEqual(result, 12345)

        # Assert that the necessary Firebase Realtime Database methods were called
        mock_db.reference.assert_called_once_with('id')
        mock_ref.get.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
