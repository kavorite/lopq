from setuptools import setup

setup(
    name='lopq',
    version='1.0.0',
    description='yahoo lopq for product quantization',
    url='https://github.com/anas-899/lopq.git',
    author='Clayton Mellina,Yannis Kalantidis,Huy Nguyen',
    author_email='clayton@yahoo-inc.com',
    license='Apache-2.0',
    packages=[
        'lopq'
    ],
    install_requires=[
        'protobuf>=3.11',
        'numpy>=1.15',
        'scipy>=0.14',
        'scikit-learn>=0.18'
    ]
)
