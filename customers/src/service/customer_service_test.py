import unittest
from .customer_service import CustomerService


class CustomerServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.customer = CustomerService()
        self.mock_customer = {"name": "John Doe", "email": "test@gmail.com"}
        return super().setUp()

    def test_get_customer(self):
        pass

    def test_create_customer_raise_error_if_name_is_missing(self):
        with self.assertRaises(ValueError):
            self.mock_customer.pop("name")
            self.customer.create_customer(self.mock_customer)

    def test_create_customer_raise_error_if_email_is_missing(self):
        with self.assertRaises(ValueError):
            self.mock_customer.pop("email")
            self.customer.create_customer(self.mock_customer)

    def test_create_customer(self):

        response = self.customer.create_customer(self.mock_customer)
        self.assertTrue("id" in response)
        self.assertEqual(response["id"], 1)

    def test_update_customer(self):
        pass

    def test_delete_customer(self):
        pass
