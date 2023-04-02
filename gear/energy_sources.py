from gear.fuel_units import fuel_units
from abc import ABC

class Generic_energy_source(ABC):
    def __init__(self, supported_fuel: str) -> None:
        if supported_fuel in fuel_units:
            self.supported_fuel = supported_fuel
            self.fuel_level = 0.0
        else:
            raise ValueError
            
    def add_fuel(self, value: float, unit: str) -> float:
        """AI is creating summary for add_fuel

        Args:
            value (float): [description]
            unit (str): [description]

        Raises:
            ValueError: [description]

        Returns:
            float: [description]
        """
        if unit in fuel_units:
            self.fuel_level += value
        else:
            raise ValueError
        return self.fuel_level

class Muscles(Generic_energy_source):
    def __init__(self) -> None:
        super().__init__("sausage")
