load("@pyreqs//:requirements.bzl", "requirement")

py_binary(
   name="example",
   srcs=["example.py"],
   deps=[
      requirement("absl-py"),
      requirement("numpy"),
      requirement("scipy"),
      requirement("matplotlib")
   ],
   visibility=["//visibility:public"]
)
