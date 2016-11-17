from __future__ import division
from __future__ import print_function

try:
    long(1)
except NameError:
    long = int # pylint: disable=redefined-builtin

# http://code.activestate.com/recipes/577081-humanized-representation-of-a-number-of-bytes/
def humanize_bytes(b, precision=1):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1<<long(50), 'PB'),
        (1<<long(40), 'TB'),
        (1<<long(30), 'GB'),
        (1<<long(20), 'MB'),
        (1<<long(10), 'kB'),
        (1, 'bytes')
    )
    if b == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if b >= factor:
            break
    return '%.*f %s' % (precision, b / factor, suffix) # pylint: disable=undefined-loop-variable
