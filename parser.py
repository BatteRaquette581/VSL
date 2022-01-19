def parse(base_code=[]):
  vsl = open("main.vsl","r")
  file = open("vsl.py","w")
  commands = open("commands.py","r")
  lines = vsl.readlines()
  file.writelines(commands.readlines())
  file.writelines("\n")
  spaces = 0
  space = 0
  code = []
  if base_code:
    for i in base_code:
      code.append(i)
  for i in lines:
    i = i.strip()
    if i[-1] in ("{","[","("):
      if i[-1] == "{":
        i = i[0:-1]+":"
      space = 1
    elif i[-1] in ("}",")","]"):
      if i[-1] == "}":
        i = i[0:-1]
      space = -1
    try:
      if i[-1] == ";":
        i = i[0:-1]
    except:
      pass
    if not i == "":
      code.append(spaces * " " + i)
    spaces += space*2
    space = 0
  file.writelines("\n".join(code))
  vsl.close()
