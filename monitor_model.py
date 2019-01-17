import json, datetime

class MonitorModel:
    def __init__(self):
        self.AzureMonitor = "AzureMonitor"
        self.Data = "Data"
        self.BaseData = "BaseData"
        self.Series = Series

class AzureMonitor:
    def __init__(self, time, Data):
        self.time = time
        self.data = Data

class Data:
    def __init__(self, BaseData):
        self.baseData = BaseData

class BaseData:
    def __init__(self, metric, namespace, dimNames, Series):
        self.metric = metric
        self.namespace = namespace
        self.dimNames = dimNames
        self.series = Series

class Series:
    def __init__(self, dimValues, min, max, sum, count):
        self.dimValues = dimValues
        self.min = min
        self.max = max
        self.sum = sum
        self.count = count

series = Series(["SB value"], 1, 2, 3, 2)
baseData = BaseData("Message Count", "Some Namespace", ["SB name"], [series])
data = Data(baseData)
azureMonitor = AzureMonitor(datetime.datetime.now().isoformat(), data)

print(json.dumps(azureMonitor, indent=4, default=lambda o: o.__dict__))