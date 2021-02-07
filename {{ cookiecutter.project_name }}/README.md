# {{ cookiecutter.project_name }}

{{ cookiecutter.project_name }} is a python project for the Spring 2021 semester of the `DGMD E-17` (Robotics, Autonomous Vehicles, Drones, and Artficial Intelligence) course.
{% if cookiecutter.library_or_application == "Library" %}
## Installation

`python setup.py install`
{% endif %}
## Usage

`python {{ cookiecutter.project_name }}.py`

## Development Setup

To install all development dependencies:

`pip install -r requirements.txt`

To run the tests (verbose):

`py.test -s -v {{ cookiecutter.project_name }}tests.py`

## Release History

TODO

## Meta
Generated using cookiecutter template generated here: 
{{ cookiecutter.author_name|title }} - {{ cookiecutter.author_email }}
Distributed under the MIT license. See [`LICENSE`](./LICENSE) for more information.
