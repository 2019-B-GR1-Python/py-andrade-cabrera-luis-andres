from datetime import datetime
class Stand_ability:
    def __init__(self, name,stand_id, description='unknown',id="unknown"):
        if id == "unknown":
            current_time = datetime.now()
            id = current_time.strftime("%Y%m%d%H%M%S%f")
        self.id = id
        self.name = name
        self.stand_id = stand_id
        self.description = description
