"""Tests for the notional license manager."""
import pytest

from license_manager import (
    add_product,
    available_seats,
    deprovision_seats,
    get_license,
    provision_seats,
)


def test_provision_exact_capacity():
    """Provisioning the exact last available seat should succeed."""
    add_product("demo-product", total_seats=10, used_seats=5)
    provision_seats("demo-product", 5)
    assert available_seats("demo-product") == 0


def test_provision_exceeds_capacity():
    """Provisioning more seats than available should fail."""
    add_product("demo-product", total_seats=10, used_seats=8)
    with pytest.raises(ValueError):
        provision_seats("demo-product", 3)


def test_deprovision_seats():
    """Deprovisioning seats should free them up."""
    add_product("demo-product", total_seats=10, used_seats=5)
    deprovision_seats("demo-product", 2)
    assert available_seats("demo-product") == 7
    assert get_license("demo-product").used_seats == 3


def test_provision_negative_seats():
    """Provisioning a non-positive number of seats should fail."""
    add_product("demo-product", total_seats=10, used_seats=0)
    with pytest.raises(ValueError):
        provision_seats("demo-product", -1)
