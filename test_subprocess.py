# -*- coding: utf-8 -*-

import subprocess as sp


def readGitVersion():
    proc = sp.Popen("ls tests/",
    				 shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = proc.communicate()
    if proc.returncode != 0:
        raise Exception("ls command call failed %d %s %s" % (proc.returncode, output, error))
    return output.splitlines()[0].strip()

if __name__ == '__main__':
    print(readGitVersion())
