from setuptools import setup
setup(name='uzerp',
      version='21.7.3',
      packages=['uzerp'],
      entry_points={
          'console_scripts': [
              'uzerp = uzerp.__main__:main'
          ]
      },
      install_requires=[
          'fire',
          'xdg'
      ],
      include_package_data=True,
      )
