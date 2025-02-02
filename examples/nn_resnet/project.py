#!/usr/bin/env python
#-*- coding = utf-8 -*-

#
# @file from https://github.com/Neutree/c_cpp_project_framework
# @author neucrack
# @license Apache 2.0
#

import sys, os

sdk_env_name = "LIBMAIX_SDK_PATH"

# get SDK absolute path
sdk_path = os.path.abspath(sys.path[0]+"/../../")

try:
    sdk_path = os.environ[sdk_env_name]
except Exception:
    pass
print("-- SDK_PATH:{}".format(sdk_path))

# tool chain staging dir
os.environ["STAGING_DIR"] = "build"

# execute project script from SDK
project_file_path = sdk_path+"/tools/cmake/project.py"
with open(project_file_path) as f:
    exec(f.read())

