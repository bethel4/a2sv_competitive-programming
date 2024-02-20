class FrequencyTracker:
    def __init__(self):
        self.number_frequency = {}  # Dictionary to store frequency of each number
        self.frequency_numbers = {}  # Dictionary to store numbers corresponding to each frequency

    def add(self, number):
        # Update the frequency of the number
        frequency = self.number_frequency.get(number, 0) + 1
        self.number_frequency[number] = frequency

        # Update the set of numbers corresponding to the frequency
        if frequency not in self.frequency_numbers:
            self.frequency_numbers[frequency] = set()
        self.frequency_numbers[frequency].add(number)

        # If the number had a previous frequency, remove it from the set
        if frequency > 1:
            self.frequency_numbers[frequency - 1].remove(number)

    def deleteOne(self, number):
        if number in self.number_frequency and self.number_frequency[number] > 0:
            # Update the frequency of the number
            frequency = self.number_frequency[number]
            self.number_frequency[number] = frequency - 1

            # Update the set of numbers corresponding to the frequency
            self.frequency_numbers[frequency].remove(number)
            if frequency - 1 > 0:
                if frequency - 1 not in self.frequency_numbers:
                    self.frequency_numbers[frequency - 1] = set()
                self.frequency_numbers[frequency - 1].add(number)

    def hasFrequency(self, frequency):
        return frequency in self.frequency_numbers and len(self.frequency_numbers[frequency]) > 0

