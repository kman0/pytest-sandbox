# -*- coding: utf-8 -*-
"""
pytest-sandbox
**************

"""
from __future__ import print_function
import os
import sys
from path import Path
import pytest


__author__ = 'M'


def pytest_addoption(parser):
    parser.addoption(
        '--no-sandbox', action="store_false", dest="sandbox", default=True,
        help="disable pytest-sandbox"
    )
    parser.addini("sandbox_path", "path to sandbox dir")


@pytest.fixture(autouse=True)
def enter_sandbox(request, pytestconfig):
    if not pytestconfig.option.sandbox:
        return
    if 'sandbox_path' in pytestconfig.inicfg:
        sandbox_prefix = pytestconfig.inicfg['sandbox_path']
    else:
        sandbox_prefix = '.sandbox/'

    pytestconfig._sandbox_old_dir = Path.getcwd()

    mod_dir, _, func = request.node.nodeid.partition('::')
    sand_path = Path(Path(sandbox_prefix).joinpath(Path(mod_dir).joinpath(func))).abspath()

    if sand_path.isdir():
        sand_path.removedirs_p()
    elif sand_path.isfile():
        sand_path.remove_p()
    sand_path.makedirs_p()

    os.chdir(sand_path)
    print('cwd: %s' % os.getcwd())

    def exit_sandbox():
        os.chdir(pytestconfig._sandbox_old_dir)
        print('teardown cwd: %s' % os.getcwd())
        pytestconfig._sandbox_old_dir = None
    request.addfinalizer(exit_sandbox)
