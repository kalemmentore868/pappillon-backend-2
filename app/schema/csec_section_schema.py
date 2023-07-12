class CSEC_SectionSchemaValidator:
    def __init__(self, csec_section={}):
        self.csec_section = csec_section

    def validate(self):
        error_messages = []

        try:
            name = self.csec_section.get('name')
            if not name or len(name.strip()) == 0:
                error_messages.append('Name is required')
        except Exception as e:
            error_messages.append('Error validating name')

        try:
            name = self.csec_section.get('subject_id')
            if not name or len(name.strip()) == 0:
                error_messages.append('subject_id is required')
        except Exception as e:
            error_messages.append('Error validating subject_id')

        try:
            objectives = self.csec_section.get('objectives')
            if not objectives or len(objectives) == 0:
                error_messages.append('Objectives are required')
        except Exception as e:
            error_messages.append('Error validating objectives')

        return error_messages
