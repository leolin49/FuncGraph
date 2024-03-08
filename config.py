# Config file


"""
Cpp Config
Cpp function code style:    return_type function_name(parameter list)
    Example 1:              vector<string> split(char seq, int max_split) {
"""
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
FUNC_PATTERN_CPP = r"\s*(\w+)\s+(\w+)\s*\((.*?)\)\s*{*"
LOG_PATH_CPP = "log/cpp_log.log"
LOG_NAME_CPP = "func_cpp"

"""
Golang Config
Golang function code style:     func function_name(parameter list) (return list) {
    Example 1:                  func split(seq rune, max_split uint32) []string {
    Example 2:                  func split(seq rune) (int, []string) {
"""
FUNC_PATTERN_GOLANG = r"\s*func\s+(\w+)\s*\((.*?)\)\s*\(*(.*?)\)*\s*{"
LOG_PATH_GOLANG = "log/golang_log.log"
LOG_NAME_GOLANG = "func_golang"
