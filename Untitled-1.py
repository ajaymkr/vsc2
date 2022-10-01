

class student():
 
  def generate_description_from_offense(self, offense):
        description = ""
        offence=self. offenses = {"physics":80,"maths":65}
        for key, value in offense:
            description += f"<strong>{key}: </strong>"
            try:
                description += "<br/>" + str(value)
                description += "<br/><br/>"
            except:
                description += "-"
            print(description)
            print(offence)

        return description