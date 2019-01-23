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

def sample_metric():
    series = Series(["SBvalue"], 1, 2, 3, 2)
    baseData = BaseData("MessageCount", "SomeNamespace", ["SBname"], [series])
    data = Data(baseData)
    azureMonitor = AzureMonitor(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"), data)

    return json.dumps(azureMonitor, default=lambda o: o.__dict__)