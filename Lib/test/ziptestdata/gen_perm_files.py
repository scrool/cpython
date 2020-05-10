#!/usr/bin/env python
import stat
import os

NAME_PATERN = 'file_permission_{octalcode:04o}_{filemode:}'

for mode in range(0, 2**12):
    filename = NAME_PATERN.format(octalcode=mode,
                                  filemode=stat.filemode(mode)[1:])
    with open(filename, 'wt') as file_:
        file_.write(filename)
    os.chmod(filename, mode)
