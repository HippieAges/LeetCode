class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteDeg = self.getMinuteDegree(minutes)
        hourDeg = self.getHourDegree(hour, minutes)
        difference = abs(hourDeg - minuteDeg)
        minAngle = min(difference, 360 - difference)
        return minAngle
    
    # 360 degrees in a circle / 60 minutes = 6 degrees per minute for the minute hand
    def getMinuteDegree(self, minutes: int) -> int:
        return minutes * 6 
    
    # so 30 degrees / 60 minutes = 0.5 degrees per minute for the hour hand
    # Also, 360 degrees for a full circle / 12 hours = 30 degrees per hour for hour hand
    def getHourDegree(self, hour: int, minutes: int) -> int:
        return (hour * 30) + (minutes * 0.5)