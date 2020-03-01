def pytest_addoption(parser):
    parser.addoption('--username', action='append', help='GMail Username',required=True)
    parser.addoption('--password', action='append', help='GMail Password',required=True)
    parser.addoption('--to',required=True,action='append',default=[], help='To (multiple allowed)')
    parser.addoption('--cc',action='append',default=[], help='Cc (multiple allowed)')
    parser.addoption('--subject', action='append', required=True, help='Subject')
    parser.addoption('--body', action='append', help='Message Body (text)')
    parser.addoption('--html',default=None, help='Message Body (html)')


def pytest_generate_tests(metafunc):
    # if "username" in metafunc.fixturenames:
    for parameter in ("username", "password", "to", "subject", "body"):
        metafunc.parametrize(parameter, metafunc.config.getoption(parameter))