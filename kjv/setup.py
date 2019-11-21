from setuptools import setup

setup(
    name='kjv',
    version='0.1',
    packages=['kjv'],
    package_data={
        'kjv': [
            'data/*.bz2',
        ],
    },
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'kjv-init-db=kjv.shell:init_db',
        ],
    },
)
