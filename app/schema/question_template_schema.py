class Question_Template_Validator(object):
    def __init__(self, question_template={}):
        self.question_template = question_template

    def validate(self):
        error_messages = []

        try:
            name = self.question_template.get('name')
            if not name or len(name.strip()) == 0:
                error_messages.append('Name is required')
        except Exception as e:
            error_messages.append('Error validating name')

        try:
            status = self.question_template.get('status')
            if not status or len(status.strip()) == 0:
                error_messages.append('Status is required')
        except Exception as e:
            error_messages.append('Error validating status')

        try:
            subject = self.question_template.get('subject')
            if not subject or len(subject.strip()) == 0:
                error_messages.append('Subject is required')
        except Exception as e:
            error_messages.append('Error validating subject')

        try:
            description = self.question_template.get('description')
            if not description or len(description.strip()) == 0:
                error_messages.append('Description is required')
        except Exception as e:
            error_messages.append('Error validating description')

        try:
            csecSection = self.question_template.get('csecSection')
            if not csecSection or len(csecSection.strip()) == 0:
                error_messages.append('CSEC section is required')
        except Exception as e:
            error_messages.append('Error validating CSEC section')

        try:
            objectives = self.question_template.get('objectives')
            if not objectives or len(objectives) == 0:
                error_messages.append('Objectives are required')
        except Exception as e:
            error_messages.append('Error validating objectives')

        try:
            questionFormat = self.question_template.get('questionFormat')
            if not questionFormat or len(questionFormat.strip()) == 0:
                error_messages.append('Question format is required')
        except Exception as e:
            error_messages.append('Error validating question format')

        try:
            questionType = self.question_template.get('questionType')
            if not questionType or len(questionType.strip()) == 0:
                error_messages.append('Question type is required')
        except Exception as e:
            error_messages.append('Error validating question type')

        try:
            difficulty = self.question_template.get('difficulty')
            if not difficulty or len(difficulty.strip()) == 0:
                error_messages.append('Difficulty is required')
        except Exception as e:
            error_messages.append('Error validating difficulty')

        return error_messages
