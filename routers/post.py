from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from routers.schemas import PostBase, PostDisplay
from db.database import get_db
from fastapi.exceptions import HTTPException
from db import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
    return db_post.create_post(db, request)

