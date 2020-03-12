from mycroft import MycroftSkill, intent_file_handler
from wakeonlan import send_magic_packet
import os
import time

class HomeAutomation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

#----------------------- CINEMA ---------------------------

    @intent_file_handler('power.on.cinema.intent')
    def handle_power_on_cinema(self, message):
        self.speak_dialog('automation.home')
    
    @intent_file_handler('power.off.cinema.intent')
    def handle_power_off_cinema(self, message):
        self.speak_dialog('off')
    
    @intent_file_handler('switch.intent')
    def handle_switch(self, message):
        device = message.data.get('device')
        if device == "computer":
            self.speak_dialog("switching to computer")
        else:
            self.speak_dialog("switching to xbox")

    @intent_file_handler('power.xbox.intent')
    def handle_power_xbox(self, message):
        powermode = message.data.get('powermode')
        if powermode == "on":
            self.speak_dialog('automation.home')
            send_magic_packet(self.settings.get('xbox_mac'))
        else:
            self.speak_dialog("power off xbox")

    def stop(self):
        pass

#----------------------- Lights ---------------------------

def create_skill():
    return HomeAutomation()

