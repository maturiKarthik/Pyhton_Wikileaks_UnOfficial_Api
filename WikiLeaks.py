from Leaks import Leaks
from Topics import Topics


# Entry class
class WikiLeaksData(Leaks, Topics):

    def __init__(self):
        Leaks.__init__(self)
        Topics.__init__(self)
