# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""
        self.product: Product = Product(name="Testowy produkt", price=10.0, quantity=5)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 10)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 2)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(10)

    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(-2)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
        self.product = Product(name="Testowy produkt", price=10.0, quantity=0)
        self.assertFalse(self.product.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""
        self.assertEqual(self.product.total_value(), 50.0)

    # --- Testy apply_discount ---

    def test_apply_discount_zero(self):
        """Sprawdz, czy 0% rabatu nie zmienia ceny."""
        self.product.apply_discount(0)
        self.assertEqual(self.product.price, 10.0)
    
    def test_apply_discount_positive(self):
        """Sprawdz, czy 20% rabatu obniza cene o 20%."""
        self.product.apply_discount(20)
        self.assertEqual(self.product.price, 8.0)
    
    def test_apply_discount_full(self):
        """Sprawdz, czy 100% rabatu obniza cene do 0."""
        self.product.apply_discount(100)
        self.assertEqual(self.product.price, 0.0)

    def test_apply_discount_negative_raises(self):
        """Sprawdz, czy ujemny rabat rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.apply_discount(-10)
    
    def test_apply_discount_over_100_raises(self):
        """Sprawdz, czy rabat powyzej 100% rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.apply_discount(150)

    def test_apply_discount_multiple_times(self):
        """Sprawdz, czy wielokrotne stosowanie rabatu dziala poprawnie."""
        self.product.apply_discount(10)  # 10% rabatu -> cena 9.0
        self.product.apply_discount(20)  # dodatkowe 20% rabatu -> cena 7.2
        self.assertEqual(self.product.price, 7.2)

if __name__ == "__main__":
    unittest.main()
