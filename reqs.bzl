load("@rules_python//python:pip.bzl", "pip_parse")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

def load_reqs():
    compile_pip_requirements(
        name = "pyreqs",
        requirements_in = "//:requirements.txt",
        visibility = ["//visbibility:public"]
    )
