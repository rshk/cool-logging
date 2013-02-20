from distutils.core import setup

setup(
    name='cool_logging',
    version=__import__('cool_logging').__version__,
    packages=['cool_logging'],
    url='https://github.com/rshk/cool-logging',
    license='GNU General Public License v3 or later (GPLv3+)',
    author='Samuele Santi',
    author_email='samuele@samuelesanti.com',
    description='',
    classifiers=[
        "License :: OSI Approved :: "
        "GNU General Public License v3 or later (GPLv3+)",
    ],
    install_requires=[
        "termcolor",
    ]
)
