import json 
import os 


class StorageHdl:
    
    storage_file = "data.json"

    @classmethod
    def create_dummy_dataset(obj, data):
        if os.path.exists(obj.storage_file):
            os.remove(obj.storage_file)
        with open(obj.storage_file, 'w') as outfile:
            json.dump(data, outfile)

    def write(self, data):
        with open(self.storage_file, 'w') as outfile:
            json.dump(data, outfile)
    
    def read(self):
        with open(self.storage_file) as json_file:
            data = json.load(json_file)
        return data
