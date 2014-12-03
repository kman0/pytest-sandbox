# -*- coding: utf-8 -*-
"""
pytest-sandbox tests
********************

"""

pytest_plugins = 'pytester'


__author__ = 'M'


def test_folder_name(testdir):
    testdir.makepyfile("""
    import inspect
    from path import Path
    def test_func_1():
        assert Path.getcwd().name == inspect.stack()[0][3]
        assert Path.getcwd().parent.name == Path(__file__).name
        assert Path.getcwd().parent.parent.name == '.sandbox'
        assert Path.getcwd().parent.parent.name == '.sandbox'

    """)
    result = testdir.runpytest(testdir.tmpdir)
    assert result.ret == 0
    result.stdout.fnmatch_lines_random("*1 passed*")
    result.stdout.fnmatch_lines_random("*test_folder_name*")


def test_folder_base_path(testdir):
    testdir.tmpdir.ensure("pytest.ini").write("""[pytest]
sandbox_path=sandbox""")

    testdir.makepyfile("""
    import inspect
    from path import Path
    def test_func_1():
        print(Path.getcwd())
        assert Path.getcwd().name == inspect.stack()[0][3]
        assert Path.getcwd().parent.name == Path(__file__).name
        assert Path.getcwd().parent.parent.name == 'sandbox'

    """)
    result = testdir.runpytest(testdir.tmpdir)
    assert result.ret == 0
    result.stdout.fnmatch_lines_random("*1 passed*")
    result.stdout.fnmatch_lines_random("*test_folder_name*")

