from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import JSON
from src.db.database import Base

# ORMとは，Object Relational Mapperのことで，簡単に説明すると，テーブルとクラスを1対1に対応させて，そのクラスのメソッド経由でデータを取得したり，変更したりできるようにする存在

class Project(Base):
    __tablename__ = "projects" # SQLAlchemy の ORM モデルでテーブル名を指定するための単なるクラス変数

    project_id = Column(
        String(255),
        primary_key = True,
        comment = "主キー",
    )
    project_name = Column(
        String(255),
        nullable  = False,
        unique = True,
        comment = "プロジェクト名",
    )
    description = Column(
        Text,
        nullable = True,
        comment = "説明",
    )
    created_datetime = Column(
        DateTime(timezone = True),
        server_default = current_timestamp(),
        nullable = False,
    )


class Model(Base):
    __tablename__ = "models"

    mdoel_id = Column(
        String(255),
        primary_key = True,
        comment = "主キー",
    )
    project_id = Column(
        String(255),
        ForeignKey("projects.project_id"),
        nullable = False,
        comment = "外部キー",
    )
    model_name = Column(
        String(255),
        nullable = False,
        comment = "モデル名"
    )
    description = Column(
        Text,
        nullable = True,
        comment = "説明",
    )
    created_datetime = Column(
        DateTime(timezone = True),
        servre_default = current_timestamp(),
        nullable = False
    )

class Experiment(Base):
    __tablename__ = "experiments"

    experiment_id = Column(
        String(255),
        primary_key=True,
        comment="主キー",
    )
    model_id = Column(
        String(255),
        ForeignKey("models.model_id"),
        nullable=False,
        comment="外部キー",
    )
    model_version_id = Column(
        String(255),
        nullable=False,
        comment="モデルの実験バージョンID",
    )
    parameters = Column(
        JSON,
        nullable=True,
        comment="学習パラメータ",
    )
    training_dataset = Column(
        Text,
        nullable=True,
        comment="学習データ",
    )
    validation_dataset = Column(
        Text,
        nullable=True,
        comment="評価データ",
    )
    test_dataset = Column(
        Text,
        nullable=True,
        comment="テストデータ",
    )
    evaluations = Column(
        JSON,
        nullable=True,
        comment="評価結果",
    )
    artifact_file_paths = Column(
        JSON,
        nullable=True,
        comment="モデルファイルのパス",
    )
    created_datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )