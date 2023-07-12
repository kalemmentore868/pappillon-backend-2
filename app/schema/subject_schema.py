class SubjectSchemaValidator:
    def __init__(self, subject={}):
        self.subject = subject

    def validate(self):
        error_messages = []

        try:
            name = self.subject.get('name')
            if not name or len(name.strip()) == 0:
                error_messages.append('Name is required')
        except Exception as e:
            error_messages.append('Error validating name')

        try:
            sections = self.subject.get('sections')
            if not sections or len(sections) == 0:
                error_messages.append('Sections are required')
        except Exception as e:
            error_messages.append('Error validating sections')

        return error_messages
