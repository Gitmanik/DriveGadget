################################################################################
#
# python-lumacore
#
################################################################################

PYTHON_LUMACORE_VERSION = 2.3.1
PYTHON_LUMACORE_SOURCE = luma.core-$(PYTHON_LUMACORE_VERSION).tar.gz
PYTHON_LUMACORE_SITE = https://files.pythonhosted.org/packages/a6/04/9fae1eed53f5e68fb19351575e7019747fc53d249f592fa7b0250c2ab1a0
PYTHON_LUMACORE_SETUP_TYPE = setuptools
PYTHON_LUMACORE_LICENSE = MIT
PYTHON_LUMACORE_LICENSE_FILES = LICENSE.rst

$(eval $(python-package))
