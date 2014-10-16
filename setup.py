from setuptools import setup


def listify(filename):
    return filter(None, open(filename, 'r').read().strip('\n').split('\n'))

setup(
    name="tensor",
    version='0.0.1',
    url='http://github.com/calston/tensor',
    license='MIT',
    description="A Twisted based monitoring agent for Riemann",
    author='Colin Alston',
    author_email='colin.alston@gmail.com',
    packages=[
        "tensor",
        "twisted.plugins",
    ],
    package_data={
        'twisted.plugins': ['twisted/plugins/tensor_plugin.py']
    },
    include_package_data=True,
    install_requires=listify('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
    ],
)