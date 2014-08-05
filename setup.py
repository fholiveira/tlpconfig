from pip.req import parse_requirements
from setuptools import setup


install_reqs = [str(ir.req) for ir in parse_requirements('requirements.txt')]
VERSION = open('VERSION').read()


setup(
  name = 'tlpconfig',
  packages = ['tlp'],
  version = VERSION,
  license='BSD',
  author='Fernando Oliveira',
  author_email='fernando@fholiveira.com',
  description='A GTK+ 3.10 app to configure TLP.',
  long_description=open('README.md').read(),
  install_requires=list(install_reqs),
  url = 'https://github.com/fholiveira/tlpconfig',
  download_url = 'https://github.com/fholiveira/tlpconfig/tarball/' + VERSION,
  keywords = ['battery', 'saving', 'energy', 'tlp', 'gtk'],
  classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Intended Audience :: End Users/Desktop'
  ]
)
