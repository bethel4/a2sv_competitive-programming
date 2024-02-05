class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        my_list = []
        Kelvin = celsius + 273.15
        my_list.append(float(f"{Kelvin:.5f}"))
        Fahrenheit = (celsius * 1.80 + 32.00)
        my_list.append(float(f"{Fahrenheit:.5f}"))
        return my_list
        
