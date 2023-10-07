class Song:
    def __init__(self, flags):
        self.flags = flags

    def find_flag(self, flag):
        if flag in self.flags:
            return self.flags[flag]
    
    
    
    
            