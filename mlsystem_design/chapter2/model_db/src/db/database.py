import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.configurations import DBConfigurations

# DBエンジンのインスタンスを作成
engine = create_engine(
    DBConfigurations.sql_alchemy_database_url,
    pool_recycle = 3600,
    echo = False,
)
# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルベースクラスの作成。このベースクラスを拡張（継承）するとテーブルに対応するクラスを作れる。
Base = declarative_base()

# FastAPIのDepends(get_db)で使用
def get_db():
    db = SessionLocal()
    try:
        yield db # セッションを一時的に提供
    except:
        db.rollback() # 例外発生時にトランザクションを取り消す
        raise
    finally:
        db.close()

# pythonコードでwith get_context_db():で使用可能。 with文でデータベースセッションを管理できる
@contextmanager
def get_context_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()