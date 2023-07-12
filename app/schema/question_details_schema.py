class Question_Details_Validator(object):
    def __init__(self, question_details={}):
        self.question_details = question_details

    def validate(self):
        error_messages = []

        try:
            question_template_id = self.question_details.get('question_template_id')
            if not question_template_id or len(question_template_id.strip()) == 0:
                error_messages.append('Question template ID is required')
        except Exception as e:
            error_messages.append('Error validating question template ID')

        try:
            question_text_template = self.question_details.get('question_text_template')
            if not question_text_template or len(question_text_template.strip()) == 0:
                error_messages.append('Question text template is required')
        except Exception as e:
            error_messages.append('Error validating question text template')

        try:
            question_image = self.question_details.get('question_image')
            if not question_image or len(question_image.strip()) == 0:
                error_messages.append('Question image is required')
        except Exception as e:
            error_messages.append('Error validating question image')

        try:
            developer_note = self.question_details.get('developer_note')
            if not developer_note or len(developer_note.strip()) == 0:
                error_messages.append('Developer note is required')
        except Exception as e:
            error_messages.append('Error validating developer note')

        return error_messages
