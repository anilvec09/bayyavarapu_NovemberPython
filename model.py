class Breed:
    def __init__(self,id,name,temperament,coat):
        self.id
        self.name=name
        self.temperaament=temperament
        self.coat=coat
        var=[id,name,temperament,coat]
        for vars in var:
            if not vars:
                raise Exception(f"One or More Required  Variables are Empty")


    def __init__(self, name, temperament, coat):
        self.name = name
        self.temperaament = temperament
        self.coat = coat
        var=[name,temperament,coat]
        for vars in var:
            if not vars:
                raise Exception(f"One or More Required  Variables are Empty")


class Pupper:
    def __init__(self,id,name, sex, weight, height, color, date_of_birth, breed_id):
        self.id=id
        self.name=name
        self.sex=sex
        self.weight=weight
        self.height=height
        self.color=color
        self.date_of_birth=date_of_birth
        self.breed_id=breed_id
        var=[id,name, sex, weight, height, color, date_of_birth, breed_id]
        for vars in var:
            if not vars:
                raise Exception(f"One or More Required  Variables are Empty")

    def __init__(self, name, sex, weight, height, color, date_of_birth, breed_id):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.height = height
        self.color = color
        self.date_of_birth = date_of_birth
        self.breed_id = breed_id
        var=[name, sex, weight, height, color, date_of_birth, breed_id]
        for vars in var:
            if not vars:
                raise Exception(f"One or More Required  Variables are Empty")