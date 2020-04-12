from setuptools import setup, find_packages

setup(
    name='lighthive',
    version='0.2.2',
    packages=find_packages('.'),
    url='http://github.com/emrebeylerhive/lighthive',
    license='MIT',
    author='emrebeylerhive',
    author_email='emrebeylerhive@proton.me',
    description='A light python client to interact with the HIVE blockchain',
    install_requires=["requests", "backoff", "ecdsa", "dateutils"],
    extras_require={
        'dev': [
            'requests_mock'
        ]
    }
)
