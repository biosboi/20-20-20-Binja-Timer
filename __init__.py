# 20-20 will hereby be referred to as twtw

from binaryninja import *
from binaryninjaui import *
from . src.settings import twtwSettings
from . src.timer import *

# Init settings
settings = twtwSettings()
timerObject = twtwTimer(settings.getMinute(), settings.getSecond())

def ActivateTimer(bv) -> None:
	if show_message_box("Activate Timer", "20-20-20 Binary Ninja Eystrain Timer\n\nClick Yes to begin your 20 minute timer.", MessageBoxButtonSet.YesNoButtonSet, MessageBoxIcon.InformationIcon) == 1:
		try:
			timerObject.start()
		except:
			pass
  
# Turn off the timer. The object is not well handled here, but I will fix it later
def DeactivateTimer(bv) -> None:
    if show_message_box("Deactivate Timer", "20-20-20 Binary Ninja Eystrain Timer\n\nClick Yes to end your 20 minute timer.", MessageBoxButtonSet.YesNoButtonSet, MessageBoxIcon.InformationIcon) == 1:
        try:
            del timerObject
        except:
            pass

# Change default values for timer
def SettingsMenu(bv) -> None:
    pass


# Eventually I will add features to turn off the timer and change default values.
PluginCommand.register("20-20-20 Timer\Activate Timer", "Your relaxation countdown begins now. Get analysing!", ActivateTimer)

# Delete timer object. If new timer is created, new object will be created
PluginCommand.register("20-20-20 Timer\Deactivate Timer", "I hope you have eye insurance", DeactivateTimer)

PluginCommand.register("20-20-20 Timer\Timer Settings", "Adjust frequency of breaks", SettingsMenu)