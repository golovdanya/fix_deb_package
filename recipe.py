"""
Development container image
"""

Stage0 += baseimage(image='ubuntu:16.04')

# GNU compilers
compiler = gnu()
Stage0 += compiler

# Additional development tools
Stage0 += packages(ospackages=['autoconf', 'autoconf-archive', 'automake',
                               'bzip2', 'ca-certificates', 'cmake', 'git',
                               'gzip', 'libtool', 'libssl-dev', 'make',
                               'patch', 'xz-utils', 'zlib1g-dev'])
# Download and build cpython
Stage0 += generic_build(branch='v3.6.5',
                        build=['./configure', 'make install'],
                        repository='https://github.com/python/cpython.git')
Stage0 += shell(commands=['python3 -m pip install requests'])
