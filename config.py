# Copyright 2024 The FCAV Authors. All rights reserved.
# Use of this source code is governed by a Apache2.0-style
# license that can be found in the LICENSE file.
#
# Time    : 2024/3/12 16:40
# Author  : linyf49@qq.com
# File    : config.py

# Config file
#
# Function invalid name:
#   1. cannot begin with digit
#   2. cannot use the key word in language
#   3. only include "0-9" "_" "A-Z" "a-z"
SUPPORT_MODE_FILE = 1
SUPPORT_MODE_TERM = 2   # To be discarded
SUPPORT_MODE_EDIT = 3
SUPPORT_LANG = {"cpp", "c++", "go", "golang", "py", "python"}

"""
Cpp Config
Function code style:    return_type function_name(parameter list)
    Example 1:          vector<string> split(char seq, int max_split) {
"""
FUNC_PATTERN_CPP = r"\s*([A-Za-z_]+\w*)\s+([A-Za-z_]+\w+[()]*)\s*\((.*?)\)\s*{*"
LOG_PATH_CPP = "log/cpp_log.log"
LOG_NAME_CPP = "func_cpp"
NODE_COLOR_CPP = "red"
EDGE_COLOR_CPP = "blue"
KEYWORD_SET_CPP = {
    "if",
    "int",
    "for",
    "do",
    "new",
    "try",
    "asm",
    "else",
    "char",
    "float",
    "long",
    "void",
    "short",
    "while",
    "double",
    "break",
    "typedef",
    "register",
    "continue",
    "catch",
    "signed",
    "unsigned",
    "auto",
    "static",
    "extern",
    "sizeof",
    "delete",
    "throw",
    "const",
    "class",
    "friend",
    "return",
    "switch",
    "public",
    "union",
    "goto",
    "operator",
    "template",
    "enum",
    "private",
    "volatile",
    "this",
    "virtual",
    "case",
    "default",
    "inline",
    "protected",
    "struct",
}

"""
Golang Config
Golang function code style:     func function_name(parameter list) (return list) {
    Example 1:                  func split(seq rune, max_split uint32) []string {
    Example 2:                  func split(seq rune) (int, []string) {
"""
FUNC_PATTERN_GOLANG = r"\s*func\s+([A-Za-z_]+\w*)\s*\((.*?)\)\s*\(*(.*?)\)*\s*{"
LOG_PATH_GOLANG = "log/golang_log.log"
LOG_NAME_GOLANG = "func_golang"
NODE_COLOR_GOLANG = "yellow"
EDGE_COLOR_GOLANG = "black"
KEYWORD_SET_GOLANG = {
    "import",
    "package",
    "chan",
    "const",
    "func",
    "interface",
    "map",
    "struct",
    "type",
    "var",
    "break",
    "case",
    "continue",
    "default",
    "defer",
    "else",
    "fallthrough",
    "for",
    "go",
    "goto",
    "if",
    "range",
    "return",
    "select",
    "switch",
}

"""
Python Config
Python function code style:     def function_name(param: param_type) -> return_type:
    Example 1:                  def search(self: List[str], string: str, pos: int) -> List[str]:
    Example 2:                  def dfs():
"""
FUNC_PATTERN_PYTHON = r"\s*def\s+([A-Za-z_]+\w*)\s*\((.*?)\)\s*[->]*\s*\(*(.*?)\)*\s*:"
LOG_PATH_PYTHON = "log/python_log.log"
LOG_NAME_PYTHON = "func_python"
# KEYWORD_SET_PYTHON = keyword.kwlist
NODE_COLOR_PYTHON = "green"
EDGE_COLOR_PYTHON = "pink"
