# cython-wheel-hello-world

cython-wheel-hello-world aims to demonstrate a minimal correct project structure and wheel file build procedure for cython projects. Python packaging has evolved with PEP 517 and PEP 518 (etc.) and the introduction of [the many packaging tools listed by the Python Packaging Authority](https://packaging.python.org/en/latest/key_projects/#pypa-projects), and meanwhile there is a lot of outdated or incorrect guidance online.

This small cython project generates wheel files using setuptools (including setup.py to configure the cython extensions), pyproject.toml (to configure a virtual env for building the wheel file), MANIFEST.in (so the compiled cython code is packaged with the wheel file), and using either [build](https://pypa-build.readthedocs.io/en/stable/index.html) or [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/) to build the wheel files.

## Instructions

The wheel file for this project can be built using _build_:

`python -m build`

Or alternatively, using _cibuildwheel_ (note: if using Windows or Mac OS, docker is required if the platform option is set to `linux`):

`cibuildwheel --platform=linux --output-dir=dist`

The wheel file can then be installed:

`pip install dist/cython_wheel_hello_world[versioning_info].whl`

Finally, the code can be run:

```
> from cython_wheel_hello_world import hello_world
> hello_world()
Hello, world!
```

## Further information

- Juan José García Ripoll's project [cython_example](https://github.com/juanjosegarciaripoll/cython_example) provides a more complete example.
- [PyPa's guide for packing modules that include binary extensions](https://packaging.python.org/en/latest/guides/packaging-binary-extensions/)
