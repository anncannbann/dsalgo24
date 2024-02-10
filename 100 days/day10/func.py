
def FormatLine(fname,lname):

  new_fname = fname.title()
  new_lname = lname.title()

  return new_fname + " " + new_lname


fname = input('Enter first name')
lname = input('Enter last name')

print(FormatLine(fname,lname))
