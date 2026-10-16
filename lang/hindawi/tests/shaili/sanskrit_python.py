class गणक:
    def __init__(self, मान):
        self.मान = मान
    def जोड़(self, म):
        self.मान += म
        return self.मान

def मुख्य():
    ग = गणक(10)
    return ग.जोड़(5)
