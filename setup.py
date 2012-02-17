from setuptools import setup

setup(
    name='tablesnap',
    version='0.2',
    author='Jeremy Grosser',
    author_email='jeremy@synack.me',
    scripts=['tablesnap'],
    data_files=[('/etc/tablesnap', ['tablesnap.conf'])],
    install_requires=[
        'pyinotify',
        'boto',
    ]
)
