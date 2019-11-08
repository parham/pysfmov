with open('README.rst', 'r') as f:
    readme = f.read()
    
def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')

#from distutils.core import setup, Extension
from setuptools import setup, Extension
from pysfmov import __version__
setup(name='pysfmov',
      version=__version__,
      author='',
      author_email='',
      description='',
      url='https://github.com/LolloCappo/pysfmov',
      py_modules=['pysfmov'],
      #ext_modules=[Extension('lvm_read', ['data/short.lvm'])],
      long_description=readme,
      install_requires=requirements
      )