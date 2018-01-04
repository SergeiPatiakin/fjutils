from subprocess import call

def bash_quote(string):
    # TODO: proper quoting
    return string.replace("'", "\\'")

def call_bash(argv):
    return call(["bash"] + argv)
