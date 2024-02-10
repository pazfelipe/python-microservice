import unittest
from .customer_service import CustomerService


class CustomerServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.customer = CustomerService()
        return super().setUp()

    def test_get_customer(self):
        pass

    def test_create_customer(self):
        with self.assertRaises(ValueError):
            self.customer.create_customer(customer={"name": "test"})

        with self.assertRaises(ValueError):
            self.customer.create_customer(customer={"name": "John Doe"})

        response = self.customer.create_customer(
            customer={"name": "John Doe", "email": "test@email.com"}
        )
        self.assertTrue("id" in response)
        self.assertEqual(response["id"], 1)

    def test_update_customer(self):
        pass

    def test_delete_customer(self):
        pass
