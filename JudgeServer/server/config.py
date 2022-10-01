import os
import pwd

import grp

JUDGER_WORKSPACE_BASE = "/judger/run"
LOG_BASE = "/log"

COMPILER_LOG_PATH = os.path.join(LOG_BASE, "compile.log")
JUDGER_RUN_LOG_PATH = os.path.join(LOG_BASE, "judger.log")
SERVER_LOG_PATH = os.path.join(LOG_BASE, "judge_server.log")

RUN_USER_UID = pwd.getpwnam("code").pw_uid
RUN_GROUP_GID = grp.getgrnam("code").gr_gid

COMPILER_USER_UID = pwd.getpwnam("compiler").pw_uid
COMPILER_GROUP_GID = grp.getgrnam("compiler").gr_gid

SPJ_USER_UID = pwd.getpwnam("spj").pw_uid
SPJ_GROUP_GID = grp.getgrnam("spj").gr_gid

TEST_CASE_DIR = "/test_case"
SPJ_SRC_DIR = "/judger/spj"
SPJ_EXE_DIR = "/judger/spj"

CLANG_TIDY_CHECKS = "-*,bugprone-*,cert-dcl21-cpp,cert-dcl50-cpp,cert-env33-c,cert-err34-c,cert-err52-cpp,cert-err60-cpp,cert-flp30-c,cert-msc50-cpp,cert-msc51-cpp,cppcoreguidelines-*,-cppcoreguidelines-macro-usage,-cppcoreguidelines-pro-type-reinterpret-cast,-cppcoreguidelines-pro-type-union-access,-cppcoreguidelines-pro-bounds-pointer-arithmetic,-cppcoreguidelines-pro-type-vararg,google-readability-braces-around-statements,google-build-using-namespace,google-explicit-constructor,google-global-names-in-headers,google-readability-casting,google-runtime-int,google-runtime-operator,hicpp-*,-hicpp-vararg,misc-*,modernize-*,performance-*,readability-*,-readability-named-parameter"