import util
from func_cpp import FuncCpp
from func_go import FuncGolang

if __name__ == '__main__':
    filename = "testfiles/test.cpp"
    filetype = util.get_file_type(filename)
    if filetype == "cpp":
        f = FuncCpp(filename)
        f.start()
        f.draw()
    elif filetype == "go":
        f = FuncGolang(filename)
        f.start()
        f.draw()
    elif filetype == "py":
        # TODO
        pass
