# Lua escape
from jinja2.runtime import Undefined

# Based on code from https://gist.github.com/SegFaultAX/629a3a8c15b0fd188000
SPECIAL_DELIM = [("[{}[".format("=" * n), "]{}]".format("=" * n)) for n in range(10)]


def type_of(v, *types):
    return any(isinstance(v, t) for t in types)


def get_delim(s):
    if '"' not in s and "\n" not in s and "\\" not in s:
        return ('"', '"')
    for op, cl in SPECIAL_DELIM:
        if op not in s and cl not in s:
            if s.startswith("\n"):
                op += "\n"  # Newlines at the start of long strings are ignored
            return (op, cl)
    raise ValueError("could not find delimiter for string")


def indent(s, level, prefix="  "):
    return "\n".join("{}{}".format(prefix * level, l).rstrip()
                     for l in s.split("\n"))


def to_lua(v):
    if v is None or isinstance(v, Undefined):
        return "nil"
    elif type_of(v, bool):
        return v and "true" or "false"
    elif type_of(v, str):
        od, cd = get_delim(v)
        return "{}{}{}".format(od, v, cd)
    elif type_of(v, float, int):
        return "{}".format(v)
    elif type_of(v, dict):
        kvs = []
        for k, v in v.iteritems():
            ks = "{}".format(to_lua(k))
            if ks.startswith("["):
                ks = "[ {} ]".format(ks)
            else:
                ks = "[{}]".format(ks)
            vs = to_lua(v)
            kvs.append("{} = {}".format(ks, vs))
        return "{{\n{}\n}}".format(indent(",\n".join(kvs), 1))
    elif type_of(v, list, tuple, set):
        kvs = []
        for i, v in enumerate(v):
            ks = "[{}]".format(i + 1)
            vs = to_lua(v)
            kvs.append("{} = {}".format(ks, vs))
        return "{{\n{}\n}}".format(indent(",\n".join(kvs), 1))
    else:
        raise TypeError("unable to convert python value of type '{}' to lua".format(type(v)))


class FilterModule(object):
    def filters(self):
        return {
            'to_lua': to_lua
        }
