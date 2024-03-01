# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker

from .model import PullRequestModel
import os
from sqlalchemy import create_engine

from importenv import ImportEnvKeyEnum

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')


class PullRequestRepository():
    def __init__(self) -> None:
        engine = create_engine('sqlite://' + os.path.join(PYTHON_APP_HOME, *ImportEnvKeyEnum.DB_PATH), echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get(self, st):
        return self.session.query(PullRequestModel).filter(PullRequestModel.st == st).first()

    def get_list(self):
        return self.session.query(PullRequestModel).all()

    def add(self, pull_request):
        self.session.add(pull_request)
    
    def update(self, pull_request):
        self.session.merge(pull_request)
    
    def delete(self, pull_request):
        self.session.delete(pull_request)
    
    def commit(self):
        self.session.commit()
    
    def rollback(self):
        self.session.rollback()
        
    def close(self):
        self.session.close()