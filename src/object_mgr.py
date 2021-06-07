
import random
from .storage_handler import StorageHdl

class ObjectMgr:

    @classmethod
    def create_list(obj):
        return list(range(1, 10))

    def load_items(self):
        return StorageHdl().read()

    def get_object(self):
        items = self.load_items()
        selected = random.choice(items)
        items.remove(selected)
        StorageHdl().write(items)
        return selected

    def free_object(self, new_item:int):
        items = self.load_items()
        if not new_item in items:
            items.append(new_item)
            StorageHdl().write(items)
        return new_item
