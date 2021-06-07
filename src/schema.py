from .object_mgr import ObjectMgr
from graphene import ObjectType, String, Schema, Int, List, Field


class ListItem(ObjectType):
    obj = Int()


class ListItemQuery(ObjectType):
    get_object = Field(ListItem)
    free_object = Field(ListItem, obj=Int())
    list_objects = List(ListItem)
    

    def resolve_get_object(self, info):
        return ListItem(obj=ObjectMgr().get_object())
    
    def resolve_free_object(self, info, obj):
        return ListItem(obj=ObjectMgr().free_object(obj))
    
    def resolve_list_objects(self, info):
        return [ListItem(item) for item in ObjectMgr().load_items()]


class GetItemFromListQuery(ListItemQuery, ObjectType):
    pass

schema = Schema(query=GetItemFromListQuery, auto_camelcase=False)

