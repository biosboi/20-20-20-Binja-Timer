from binaryninja.settings import Settings


class twtwSettings(Settings):
    
    def __init__(self) -> None:
        super().__init__(instance_id='default')
        self.minuteTimer = 1200
        self.secondTimer = 20
        
        
    # Getters
    def getMinute(self) -> int:
        return self.minuteTimer
    
    def getSecond(self) -> int:
        return self.secondTimer
    
    # Setters
    def setMinute(self, newMin: int) -> None:
        self.minuteTimer = newMin
    
    def setSecond(self, newSec: int) -> None:
        self.secondTimer = newSec