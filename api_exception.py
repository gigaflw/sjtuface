#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by BigFlower at 16/7/30
import json


def api_error_type(e):
    if json.loads(e.body)['error_code'] == 1503:
        return NameExistError


class NameExistError(Exception):
    pass
