#!/usr/bin/env python

import sys
import traceback

try:
  from cli import CommandLineRunner

  if __name__ == "__main__":
    runner = CommandLineRunner()
    runner.run(sys.argv)
    # Keeps the console from closing (until the user hits enter) so they can
    # read any console output
    print("")
    print("Close the window, or hit enter to exit...")
    input()
except Exception as e:
  stderr = sys.stderr
  with open('error.log', 'w') as f:
    sys.stderr = f
    traceback.print_exc()
    sys.stderr = stderr
  traceback.print_exc()
  print("")
  print("An error has occurred! A copy of the crash report has been saved to 'error.log'.")
  print("If this continues please submit an issue on our Github page (http://github.com/scottrice/Ice)")
  input()
