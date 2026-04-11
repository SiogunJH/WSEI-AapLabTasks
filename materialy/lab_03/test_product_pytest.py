# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product(name="Testowy produkt", price=10.0, quantity=5)

@pytest.fixture
def empty_product():
    """Tworzy instancje Product z quantity=0."""
    return Product(name="Pusty produkt", price=5.0, quantity=0)

# --- Testy add_stock ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 10),
    (0, 5),
    (100, 105),
])
def test_add_stock_positive(product, amount, expected_quantity):
    """Sprawdz, czy dodanie towaru zwieksza quantity."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity

@pytest.mark.parametrize("amount", [
    -5,
    -10,
])
def test_add_stock_negative_raises(product, amount):
    """Sprawdz, czy ujemna wartosc rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(amount)

# --- Testy remove_stock ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (3, 2),
    (0, 5),
])
def test_remove_stock_positive(product, amount, expected_quantity):
    """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
    product.remove_stock(amount)
    assert product.quantity == expected_quantity

@pytest.mark.parametrize("amount", [
    10,
    100,
])
def test_remove_stock_too_much_raises(product, amount): 
    """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(amount)

@pytest.mark.parametrize("amount", [
    -2,
    -5,
])
def test_remove_stock_negative_raises(product, amount):
    """Sprawdz, czy ujemna wartosc rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(amount)

# --- Testy is_available ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() == True

def test_is_not_available(empty_product):
    """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
    assert empty_product.is_available() == False

# --- Testy total_value ---

@pytest.mark.parametrize("custom_product, expected_value", [
    (Product(name="Produkt A", price=10.0, quantity=5), 50.0),
    (Product(name="Produkt B", price=20.0, quantity=3), 60.0),
    (Product(name="Produkt C", price=5.0, quantity=10), 50.0),
])
def test_total_value(custom_product, expected_value):
    """Sprawdz, czy total_value zwraca price * quantity."""
    assert custom_product.total_value() == expected_value

def test_total_value_empty(empty_product):
    """Sprawdz, czy total_value dla produktu z quantity=0 zwraca 0."""
    assert empty_product.total_value() == 0.0

# --- Testy apply_discount ---

def test_apply_discount_zero(product):
    """Sprawdz, czy 0% rabatu nie zmienia ceny."""
    product.apply_discount(0)
    assert product.price == 10.0

@pytest.mark.parametrize("discount, expected_price", [
    (20, 8.0),
    (50, 5.0),
])
def test_apply_discount_positive(product, discount, expected_price):
    """Sprawdz, czy dodatni rabat zmienia cene zgodnie z oczekiwaniami."""
    product.apply_discount(discount)
    assert product.price == expected_price

def test_apply_discount_full(product):
    """Sprawdz, czy 100% rabatu obniza cene do 0."""
    product.apply_discount(100)
    assert product.price == 0.0

@pytest.mark.parametrize("discount", [
    -10,
    -50,
])
def test_apply_discount_negative_raises(product, discount):
    """Sprawdz, czy ujemny rabat rzuca ValueError."""
    with pytest.raises(ValueError):
        product.apply_discount(discount)

@pytest.mark.parametrize("discount", [
    150,
    200,
])
def test_apply_discount_too_high_raises(product, discount):
    """Sprawdz, czy rabat powyzej 100% rzuca ValueError."""
    with pytest.raises(ValueError):
        product.apply_discount(discount)

@pytest.mark.parametrize("discounts, expected_price", [
    ([10, 20], 7.2),
    ([50, 25], 3.75),
    ([20, 30, 10], 5.04),
])
def test_apply_multiple_discounts(product, discounts: list[float], expected_price):
    """Sprawdz, czy wielokrotne zastosowanie rabatu dziala poprawnie."""
    for discount in discounts:
        product.apply_discount(discount)
    assert product.price == expected_price