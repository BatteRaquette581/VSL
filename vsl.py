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
import bool
arg = 5
blob = []
if arg == 5: 
  Console.out("foo")
if bool.Bool(blob): 
  Console.out("none")