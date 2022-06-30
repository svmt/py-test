"""Web server"""

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """Read root"""
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, query: Union[str, None] = None):
    """Get item by ID"""
    return {'item_id': item_id, 'query': query}
