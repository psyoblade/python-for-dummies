#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseArgParser:

    def __init__(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("--basedate", required=True, help="작업 수행 일자")
        parser.add_argument("--gamename", required=True, help="작업 수행을 위한 게임 목록")
        parser.add_argument("--basepath", default=".", help="프로그램 실행 경로 (절대 경로)")
        parser.add_argument("--config", default="./application.yml", help="데이터 소스 설정 파일 지정")
        self.parser = parser
        self.args = None

    def parse(self):
        config = self.parser.parse_args()
        yaml_path = config.config if config.config.startswith("/") else "/".join([config.basepath, config.config])
        config.yaml_path = yaml_path
        self.args = config
        return self.args
