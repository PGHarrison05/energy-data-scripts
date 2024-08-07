from process.heat import get_eligibility04
import json 

with open("./test.json") as raw_data:
    data = json.loads(raw_data.read())
    print(get_eligibility04(data).value)