class Siege:
    def __init__(self, max_speed: int, efficiency: int) -> None:
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance: int, food_price: int) -> float:
        cost = (distance / self.efficiency) * food_price
        return cost

    def get_cargo_volume(self) -> float | None:
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed: int,
        efficiency: int,
        load_weight: int,
        bed_area: int,
    ) -> None:
        super().__init__(max_speed, efficiency)
        self.__load_weight = load_weight
        self.__bed_area = bed_area

    def get_trip_cost(self, distance: int, food_price: int) -> float:
        base = super().get_trip_cost(distance, food_price) 
        return base + (self.__load_weight * 0.01)

    def get_cargo_volume(self) -> float:
        volume = self.__bed_area * 2
        return volume


class Catapult(Siege):
    def __init__(self, max_speed: int, efficiency: int, cargo_volume: int) -> None:
        super().__init__(max_speed, efficiency)
        self.__cargo_volume = cargo_volume
        

    def get_cargo_volume(self) -> int:
        return self.__cargo_volume
