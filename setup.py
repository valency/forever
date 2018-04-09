from distutils.core import setup

setup(
    name='forever',
    version='0.4.5',
    packages=['.'],
    url='https://github.com/valency/forever',
    download_url = 'https://github.com/valency/forever/releases/download/v0.4.5/forever-0.4.5.tar.gz',
    license='CPL-3.0',
    author='Deepera Co., Ltd.',
    author_email='yding@deepera.com',
    description='Forever: auto restart any script when it stops printing.',
    keywords = ['forever', 'logging', 'auto-restart'],
    install_requires=[]
)
