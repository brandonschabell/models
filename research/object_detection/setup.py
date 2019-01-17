from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='object_detection',
    version='0.0.3',
    packages=find_packages(exclude='dist'),
    url='https://github.com/brandonschabell/models/tree/master/research/object_detection',
    license='Apache License 2.0',
    author='Brandon Schabell',
    author_email='brandonschabell@gmail.com',
    description="A package build from Tensorflow's object detection API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'tensorflow',
        'Cython',
        'contextlib2',
        'pillow',
        'lxml',
        'jupyter',
        'matplotlib'
    ],
    python_requires='>=3.5, !=3.7.*',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)
