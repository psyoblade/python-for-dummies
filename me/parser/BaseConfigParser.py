#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseConfigParser:

    def __init__(self, yaml_path):
        import os
        if not os.path.exists(yaml_path):
            raise RuntimeError("설정 파일을 읽을 수 없습니다 - {}".format(yaml_path))
        self.yaml_path = yaml_path
        self.config = None

    def parse(self):
        import yaml
        with open(self.yaml_path) as file:
            self.config = yaml.safe_load(file)
        return self

    def get_connector(self, name):
        found = list(filter(lambda conn: conn["name"] == name, self.config["connectors"]))
        if len(found) > 0:
            return found[0]
        else:
            raise RuntimeError("존재하지 않는 커넥터입니다 - {}".format(name))
