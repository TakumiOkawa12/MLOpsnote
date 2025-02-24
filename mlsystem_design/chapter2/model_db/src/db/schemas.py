import datetime
from typing import Dict, Optional

from pydantic import BaseModel

# プロジェクトを新規で作成するときに必要な変数のみ定義
class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str]

# ProjectBaseを継承することで新規作成用クラスを用意
class ProjectCreate(ProjectBase):
    pass

# テーブルからデータを取得するためのPydanticモデル
# ProjectBaseクラスの変数に加えて、project_idとcreated_timeのデータもあるので定義する
class Project(ProjectBase):
    project_id: int
    created_datetime: datetime.datetime

    # SQLAlchemy の ORM オブジェクトを Pydantic モデルに変換できる
    class Config:
        orm_mode = True

class ModelBase(BaseModel):
    project_id: str
    model_name: str
    description: Optional[str]

class ModelCreate(ModelBase):
    pass

class Model(ModelBase):
    model_id: int
    created_datetime: datetime.datetime

    class Config:
        orm_mode = True

class ExperimentBase(BaseModel):
    model_id: str
    model_version_id: str
    parameters: Optional[Dict]
    training_dataset: Optional[str]
    validation_dataset: Optional[str]
    test_dataset: Optional[str]
    evaluations: Optional[Dict]
    artifact_file_paths: Optional[Dict]


class ExperimentCreate(ExperimentBase):
    pass

# 評価結果のみを持つモデル（部分的な更新や取得に使える）
class ExperimentEvaluations(BaseModel):
    evaluations: Dict

# モデルの保存パスのみを持つモデル
class ExperimentArtifactFilePaths(BaseModel):
    artifact_file_paths: Dict


class Experiment(ExperimentBase):
    experiment_id: int
    created_datetime: datetime.datetime

    class Config:
        orm_mode = True