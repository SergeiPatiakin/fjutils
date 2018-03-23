from subprocess import call


def bash_quote(string):
    # TODO: proper quoting
    return string.replace("\\", "\\\\").replace("'", "\\'")


def call_bash(argv):
    return call(["bash"] + argv)
