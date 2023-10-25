from binaryninja import *
import time

class twtwTimer(BackgroundTaskThread):
    def __init__(self, minTimer: int, secTimer: int) -> None:
        BackgroundTaskThread.__init__(self, "Beginning Timer...", True)
        self.relaxFlag: bool = False
        self.minuteTimer: int = minTimer;
        self.secondTimer: int = secTimer;
        self.startTime = time.time()

                
    # calc remaining time based on time.time() pull
    def __timer(self, remainingTime) -> None:
        while (time.time() - self.startTime < remainingTime):
            pass
        return
    
    # Begin countdown for analysis period. Twenty minutes by default
    def __analysisCountdown(self) -> None:
        self.startTime = time.time()
        self.__timer(self.minuteTimer)
        self.relaxFlag = True
        if show_message_box("Analysis Time Complete", "Time to begin your eye strain relief. Take a break for a bit.\nWould you like to keep the timer going?", MessageBoxButtonSet.YesNoButtonSet) == 1:
            self.__relaxCountdown()
        
    # Begin countdown for relaxation period. Twenty seconds by default
    def __relaxCountdown(self) -> None:
        self.startTime = time.time()
        self.__timer(self.secondTimer)
        self.relaxFlag = False
        if show_message_box("Relaxation Time Complete", "Time to get back to analysis.\nWould you like to keep the timer going?", MessageBoxButtonSet.YesNoButtonSet) == 1:
            self.__analysisCountdown()
    
    # Init Timers
    def run(self):
        self.__analysisCountdown()
    
    
    
    # Getters
    def getMinute(self) -> int:
        return self.minuteTimer
    
    def getSecond(self) -> int:
        return self.secondTimer
    
    def getFlag(self) -> bool:
        return self.relaxFlag
    
    # Setters
    def setMinute(self, newMin: int) -> None:
        self.minuteTimer = newMin
    
    def setSecond(self, newSec: int) -> None:
        self.secondTimer = newSec
        
    def setFlag(self, newFlag: bool) -> None:
        self.relaxFlag = newFlag