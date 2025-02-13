from setuptools import setup, find_packages

import os

here = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='smartexecutor',
    version='0.1.0',
    description='A Python library to auto-select between ThreadPool and ProcessPool for task execution based on task type.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mezghenna Mohanned',
    author_email='mezh2911@gmail.com',
    url='https://github.com/Mohanned29/Limitations-of-Multithreading-in-Python-and-Task-Optimization',
    packages=find_packages(),
    install_requires=[
        'requests',
        'psutil'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8'
)
