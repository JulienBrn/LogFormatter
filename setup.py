from distutils.core import setup


setup(
    name='logformatter',
    packages=['logformatter'],
    version='0.1',
    license='MIT',
    description = 'A very simple log formatter for the logging module that can be used as is',
    author="Julien Braine",
    author_email='julienbraine@yahoo.fr',
    url='https://github.com/JulienBrn/LogFormatter',
    download_url = 'https://github.com/JulienBrn/LogFormatter.git',
    package_dir={'': 'src'},
    keywords=['python',  'logging'],
    install_requires=["logging", "termcolor"],
)