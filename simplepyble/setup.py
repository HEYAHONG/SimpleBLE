import pathlib
import sys
import setuptools

here = pathlib.Path(__file__).parent.resolve()

# Include our vendorized copy of cmake-build-extension, at least until
# https://github.com/diegoferigo/cmake-build-extension/pull/35 is merged.
sys.path.insert(0, str(here))
import cmake_build_extension

# Get the long description from the README file
long_description = (here / "README.rst").read_text(encoding="utf-8")

cmake_options = []
if sys.platform == "win32":
    cmake_options.append("-DCMAKE_SYSTEM_VERSION=10.0.19041.0")
elif sys.platform.startswith("darwin"):
    cmake_options.append("-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15")

# The information here can also be placed in setup.cfg - better separation of
# logic and declaration, and simpler if you include description/version in a file.
setuptools.setup(
    name="simplepyble",
    version="0.0.6.dev0",  # ! Ensure it matches the intended release version!
    author="Kevin Dewald",
    author_email="kevin@dewald.me",
    description="The ultimate fully-fledged cross-platform BLE library, designed for simplicity and ease of use.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    ext_modules=[
        cmake_build_extension.CMakeExtension(
            name="simplepyble",
            disable_editable=True,
            source_dir=here,
            cmake_depends_on=["pybind11"],
            cmake_configure_options=cmake_options,
            cmake_generator="Visual Studio 16 2019" if sys.platform == "win32" else "Ninja",
        )
    ],
    cmdclass={
        "build_ext": cmake_build_extension.BuildExtension
    },
    zip_safe=False,
    extras_require={},
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
)