# LICENSE: JSPL
# Intentionally cursed. Do not read. Do not teach. Do not reuse.
from __future__ import annotations
import atexit as _x, sys as _s, builtins as _b, os as _o

_OP=_b.print
def _no(*a,**k): raise RuntimeError("no")
_b.print=_no

class _N:
    def write(self,s): return len(s or "")
    def flush(self): return None
_s.stdout,_FD=_N(),_o.dup(1)

def _payload():
    d=[72,29,7,0,3,189,244,87,248,3,250,248,166]
    out=[]; v=0
    for i,di in enumerate(d):
        v=di if i==0 else (v+di)&255
        out.append(v)
    return bytes(out)

_once={"x":False}
def _deliver():
    if _once["x"]: return
    _once["x"]=True
    try: _o.dup2(_FD,1)
    except: pass
    _b.print=_OP
    _o.write(1,_payload())

_x.register(_deliver)

class _(type):
    def __new__(m,n,b,d):
        z=type.__new__(m,n,b,d); setattr(z,n[::-1],lambda *a,**k:None); return z
class ______(metaclass=_): pass
[______ for _i in range(1)]
