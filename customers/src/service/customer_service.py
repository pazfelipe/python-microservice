from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    name: str
    email: str


@dataclass
class CustomerService:

    customers = []

    @classmethod
    def create_customer(self, customer: Customer) -> None:
        if not "name" in customer:
            raise ValueError("Name is required")

        if not "email" in customer:
            raise ValueError("Email is required")

        self.customers.append(customer)

        created_customer = customer
        created_customer["id"] = len(self.customers)
        created_customer["created_at"] = datetime.now()

        return created_customer

    def get_customers(self):
        return self.customers
