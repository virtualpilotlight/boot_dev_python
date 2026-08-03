class Sword:
    def __init__(self, sword_type: str) -> None:
        self.sword_type = sword_type

    def __add__(self, other: "Sword") -> "Sword":
        new_sword = self.sword_type + other.sword_type
        if self.sword_type == other.sword_type:
            if self.sword_type == "bronze":
                new_sword = Sword("iron") 
                return new_sword
            elif self.sword_type == "iron":
                new_sword = Sword("steel")
                return new_sword
        raise Exception("cannot craft")
