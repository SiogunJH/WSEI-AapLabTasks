# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


import string


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name: string = name
        self.price: float = price
        self.quantity: int = quantity
        
        if price < 0:
            raise ValueError("Cena nie moze byc ujemna.")
        if quantity < 0:
            raise ValueError("Ilosc nie moze byc ujemna.")

    def add_stock(self, amount: int):
        """Dodaje okreslona ilosc produktow do magazynu.

        Raises:
            ValueError: jesli amount jest ujemne
        """
        if amount < 0:
            raise ValueError("Ilosc do dodania nie moze byc ujemna.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa okreslona ilosc produktow z magazynu.

        Raises:
            ValueError: jesli amount jest ujemne lub wieksze niz dostepna ilosc
        """
        if amount < 0:
            raise ValueError("Ilosc do usuniecia nie moze byc ujemna.")
        if amount > self.quantity:
            raise ValueError("Nie mozna usunac wiecej niz jest dostepne.")
        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jesli produkt jest dostepny (quantity > 0)."""
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca calkowita wartosc produktow w magazynie (price * quantity)."""
        return self.price * self.quantity
    
    def apply_discount(self, percentage: float):
        """Zastosuj zniżkę do ceny produktu.

        Args:
            percentage (float): Procent zniżki (np. 20.0 dla 20%)

        Raises:
            ValueError: jeśli percentage jest ujemne lub większe niż 100
        """
        if self.price == 0:
            return;

        if percentage < 0 or percentage > 100:
            raise ValueError("Procent zniżki musi być między 0 a 100.")
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
