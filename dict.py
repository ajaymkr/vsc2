
offence= {"rahul":1,"amit":3,"suman":5}

class atm:


     def generate_description_from_offense(self, offense):
        description = ""
        for key, value in offense.items():
            description += f"<strong>{key}: </strong>"
            try:
                description += "<br/>" + str(value)
                description += "<br/><br/>"
            except:
                description += "-"
            print(description)
        return description

       