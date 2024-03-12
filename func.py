# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : func.py
class Func:
    def __init__(self, fid: int, name: str, param: str, ret: str, lineno: int):
        self.id = fid
        self.name = name
        self.param = param
        self.ret = ret
        self.line_num = lineno

    def to_str(self):
        return (
            "Get function {}: line:{}, name:{}, parameters:{}, return_type:{}".format(
                self.id, self.line_num, self.name, self.param, self.ret
            )
        )
