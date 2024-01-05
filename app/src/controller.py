# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os
from .repository import PullRequestRepository

# import sys
from logutil import LogUtil

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

class PullRequestController():
    def __init__(self, export_path) -> None:
        self.repository = PullRequestRepository()
        self.export_path = export_path
        
    def update(self, pull_request: list):
        for pull_request in pull_request:
            self.repository.update(pull_request)
        self.repository.commit()

    def export_tsv(self):
        with open(self.export_path, 'w') as f:
            for pull_request in self.repository.get_list():
                f.write(pull_request.to_tsv() + '\n')
    
class CSVController():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def load(csv_path) -> list:
        csv_list = []
        for line in open(csv_path, 'r'):
            model = PullRequestController()
            model = model.set_tsv(line)
            
            csv_list.append(model)
        return csv_list
    
    @staticmethod
    def _convert_date(date):
        return date[0:4] + '/' + date[4:6] + '/' + date[6:8]
