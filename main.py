# import the necessary modules and libraries
import json, unittest, datetime

#use the open function to open read the three json files
with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)

# convert json data from format 1 to the expected format
def convertFromFormat1 (jsonObject):
    
    # IMPLEMENT: Conversion From Type 1

    # Extracting the various parts of the location (country, city, etc.) using the split method
    locationList = jsonObject.get('location').split('/')

    format1 = {
        "deviceID": jsonObject.get('deviceID'),
        "deviceType": jsonObject.get('deviceType'),
        "timestamp": jsonObject.get('timestamp'),
        "location": {
            "country": locationList[0],
            "city": locationList[1],
            "area": locationList[2],
            "factory": locationList[3],
            "section": locationList[4]
        },
        "data": {
            "status": jsonObject.get('operationStatus'),
            "temperature": jsonObject.get('temp')
        }
    }

    return format1

# convert json data from format 2 to the expected format
def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 2

    convertedTimestamp = 0

    format2 = {
        "deviceID": jsonObject.get('device').get('id'),
        "deviceType": jsonObject.get('device').get('type'),
        "timestamp": jsonObject.get('timestamp'),
        "location": {
            "country": jsonObject.get('country'),
            "city": jsonObject.get('city'),
            "area": jsonObject.get('area'),
            "factory": jsonObject.get('factory'),
            "section": jsonObject.get('section')
        },
        "data": {
            "status": jsonObject.get('data').get('status'),
            "temperature": jsonObject.get('data').get('temperature')
        }
    }

    return format2

def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


# Test cases using unittest module
class TestSolution(unittest.TestCase):

    # Sanity test to ensure the expected result is as intended
    # converts json data to python objects usnig json.loads and json.dumps
    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    # run the tests
    unittest.main()
