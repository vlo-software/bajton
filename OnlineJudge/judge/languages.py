from problem.models import ProblemIOMode


default_env = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]

_c_lang_config = {
    "template": """//PREPEND BEGIN
#include <stdio.h>
//PREPEND END

//TEMPLATE BEGIN
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//TEMPLATE END

//APPEND BEGIN
int main() {
  printf("%d", add(1, 2));
  return 0;
}
//APPEND END""",
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 256 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_c_lang_spj_compile = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 3000,
    "max_real_time": 10000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}"
}

_c_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_cpp_lang_config = {
    "template": """//PREPEND BEGIN
#include <iostream>
//PREPEND END

//TEMPLATE BEGIN
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//TEMPLATE END

//APPEND BEGIN
int main() {
  std::cout << add(1, 2);
  return 0;
}
//APPEND END""",
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 10000,
        "max_real_time": 20000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_cpp_lang_spj_compile = {
    "src_name": "spj-{spj_version}.cpp",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 10000,
    "max_real_time": 20000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}"
}

_cpp_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_java_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_csharp_lang_config = {
        "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.cs",
        "exe_name": "Main.exe",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": -1,
        "compile_command": "/usr/bin/mcs {src_path} -out:{exe_path}"
    },
    "run": {
        "command": "/usr/bin/mono {exe_path}",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_py3_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "__pycache__/solution.cpython-310.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python3.10 -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python3.10 {exe_path}",
        "seccomp_rule": "general",
        "env": default_env + ["PYTHONIOENCODING=utf-8"]
    }
}

_go_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.go",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/go build -o {exe_path} {src_path}",
        "env": ["GOCACHE=/tmp", "GOPATH=/tmp", "GOMAXPROCS=1"] + default_env
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "golang",
        # 降低内存占用
        "env": ["GODEBUG=madvdontneed=1", "GOMAXPROCS=1"] + default_env,
        "memory_limit_check_only": 1
    }
}

_perl_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.pl",
        "exe_name": "main.pl",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/perl -c {src_path}",
        "env": []
    },
    "run": {
        "command": "/usr/bin/perl {exe_path}",
        "seccomp_rule": "",
        "env": [],
        "memory_limit_check_only": 1
    }
}

_node_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.js",
        "exe_name": "main.js",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/node --check {src_path}",
        "env": default_env
    },
    "run": {
        "command": "/usr/bin/node {exe_path}",
        "seccomp_rule": "node",
        # 降低内存占用
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_ts_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.ts",
        "exe_name": "main.ts",
        "max_cpu_time": 6000,
        "max_real_time": 10000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/tsc --typeRoots /usr/lib/node_modules/@types --noEmit {src_path}",
        "env": default_env
    },
    "run": {
        "command": "/usr/bin/ts-node -T {exe_path}",
        "seccomp_rule": "node",
        # 降低内存占用
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_bf_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.b",
        "exe_name": "main",
        "max_cpu_time": 6000,
        "max_real_time": 10000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/python3.10 /tools/bfc.py {src_path} {exe_path}",
        "env": default_env
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

languages = [
    {"config": _c_lang_config, "spj": {"compile": _c_lang_spj_compile, "config": _c_lang_spj_config},
     "name": "C", "description": "GCC 9.4", "content_type": "text/x-csrc"},
    {"config": _cpp_lang_config, "spj": {"compile": _cpp_lang_spj_compile, "config": _cpp_lang_spj_config},
     "name": "C++", "description": "G++ 9.4", "content_type": "text/x-c++src"},
    {"config": _java_lang_config, "name": "Java", "description": "OpenJDK 17", "content_type": "text/x-java"},
    {"config": _csharp_lang_config, "name": "C#", "description": "Mono 4.6.2", "content_type": "text/x-csharp"},
    {"config": _py3_lang_config, "name": "Python3", "description": "Python 3.10", "content_type": "text/x-python"},
    {"config": _go_lang_config, "name": "Golang", "description": "Golang 1.17", "content_type": "text/x-go"},
    {"config": _perl_lang_config, "name": "Perl", "description": "Perl 5", "content_type": "text/x-perl"},
    {"config": _node_lang_config, "name": "JavaScript", "description": "Node 14", "content_type": "text/javascript"},
    {"config": _ts_lang_config, "name": "TypeScript", "description": "TS-Node", "content_type": "text/typescript"},
    {"config": _bf_lang_config, "name": "BrainFuck", "description": "BF Compiler", "content_type": "text/x-brainfuck"},
]
