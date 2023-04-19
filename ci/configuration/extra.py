PLUGINS = ['netbox_slm']
DEBUG = True
SECRET_KEY = 'dummy'
DEVELOPER = True
PLUGINS_CONFIG = {
    'netbox_slm': dict(
        TEST_RUNNER='xmlrunner.extra.djangotestrunner.XMLTestRunner',
        TEST_OUTPUT_DIR='/ci/reports/',
        TEST_OUTPUT_FILE_NAME='junit.xml',
    )
}
