class Question_Solution_Validator:
    def __init__(self, question_solution={}):
        self.question_solution = question_solution

    def validate(self):
        error_messages = []

        try:
            question_formula = self.question_solution.get('question_formula')
            if not question_formula or len(question_formula.strip()) == 0:
                error_messages.append('Question formula is required')
        except Exception as e:
            error_messages.append('Error validating question formula')

        try:
            question_hint = self.question_solution.get('question_hint')
            if not question_hint or len(question_hint.strip()) == 0:
                error_messages.append('Question hint is required')
        except Exception as e:
            error_messages.append('Error validating question hint')

        try:
            video_solution = self.question_solution.get('video_solution')
            if not video_solution or len(video_solution.strip()) == 0:
                error_messages.append('Video solution is required')
        except Exception as e:
            error_messages.append('Error validating video solution')

        try:
            image_solution = self.question_solution.get('image_solution')
            if not image_solution or len(image_solution.strip()) == 0:
                error_messages.append('Image solution is required')
        except Exception as e:
            error_messages.append('Error validating image solution')

        try:
            question_template_id = self.question_solution.get('question_template_id')
            if not question_template_id or len(question_template_id.strip()) == 0:
                error_messages.append('Question template ID is required')
        except Exception as e:
            error_messages.append('Error validating question template ID')

        return error_messages
