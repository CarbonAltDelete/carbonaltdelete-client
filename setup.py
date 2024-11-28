from setuptools import setup, find_packages

RELEASE = "v2024.11.2"
setup(
    name="Carbon+Alt+Delete Client",
    version=RELEASE[1:],
    description="Client SDK to communicate with the Carbon+Alt+Delete API",
    url="https://github.com/CarbonAltDelete/carbonaltdelete-client",
    author="Carbon+Alt+Delete",
    author_email="support@carbonaltdelete.eu",
    license="MIT",
    packages=find_packages(
        include=[
            "carbon_alt_delete",
            "carbon_alt_delete.*",
        ],
    ),
    install_requires=[
        "pydantic[email]",
        "python-jose",
        "requests",
        "rich",
    ],
)
