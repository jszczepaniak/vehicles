import unittest
from gear import (
    energy_sources,
    vehicles
)
class test_gear(unittest.TestCase):
    def test_add_fuel(self):
        engine = energy_sources.Generic_energy_source("gas")
        value = 5
        unit = "gas"
        fuel_before = engine.add_fuel(5, unit)
        fuel_to_add = 6
        self.assertEqual(engine.add_fuel(fuel_to_add, unit), fuel_before + fuel_to_add)
        self.assertRaises(ValueError, engine.add_fuel, fuel_to_add, "dupa")
        

if __name__ == '__main__':
    unittest.main()