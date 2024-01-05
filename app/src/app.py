# -*- coding: utf-8 -*-
from logging import getLogger, config, DEBUG
import os

import sys
from .model import PullRequestModel
from logutil import LogUtil
from importenv import ImportEnvKeyEnum

from util.sample import Util
from controller import CSVController, PullRequestController

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
LOG_CONFIG_FILE = ['config', 'log_config.json']

logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(os.path.join(PYTHON_APP_HOME, *LOG_CONFIG_FILE))
config.dictConfig(log_conf)
logger.setLevel(DEBUG)
logger.propagate = False

def main():
    args = sys.argv
    args_index = 1

    release_date = args[args_index]; args_index += 1
    logger.info(f'release_date : {release_date}')

    csv_path = os.path.join(PYTHON_APP_HOME, 'files', 'csv', f'apply_{release_date}.csv')
    logger.info(f'csv_path : {csv_path}')
    
    release_list = CSVController().load(csv_path)
    
    export_path = os.path.join(PYTHON_APP_HOME, 'files', 'export', f'{release_date}.tsv')
    logger.info(f'export_path : {export_path}')
    controller = PullRequestController(os.path.join(PYTHON_APP_HOME, 'files', 'export', f'{release_date}.tsv'))
    controller.update(release_list)
    controller.export_tsv()


if __name__ == '__main__':
    # 起動引数の取得
    # args = sys.argv
    # args[0]はpythonのファイル名。
    # 実際の引数はargs[1]から。
    
    logger.info('Start.')
    main()
    logger.info('Finish.')

