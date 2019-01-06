from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pack',
      version='0.1',
      description='test packaging',
      long_description=long_description,
      url='https://github.com/snans666/pack',
      author='snans666',
      author_email='a@b.c',
      license='MIT',
      packages=['pack'],
      dependency_links=['https://github.com/snans666/pack/blob/master/dist/pack-0.1-py3-none-any.whl'],
      zip_safe=False)
