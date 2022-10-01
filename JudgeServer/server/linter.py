from unittest import result
import _judger
import os

from config import CLANG_TIDY_CHECKS, COMPILER_LOG_PATH, COMPILER_USER_UID, COMPILER_GROUP_GID
from exception import CompileError
import shlex


class Linter(object):
    def lint(self, src_path, output_dir):
        command = """/usr/bin/clang-tidy -checks="{clang_tidy_checks}" {src_path}"""
        command = command.format(src_path=src_path, clang_tidy_checks=CLANG_TIDY_CHECKS, exe_dir=output_dir)
        compiler_out = os.path.join(output_dir, "compiler.out")
        _command = shlex.split(command)

        os.chdir(output_dir)
        env = ["PATH=" + os.getenv("PATH")]
        result = _judger.run(max_cpu_time=8000,
                             max_real_time=8000,
                             max_memory=1024 * 1024 * 1024,
                             max_stack=128 * 1024 * 1024,
                             max_output_size=20 * 1024 * 1024,
                             max_process_number=_judger.UNLIMITED,
                             exe_path=_command[0],
                             # /dev/null is best, but in some system, this will call ioctl system call
                             input_path=src_path,
                             output_path=compiler_out,
                             error_path="/dev/null",
                             args=_command[1::],
                             env=env,
                             log_path=COMPILER_LOG_PATH,
                             seccomp_rule_name=None,
                             uid=COMPILER_USER_UID,
                             gid=COMPILER_GROUP_GID)

        with open(compiler_out, encoding="utf-8") as f:
            result = f.read().strip()
            os.remove(compiler_out)
            return result
