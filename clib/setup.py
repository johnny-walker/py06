from distutils.core import setup, Extension

# Generated C file: <module>_wrap.c
# Note the underscore prefix in the extension name
example_module = Extension('_example',
                                       sources=['example_wrap.cxx'])

setup(name='SpeedupPerformance',
      description='A package containing modules from c++.',
      ext_modules=[example_module],
)