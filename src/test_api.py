from .storage_handler import StorageHdl
import pytest
from .app import create_app
from .schema import GetItemFromListQuery
from graphene import Schema


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_empty_db(client):
    rv = client.get('/')
    print(rv.data)
    assert b'Hello' in rv.data

def test_get_object():
    schema = Schema(query=GetItemFromListQuery, auto_camelcase=False)
    StorageHdl.create_dummy_dataset([1,2,3])

    stored_items = StorageHdl().read()
    assert len(stored_items) == 3

    query = """
    {
        get_object {
            obj
        }
    }
    """
    result = schema.execute(query)
    
    assert not result.errors
    assert 'get_object' in result.data.keys()
    assert 'obj' in  result.data['get_object'].keys()
    assert isinstance(result.data['get_object']['obj'], int)
    
    stored_items = StorageHdl().read()
    assert result.data['get_object']['obj'] not in stored_items
    assert len(stored_items) == 2

def test_free_object():
    schema = Schema(query=GetItemFromListQuery, auto_camelcase=False)
    StorageHdl.create_dummy_dataset([1,2,3])

    stored_items = StorageHdl().read()
    assert len(stored_items) == 3

    query = """
    {
        free_object(obj:144) {
            obj
        }
    }
    """
    result = schema.execute(query)
    
    assert not result.errors
    assert 'free_object' in result.data.keys()
    assert 'obj' in  result.data['free_object'].keys()
    assert isinstance(result.data['free_object']['obj'], int)
    assert result.data['free_object']['obj'] == 144 
    
    stored_items = StorageHdl().read()
    assert 144 in stored_items
    assert len(stored_items) == 4
