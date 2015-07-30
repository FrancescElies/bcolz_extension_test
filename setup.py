from setuptools import setup, Extension
from Cython.Distutils import build_ext
from numpy.distutils.misc_util import get_numpy_include_dirs

# Sources & libraries
inc_dirs = ['my_extension']
lib_dirs = []
libs = []
def_macros = []
sources = ["my_extension/carray_ext.pyx"]

# Include NumPy header dirs
from numpy.distutils.misc_util import get_numpy_include_dirs
inc_dirs.extend(get_numpy_include_dirs())
optional_libs = []

# Sources

setup(
    name="my_package",
    description='My description',
    license='MY_LICENSE', 
    ext_modules=[
        Extension(
            "my_extension.carray_ext",
            include_dirs=inc_dirs,
            define_macros=def_macros,
            sources=sources,
            library_dirs=lib_dirs,
            libraries=libs,
        ),
    ],
    cmdclass={"build_ext": build_ext},
    packages=['my_extension', 'tests'],
)
