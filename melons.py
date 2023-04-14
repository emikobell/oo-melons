from random import randint
from datetime import datetime

"""Classes for melon orders."""

class AbstractMelonOrder:


    def __init__(self,species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = None


    def get_base_price(self):
        self.base_price = randint(5,9)

        hour_now = datetime.now().hour
        weekday_now = datetime.now().weekday()

        if hour_now > 7 and hour_now < 11 and weekday_now >= 0 and weekday_now <5:
            self.base_price += 4

    def get_total(self):
        """Calculate price, including tax."""

        self.get_base_price()

        if self.species == "Christmas":
            self.base_price = self.base_price *1.5
        
        total = (1 + self.tax) * self.qty * self.base_price

        if self.qty < 10 and self.order_type == 'international':
            total += 3
            

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    order_type = "government"

    def __init__(self, species, quantity):
        super().__init__(species, quantity)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
