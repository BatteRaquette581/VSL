import sys
class Console:
  def out(arg):
    global can_print
    can_print = True
    print(arg)
    can_print = False
def print(arg):
  if can_print:
    sys.stdout.write(str(arg)+"\n")