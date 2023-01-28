from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author
from typing import List


app = FastAPI()



@app.post('/book', response_model=Book, response_model_exclude_unset=False)
def create_book(item: Book):
    return item


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}

@app.get('/book')
def get_book(q: List[str] = Query(['test', 'test2'],
                            description="search book",)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk:int = Path(..., gt=1, le=20),
                    pages: int=Query(None,gt=10, le=500)):
    return {'pk': pk, 'pages': pages}
