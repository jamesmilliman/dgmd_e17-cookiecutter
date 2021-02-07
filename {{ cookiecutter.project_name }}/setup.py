from setuptools import setup

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1',
    py_modules=["{{ cookiecutter.project_name }}.py"],
    license='MIT',
    description='TODO',
    long_description=open('README.md').read(),
    install_requires=[],
    author='{{ cookiecutter.author_name|title }}',
    author_email='{{ cookiecutter.author_email }}'
)
