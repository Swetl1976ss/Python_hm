class Mailing:
    def __init__(self, track, from_address, to_address, cost):
        self.track = track
        self.to_address = from_address
        self.from_address = to_address
        self.cost = cost

    def __str__(self):
        return (f"Отправление {self.track} Из:{self.from_address}"
                f"в:{self.to_address}.Стоимость {self.cost} рублей.")




