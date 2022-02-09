from random import choice as rc

class word:
    def __init__(self):
        self.__master_list = [
        "cross",
        "skin",
        "soup",
        "stupid", 
        "film", 
        "physics", 
        "clerk", 
        "kick", 
        "yard", 
        "plant", 
        "reserve", 
        "trouble", 
        "might", 
        "upper", 
        "finance", 
        "today", 
        "quarter", 
        "rate", 
        "revenue", 
        "nothing", 
        "possibility", 
        "split", 
        "team", 
        "towel", 
        "chapter", 
        "singer", 
        "promise", 
        "spare", 
        "cross", 
        "extreme", 
        "trick", 
        "recording", 
        "press", 
        "west", 
        "fix", 
        "insurance", 
        "abroad", 
        "finger", 
        "jacket",
        "secure", 
        "commercial", 
        "live", 
        "tremendous", 
        "specific", 
        "equal", 
        "fascinated", 
        "right", 
        "late", 
        "current", 
        "active", 
        "inner", 
        "novel", 
        "period", 
        "agent", 
        "puzzled", 
        "stupid", 
        "nasty", 
        "that", 
        "corner"
        ]
        self.__chosen_word = ""

    def choose_word(self):
        self.__chosen_word = rc(self.__master_list)

    def check_char(self,char):
        if char in self.__chosen_word:
            return True
        else:
            return False

    def get_word(self):
        return self.__chosen_word
    