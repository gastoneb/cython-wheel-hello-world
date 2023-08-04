import os

from Cython.Build import cythonize
from setuptools import Extension, setup, find_packages
from Cython.Distutils import build_ext

extensions = [
    Extension(
        "cython_wheel_hello_world",
        [os.path.join("cython_wheel_hello_world", "hello_world.pyx")],
    )
]

setup(
    name="cython_wheel_hello_world",
    version="0.1.0",
    description="Minimial example of how to build a cython project wheel file",
    license="MIT",
    packages=find_packages(),
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(extensions),
)
