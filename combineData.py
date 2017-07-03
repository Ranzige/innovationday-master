# -*- coding:utf-8 -*-
import rpi.sensortag
import webapp
import json
import sys

reload(sys)

sys.setdefaultencoding('utf-8')


def truckMessage():
    f = open('/Users/ibmstudio/Desktop/innovationday-master/static/truck.json', 'r')

    content = json.load(f)
    truck = json.dumps(content, sort_keys=True, ensure_ascii=False)
    truck = truck.split('[]')
    f.close()

    print truck
    return truck

def combineData(mes, environment):
    mes['environment'] = environment
    jsonData = json.dumps(mes, indent=4, ensure_ascii=False)
    print jsonData
    return jsonData


"""def main():
    environment = rpi.sensortag.main()
    mes = {
            "batch":"001101",
            "container":"01",
            "deliveryman":"IBM",
            "order":"056725",
            "vehicle":"辽B1289",
            "driver":"Maichel",
            "target":"上海",
            "start":"辽宁",
        }
    environment = {"h":20, "l":89.90}
    jsonData = combineData(mes, environment)
    return jsonData"""


if __name__ =='__main__':
    #main()
    truckMessage()
