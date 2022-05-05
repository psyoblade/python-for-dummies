#!/usr/bin/env python
# -*- coding:utf-8 -*-
from me.parser import BaseArgParser as ap
from me.parser import BaseConfigParser as cp
from me.util import out


def main(basedate, gamename, configs):
    print(basedate, gamename)
    out.pprint(configs.get_connector("first-connector"))
    out.pprint(configs.get_connector("second-connector"))


if __name__ == "__main__":
    argParser = ap.BaseArgParser()
    args = argParser.parse()

    configParser = cp.BaseConfigParser(args.yaml_path)
    configs = configParser.parse()

    main(args.basedate, args.gamename, configs)
