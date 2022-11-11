class Problem:
    problem_categories = [
        "Kinematics",
        "Dynamics",
        "Energy",
        "Collisions",
        "System of Masses",
        "Rigid Bodies",
        "Oscillatory Motion",
        "Gravity",
        "Fluids",
        "Other",
        "Elasticity",
        "Experiment",
        "Dimensional Analysis",
        "Graphs",
        "Waves",
    ]

    def __init__(self, solved, secs, year, number, category):
        self.solved = solved
        self.secs = secs
        self.year = year
        self.number = number
        self.category = category

    def __repr__(self):
        return (
            str(self.solved)
            + " "
            + str(self.secs)
            + " "
            + str(self.year)
            + " "
            + str(self.number)
            + " "
            + self.category
        )
