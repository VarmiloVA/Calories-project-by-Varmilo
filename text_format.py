def format_low(*t):
    """DEVUELVE EL TEXTO PASADO POR LOWER Y STRIP"""
    for ts in t:
        ts = ts.lower()
        ts = ts.strip()
        return ts

def format_tit(*txt):
    """DEVUELVE EL TEXTO PASADO POR TITLE Y STRIP"""
    for tst in txt:
        tst = tst.title()
        tst = tst.strip()
        return tst

def format_up(*text):
    """DEVUELVE EL TEXTO PASADO POR UPPER Y STRIP"""
    for tsxt in text:
        tsxt = tsxt.upper()
        tsxt = tsxt.strip()
        return tsxt