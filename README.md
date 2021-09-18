# Overview
[broot](https://github.com/Canop/broot) support function for xonsh shell


## Installation

To install use pip:

``` bash
xpip install xontrib-broot
# or: xpip install -U git+https://github.com/jnoortheen/xontrib-broot
```

## Usage
It adds `br` alias function. So commands like `cd` will work from broot.
``` bash
$ xontrib load broot
$ br 
```

`broot` can also be launched with shortcut `Ctrl+N`. 
This can be changed by `$XONSH_BROOT_KEY="c-n"` or disabled with `$XONSH_BROOT_KEY=""`. 
(PS [PTK's keybinding guide](https://python-prompt-toolkit.readthedocs.io/en/master/pages/advanced_topics/key_bindings.html#list-of-special-keys) 
for full list of key names.)

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/jnoortheen/xontrib-cookiecutter).
