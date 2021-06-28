from setuptools import setup

setup(
    name='pyxosnip',
    version='1.1.0',
    author='Leo Izen',
    author_email='leo.izen+maintainer@gmail.com',
    url='https://github.com/thebombzen/PyXOSnip',
    download_url='https://github.com/thebombzen/PyXOSnip/archive/1.1.0.tar.gz',
    keywords=['screenshot', 'screen-recording', 'scrot', 'cli'],
    packages=['pyxosnip'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'PyGObject',
      'xcffib',
      'pycairo',
    ],
    entry_points={
        'console_scripts': [
            'pyxosnip = pyxosnip.main:run',
        ],
    }
)
