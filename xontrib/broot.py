import builtins
import os
import subprocess
import tempfile


def _br(args, stdin, stdout, stderr):
    cmd_file = tempfile.NamedTemporaryFile(delete=False)

    try:
        cmds = ("broot", "--outcmd", cmd_file.name) + tuple(args)
        if builtins.__xonsh__.env.get("XONSH_INTERACTIVE"):
            cmds += ("--color", "yes")
        subprocess.call(
             cmds,
            stdin=stdin, stderr=stderr, stdout=stdout,
        )
        builtins.evalx(cmd_file.read().decode())
    finally:
        os.remove(cmd_file.name)

builtins.aliases["br"] = _br
