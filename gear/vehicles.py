class Vehicle():
    def __init__(self, number_of_wheels: int, fuel_type: list) -> None:
        self.number_of_wheels = number_of_wheels
        self.fuel_type = fuel_type
    
    def go_forward() -> None:
        print("I'm going forward!")
    
    def go_backward() -> None:
        print("I'm going backward!")

    def tank_up(fuel_type: str, value: int) -> None:
        pass

class Bicycle(Vehicle):
    def __init__(self) -> None:
        super().__init__(2, ["sausage"])
