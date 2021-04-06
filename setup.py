from setuptools import setup, find_packages


def readme():
    with open(r"README.md") as f:
        README = f.read()
    return README


def requirements():
    with open("requirements.txt", "r") as f:
        requirements = f.read()
    return requirements


setup(
    name="pyprofiles",
    packages=find_packages(),
    version="0.0.2",
    license="MIT",
    description="""Get social media profiles of anyone""",
    author="Shubhendra Kushwaha",
    author_email="shubhendrakushwaha94@gmail.com",
    url="https://github.com/TheShubhendra/profiles",
    keywords=[
        "social media",
        "quora",
    ],
    install_requires=requirements(),
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "License :: Free For Educational Use",
        "License :: Free For Home Use",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
