class FrequencyTracker:

    def __init__(self):
        self.numFreq = {}
        self.freqCount = {}

    def _inc_freq_count(self, freq: int, delta: int) -> None:
        if freq <= 0:
            return
        self.freqCount[freq] = self.freqCount.get(freq, 0) + delta
        if self.freqCount[freq] == 0:
            del self.freqCount[freq]

    def add(self, number: int) -> None:
        old_freq = self.numFreq.get(number, 0)
        new_freq = old_freq + 1

        self.numFreq[number] = new_freq

        if old_freq > 0:
            self._inc_freq_count(old_freq, -1)
        self._inc_freq_count(new_freq, 1)

    def deleteOne(self, number: int) -> None:
        if number not in self.numFreq:
            return

        old_freq = self.numFreq[number]
        new_freq = old_freq - 1

        if new_freq == 0:
            del self.numFreq[number]
        else:
            self.numFreq[number] = new_freq

        self._inc_freq_count(old_freq, -1)
        if new_freq > 0:
            self._inc_freq_count(new_freq, 1)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount.get(frequency, 0) > 0
