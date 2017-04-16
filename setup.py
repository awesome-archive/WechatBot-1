# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))


entry_points = [
    "wechatbot = wechatbot.bot:main"
]

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

requires = [
    "beautifulsoup4==4.5.1",
    "anyjson==0.3.3",
    "simplejson==3.7.3",
    "ujson==1.34",
    "pypng==0.0.18",
    "editdistance==0.3",
    "Pillow==4.0.0",
    "qrcode==5.3",
    "pytest==3.0.7",
    "enum34==1.1.6"
]

setup(
    name="wechatbot",
    version='1.0.4',
    description="a wechat bot developed for geeks",
    long_description=long_description,
    author="chuanwu",
    author_email="chuanwusun@gmail.com",
    keywords="wechat bot chatops",
    packages=['wechatbot'],
    license='MIT',
    url="https://github.com/chuanwu/WechatBot.py",
    entry_points={"console_scripts": entry_points},
    install_requires=requires
)
