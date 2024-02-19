class UndergroundSystem:

    def __init__(self):
         self.data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.data:
            self.data[id] = [{'check_in_time': t, 'check_in_country': stationName}]
        else:
            self.data[id].append({'check_in_time': t, 'check_in_country': stationName})

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.data:
            self.data[id][-1]['check_out_time'] = t
            self.data[id][-1]['check_out_country'] = stationName
       

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = 0
        count = 0
        for user_id, checkin_checkout_list in self.data.items():
            for checkin_checkout in checkin_checkout_list:
                check_in_country = checkin_checkout.get('check_in_country')
                check_out_country = checkin_checkout.get('check_out_country')

                if check_in_country == startStation and check_out_country == endStation:
                    check_in_time = checkin_checkout.get('check_in_time', 0)
                    check_out_time = checkin_checkout.get('check_out_time', 0)

                    total_time += check_out_time - check_in_time
                    count += 1

        return total_time / count if count > 0 else 0.0

