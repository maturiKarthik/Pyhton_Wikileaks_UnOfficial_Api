import json

import Const
from WikiLeaks import WikiLeaksData

wld = WikiLeaksData()

print json.dumps(wld.get_leaks("+-Government-+.html"))
