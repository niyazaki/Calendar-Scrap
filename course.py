class Course:
    def __init__(self, *args, **kwargs):
        self.courseCode = kwargs.get("courseCode", "")
        self.courseName = kwargs.get("courseName", "")
        self.date = kwargs.get("date", None)
        self.weekNumber = int(kwargs.get("weekNumber", -1))
        self.day = kwargs.get("day", "")
        self.dayNumber = int(kwargs.get("dayNumber", -1))
        self.hourStart = kwargs.get("hourStart", "")
        self.hourEnd = kwargs.get("hourEnd", "")
        self.duration = kwargs.get("duration", "")
        self.width = int(kwargs.get("width", -1))
        self.left = int(kwargs.get("left", -1))
        self.location = kwargs.get("location", "")
        self.type = kwargs.get("type", "")

        self.weekDays = ["Lundi", "Mardi", "Mercredi",
                         "Jeudi", "Vendredi", "Samedi", "Dimanche"]

        if self.width and self.left:
            # print(self.left+1//self.width)
            self.dayNumber = (self.left+1)//self.width
            self.day = self.weekDays[self.dayNumber]

    def __str__(self):
        return f"courseCode: {self.courseCode},\n courseName: {self.courseName},\n date: {self.date},\n weekNumber: {self.weekNumber},\n day: {self.day},\n dayNumber: {self.dayNumber},\n hourStart: {self.hourStart},\n hourEnd: {self.hourEnd},\n duration: {self.duration},\n width: {self.width},\n left: {self.left},\n location : {self.location}"

    """
    def __repr__(self):
        return f"courseCode: {self.courseCode},\n courseName: {self.courseName},\n date: {self.date},\n weekNumber: {self.weekNumber},\n day: {self.day},\n dayNumber: {self.dayNumber},\n hourStart: {self.hourStart},\n hourEnd: {self.hourEnd},\n duration: {self.duration},\n width: {self.width},\n left: {self.left},\n location : {self.location}"
    """
    def __repr__(self):
        return f"courseCode: {self.courseCode},\n courseName: {self.courseName},\n weekNumber: {self.weekNumber},\n day: {self.day},\n hourStart: {self.hourStart},\n hourEnd: {self.hourEnd},\n duration: {self.duration},\n location : {self.location}"