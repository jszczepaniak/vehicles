from gear import vehicles

some_bike = vehicles.Bicycle()
print(some_bike.fuel_type)
some_bike.go_forward()
some_bike.go_backward()
some_bike.add_fuel("sausage", 300)
some_bike.add_fuel("gas", 2)