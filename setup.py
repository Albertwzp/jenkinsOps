# -*- coding: utf-8 -*-

from setuptools import setup

# 需要导入的包名，多层子目录也是需要写的
packages = ["jenkinsOps"]
# 需要导入的静态文件
file_data = [
    ("README.md"),
]
# 第三方依赖
requires = [
    "python-jenkins>=1.7.0"
    "json"
]
# 自动读取version信息
about = {
"__title__": "jenkinsOps",
"__version__": "0.1",
"__description__": "jenkins operator",
"__author__": "Albertwzp",
"__author_email__": "albert.wzp@gmail.com",
"__url__": "https://github.com/Albertwzp/jenkinsOps"
}
#with open(os.path.join('.', __version__.py), r, 'utf-8') as f:
#    exec(f.read(), about)

# 自动读取readme
#with open('RAEDME.md', 'r', 'utf-8') as f:
#    readme = f.read()
setup(
    name = about["__title__"],
    version = about["__version__"],
    description = about["__description__"],
    author = about["__author__"],
    author_email = about["__author_email__"],
    url = about["__url__"],
    data_files = file_data,
    include_package_data = False,
    packages = packages,
    python_requires = ">=3.0",
    install_requires = requires,
    zip_safe = False,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
