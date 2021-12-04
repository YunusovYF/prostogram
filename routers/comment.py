from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_comment
from routers.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user



router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.post('')
def create_comment(request: CommentBase,
                db: Session = Depends(get_db),
                current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create_comment(db, request)


@router.get('/all/{post_id}')
def get_all_comments_for_post(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all_comments_for_post(db, post_id)