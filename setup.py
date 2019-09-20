from setuptools import setup, find_packages

setup(
    name='multivisor',
    version='5.0.2.1',
    author='Tiago Coutinho',
    author_email='coutinhotiago@gmail.com',
    description='A centralized supervisor UI (web & CLI)',
    packages=find_packages(),
    package_data={'multivisor.server': ['dist/*',
                                        'dist/static/css/*',
                                        'dist/static/js/*']},
    entry_points=dict(console_scripts=[
        'multivisor=multivisor.server.web:main',
        'multivisor-cli=multivisor.client.cli:main']),
    install_requires=['flask==1.1.1', 'gevent==1.4.0', 'supervisor==4.0.4', 'zerorpc==0.6.3', 'blinker==1.4',
                      'maya==0.6.1', 'requests==2.22.0', 'prompt_toolkit>=2.0.0,<2.1.0'])
