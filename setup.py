from setuptools import setup

setup(
    name='gen_data',
    version='0.0.1',
    author='Le Vuong Nguyen',
    author_email='vuong.se@gmail.com',
    url='https://github.com/patfinder/gen_data/',
    description='A convinient tool for generating big test data.',
    entry_points={
        'console_scripts': [
            'gen_data=gen_data:main'
        ]
    }
)
