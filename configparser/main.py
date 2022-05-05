#!/usr/bin/env python
# -*- coding:utf-8 -*-


def load_config():
    import yaml
    with open("application.yml") as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    import json
    config = load_config()
    print(json.dumps(config, indent=2, sort_keys=False))
    for connector in config['connectors']:
        if connector["name"] == "first-connector":
            print(connector["user"])
            print(connector["pass"])
