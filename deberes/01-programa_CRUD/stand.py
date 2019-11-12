from datetime import datetime
class Stand:
    def __init__(self,name,user_id,appearance = "unknown",stand_cry = "unknown",origin="unknown",id="unknown"):
        if id == "unknown":
            current_time = datetime.now()
            id = current_time.strftime("%Y%m%d%H%M%S%f")
        self.id = id
        self.name = name
        self.user_id = user_id
        self.appearance = appearance
        self.stand_cry = stand_cry
        self.origin=origin
