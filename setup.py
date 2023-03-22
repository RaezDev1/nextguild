[build-system]
requires = ["setuptools", "requests", "asyncio", "websockets"]
build-backend = "setuptools.build_meta"

[project]
name = "nextguild"
version = "1.0.1"
authors = [
    { name="Arjun Sharda", email="sharda.aj17@gmail.com" },
]
description = "Interactions with the Guilded API made simpler"
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/ArjunSharda/nextguild"
"Bug Tracker" = "https://github.com/ArjunSharda/nextguild/issues"
