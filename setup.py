import setuptools

pkg_name = "reactopya"

setuptools.setup(
    name=pkg_name,
    version="0.2.5",
    author="Jeremy Magland",
    author_email="jmagland@flatironinstitute.org",
    description="",
    packages=setuptools.find_packages(),
    scripts=['bin/reactopya'],
    package_data={
        'reactopya': ['templates/*']
    },
    include_package_data=True,
    install_requires=[
        "jinja2"
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    )
)
