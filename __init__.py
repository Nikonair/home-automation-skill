from mycroft import MycroftSkill, intent_file_handler


class HomeAutomation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('automation.home.intent')
    def handle_automation_home(self, message):
        self.speak_dialog('automation.home')


def create_skill():
    return HomeAutomation()

