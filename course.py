class Course:
    def __init__(self, *args, **kwargs):
        self.courseCode = kwargs.get("courseCode", "None")
        self.courseName = kwargs.get("courseName", "None")
        self.date = kwargs.get("date", None)
        self.weekNumber = int(kwargs.get("weekNumber", -1))
        self.day = kwargs.get("day", "None")
        self.dayNumber = int(kwargs.get("dayNumber", -1))
        self.hourStart = kwargs.get("hourStart", "00h00")
        self.hourEnd = kwargs.get("hourEnd", "00h00")
        self.duration = kwargs.get("duration", "00h00")
        self.width = int(kwargs.get("width", -1))
        self.left = int(kwargs.get("left", -1))

        self.weekDays = ["Lundi", "Mardi", "Mercredi",
                         "Jeudi", "Vendredi", "Samedi", "Dimanche"]

        if self.width and self.left:
            print(self.left+1//self.width)
            self.day = self.weekDays[(self.left+1)//self.width]

    def __str__(self):
        return f"courseCode: {self.courseCode},\n courseName: {self.courseName},\n date: {self.date},\n weekNumber: {self.weekNumber},\n day: {self.day},\n dayNumber: {self.dayNumber},\n hourStart: {self.hourStart},\n hourEnd: {self.hourEnd},\n duration: {self.duration},\n width: {self.width},\n left: {self.left},\n"

    def __repr__(self):
        return f"courseCode: {self.courseCode},\n courseName: {self.courseName},\n date: {self.date},\n weekNumber: {self.weekNumber},\n day: {self.day},\n dayNumber: {self.dayNumber},\n hourStart: {self.hourStart},\n hourEnd: {self.hourEnd},\n duration: {self.duration},\n width: {self.width},\n left: {self.left},\n"
