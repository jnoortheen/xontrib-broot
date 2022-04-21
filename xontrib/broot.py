import os
import subprocess
import tempfile
from xonsh.built_ins import XSH
from xonsh.tools import uncapturable
from contextlib import contextmanager


@contextmanager
def mk_temp_file() -> str:
    fd, file_name = tempfile.mkstemp()
    os.close(fd)
    yield file_name
    os.remove(file_name)


@uncapturable
def _br(args, stdin=None, stdout=None, stderr=None):
    with mk_temp_file() as cmd_file:
        cmds = ("broot", "--outcmd", cmd_file) + tuple(args)
        status_code: int = subprocess.call(
            cmds,
            stdin=stdin,
            stderr=stderr,
            stdout=stdout,
        )
        if status_code == 0:
            with open(cmd_file) as fr:
                content = fr.read()
                if content:
                    XSH.builtins.evalx(content)

    return status_code


XSH.aliases["br"] = _br


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


if __name__ == "__main__":
    from xonsh.built_ins import XSH

    XSH.load()
    data = XSH.execer.eval("")
