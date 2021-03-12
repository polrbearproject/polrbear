#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

def getcommands(root):
    modfils = Path(root + '/mono/none/Commands').glob('**/*.cs')
    rtn = []
    for modfil in modfils:
        rtn.append(str('/'.join(modfil.parts)).replace('mono/none/Commands/', '').replace('.cs', ''))
    return rtn

def getmodules(root):
    modfils = Path(root + '/modules').glob('**/*.py')
    rtn = []
    for modfil in modfils:
        rtn.append(str('/'.join(modfil.parts)).replace('modules/', '').replace('.py', ''))
    return rtn
