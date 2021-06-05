from mycroft import MycroftSkill, intent_file_handler


class Education(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('education.intent')
    def handle_education(self, message):
        self.speak_dialog('education')


def create_skill():
    return Education()

