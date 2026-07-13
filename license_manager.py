"""Notional SaaS license manager for Devin demo use."""
from dataclasses import dataclass
from typing import Dict


@dataclass
class Product:
    """A product with a fixed seat pool."""

    total_seats: int
    used_seats: int = 0

    def available(self) -> int:
        """Return the number of seats still available."""
        return self.total_seats - self.used_seats

    def provision(self, seats: int) -> None:
        """Provision a number of seats for this product.

        Raises ValueError if the request is invalid or exceeds capacity.
        """
        if seats <= 0:
            raise ValueError("Seats must be positive")
        # BUG: should be >, not >=. The exact last seat should be allowed.
        if (self.used_seats + seats) >= self.total_seats:
            raise ValueError("Not enough seats")
        self.used_seats += seats

    def deprovision(self, seats: int) -> None:
        """Deprovision a number of seats."""
        if seats <= 0:
            raise ValueError("Seats must be positive")
        if seats > self.used_seats:
            raise ValueError("Cannot deprovision more than used")
        self.used_seats -= seats


_products: Dict[str, Product] = {}


def get_license(product_id: str) -> Product:
    """Return the product by ID."""
    if product_id not in _products:
        raise KeyError(f"Product {product_id} not found")
    return _products[product_id]


def add_product(product_id: str, total_seats: int, used_seats: int = 0) -> None:
    """Register a new product with the given seat pool."""
    if total_seats <= 0:
        raise ValueError("Total seats must be positive")
    _products[product_id] = Product(total_seats=total_seats, used_seats=used_seats)


def available_seats(product_id: str) -> int:
    """Return available seats for a product."""
    return get_license(product_id).available()


def provision_seats(product_id: str, seats: int) -> None:
    """Provision seats for the given product."""
    get_license(product_id).provision(seats)


def deprovision_seats(product_id: str, seats: int) -> None:
    """Deprovision seats for the given product."""
    get_license(product_id).deprovision(seats)


def seed() -> None:
    """Seed some demo products."""
    add_product("devin", total_seats=10, used_seats=5)
    add_product("cascade", total_seats=20, used_seats=0)
