from setuptools import find_packages, setup

setup(
  name='Janky Chatroom',
  version='1.0.0',
  packages=find_packages(),
  entrypoints={
    'console_scripts': [
      'boot = python boot_client.py --connect client_config.json',
    ],
  },
)
