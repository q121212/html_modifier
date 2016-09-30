from cx_Freeze import setup, Executable

setup(
  name = "html_modifier",
  version = "0.1",
  author = "Max Rekunchak",
  description = "html_modifier for MGTS",
  executables = [Executable("html_modifier.py")]
)