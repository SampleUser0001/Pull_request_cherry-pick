# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dataclasses import dataclass

@dataclass
class PullRequestModel():
    __tablename__ = 'pull_request'
    
    st = Column(String(1000), primary_key=True)
    e2euat = Column(String(10))
    e2euat_date = Column(String(1000))
    main = Column(String(10))
    main_date = Column(String(1000))
    
    def set_tsv(self, tsv, release_date):
        # TODO : 後で修正する
        tsv_list = tsv.split('\t')
        self.st = tsv_list[8]
        self.e2euat = tsv_list[9]
        self.main = tsv_list[10]
        
        if not (self.e2euat == None or self.e2euat == ''):
            self.e2euat_date = release_date
        else:
            self.e2euat = '未申請'
            self.e2euat_date = '未申請'
        
        if not (self.main == None or self.main == ''):
            self.main_date = release_date
        else:
            self.main = '未申請'
            self.main_date = '未申請'
        
    
    def to_tsv(self):
        return f'{self.st}\t{self.e2euat}\t{self.e2euat_date}\t{self.main}\t{self.main_date}'