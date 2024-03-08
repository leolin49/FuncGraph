class Func:
    def __init__(self, fid: int, name: str, param: str, ret: str, lineno: int):
        self.id = fid
        self.name = name
        self.param = param
        self.ret = ret
        self.line_num = lineno

    def to_str(self):
        return "Get function {}: line:{}, name:{}, parameters:{}, return_type:{}".format(
            self.id, self.line_num, self.name, self.param, self.ret
        )
