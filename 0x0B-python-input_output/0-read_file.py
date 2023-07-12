#!/usr/bin/python3
  """Defines text file-read funcation."""


  def read_file(filename=""):
      """Prints content of a UTF8 text file to stdout."""
      with open(flename, encoding="utf-8") as f:
          print(f.read(), end="")
