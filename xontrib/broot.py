import builtins
import os
import subprocess
import tempfile
from xonsh.built_ins import XSH


def _br(args, stdin=None, stdout=None, stderr=None):
    cmd_file = tempfile.NamedTemporaryFile(delete=False)

    try:
        cmds = ("broot", "--outcmd", cmd_file.name) + tuple(args)
        if builtins.__xonsh__.env.get("XONSH_INTERACTIVE"):
            cmds += ("--color", "yes")
        subprocess.call(
            cmds,
            stdin=stdin,
            stderr=stderr,
            stdout=stdout,
        )
        builtins.evalx(cmd_file.read().decode())
    finally:
        os.remove(cmd_file.name)


builtins.aliases["br"] = _br


@XSH.builtins.events.on_ptk_create
def custom_keybindings(bindings, **kw):
    def handler(key_name: str, default: str):
        def do_nothing(_):
            pass

        if key_name not in XSH.env:
            key = default
        else:
            key = XSH.env.get(key_name)
        if key:
            return bindings.add(key)
        return do_nothing

    @handler("XONSH_BROOT_KEY", "c-n")
    def start_broot(event):
        _br([])
