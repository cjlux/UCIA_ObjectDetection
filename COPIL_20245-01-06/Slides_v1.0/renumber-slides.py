# renumber tle slides in a .tex file
#
# The lines with the slide number contain the tag "%====== #"

fileName = "slides.tex"

with open(fileName, "r", encoding="utf8") as F:
   lines = F.readlines()

with open("renum.tex", "w", encoding="utf8") as F:
   slide_num = 1
   for line in lines:
      if line.startswith("%====== #"):
         line = f"%====== #{slide_num:2d} "+ 50*"=" +"\n"
         slide_num += 1
      elif line.startswith("%======="):
         line = "%" + 61*"=" + "\n"
      F.write(line)
