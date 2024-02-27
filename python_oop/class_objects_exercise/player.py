class Player:
    def __init__(self, name: str, hp: int, mp: int, guild = "Unaffiliated"):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills = [f'==={skill_name} - {skill_mana_cost}' for skill_name, skill_mana_cost in self.skills]
        return f"""
        Name: {self.name}
        Guild: {self.guild}
        HP: {self.hp}
        MP: {self.mp}
        {"".join(skills)}
                """
        ### Тук трябва да сложа знак за нов ред