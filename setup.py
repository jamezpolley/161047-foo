from setuptools import setup

setup(name='foo',
      version='0.3',
      description='foo',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['foo'],
      zip_safe=False,
      install_requires=['bar>=2.1']
  )
