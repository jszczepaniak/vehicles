from gear import fuel_units
from abc import ABC

class Generic_energy_source(ABC):
    def __init__(self, supported_fuel) -> None:
        if supported_fuel in fuel_units:
            self.supported_fuel = supported_fuel
            self.fuel_level = 0.0
        else:
            raise ValueError
            
    def add_fuel(self, value: float, unit: str) -> float:
        if unit in fuel_units.items():
            self.fuel_level += value
        else:
            raise ValueError
        return self.fuel_level

class Muscles(Generic_energy_source):
    def __init__(self) -> None:
        super().__init__("sausage")
