from setuptools import setup, find_packages

setup(
    name="eodp-students",
    version="0.1.0",
    description="Earth Observation Data Processing Students Package",
    author="Student",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib",
        "netCDF4",
    ],
    include_package_data=True,
    package_data={
        "auxiliary": ["*.conf", "equalization/*.nc", "isrf/*.nc"],
    },
)
