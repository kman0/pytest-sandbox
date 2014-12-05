# -*- coding: utf-8 -*-
"""
pytest-sandbox tests
********************

"""

pytest_plugins = 'pytester'
from pprint import pprint
from path import Path
__author__ = 'M'


def init_no_ini_config(testdir):
    testdir.makepyfile("""
    import inspect
    from path import Path
    def test_func_1():
        # print(inspect.stack()[0])
        # print(r'\\n')
        # print(Path.getcwd())
        assert Path.getcwd().name == inspect.stack()[0][3]
        assert Path.getcwd().parent.name == Path(__file__).name
        assert Path.getcwd().parent.parent.name == '.sandbox'
        assert Path.getcwd().parent.parent.name == '.sandbox'
    """)


def init_path_ini_config(testdir):
    testdir.tmpdir.ensure("pytest.ini").write("""[pytest]
sandbox_path=sand_box""")
    # print('\ninit tmp: %s' % testdir)
    testdir.makepyfile("""
    import inspect
    from path import Path
    def test_func_2():
        # print(Path.getcwd())
        assert Path.getcwd().name == inspect.stack()[0][3]
        assert Path.getcwd().parent.name == Path(__file__).name
        assert Path.getcwd().parent.parent.name == 'sand_box'
    """)


def test_no_configure_print(testdir):
    init_no_ini_config(testdir)
    result = testdir.runpytest(testdir.tmpdir)
    assert result.ret == 0
    result.stdout.fnmatch_lines_random("*sandbox: .sandbox*")


def test_folder_name(testdir):
    init_no_ini_config(testdir)
    result = testdir.runpytest(testdir.tmpdir)
    assert result.ret == 0

    result.stdout.fnmatch_lines_random("*1 passed*")
    result.stdout.fnmatch_lines_random("*test_folder_name*")
    result.stdout.fnmatch_lines_random("*sandbox: .sandbox*")


def test_folder_base_path(testdir):
    init_path_ini_config(testdir)
    result = testdir.runpytest(testdir.tmpdir)
    assert result.ret == 0
    result.stdout.fnmatch_lines_random("*1 passed*")
    result.stdout.fnmatch_lines_random("*test_folder_base_path*")
    result.stdout.fnmatch_lines_random("*sandbox: sand_box*")
