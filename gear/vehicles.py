from gear import energy_sources
import abc
from gear import fuel_units

class Fuel_error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Vehicle(abc):
    def __init__(self, number_of_wheels: int, fuel_type: list) -> None:
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type
        self.primary_fuel_level = 1.0
        self.energy_source = []
    
    def go_forward(self) -> None:
        print("I'm going forward!")
        # TODO use fuel
    
    def go_backward(self) -> None:
        print("I'm going backward!")
        # TODO use fuel

    def add_fuel(self, fuel_type: str, value: int) -> None:
        try:
            if fuel_type not in self.fuel_type:
                raise Fuel_error()
        except Fuel_error:
            print("This vehicle cannot use that fuel!")
        else:
            print("%s %s of %s has been added." %(value, fuel_units[fuel_type], fuel_type))
        finally:
            print("Leaving the gas station")
        
    

class Bicycle(Vehicle):
    def __init__(self) -> None:
        super().__init__(2, ["sausage"])
        self.energy_source.append(energy_sources.Muscles())
