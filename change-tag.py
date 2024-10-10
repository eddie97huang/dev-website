import sys

def replace_tag(line):
  return line.replace("awscmhinfra2", "shared-qa-rad-consumer-awscmhinfra3")
  
with open(sys.argv[2], 'w') as output_file:
  with open(sys.argv[1], 'r') as input_file:
    in_tags = False
    for line in input_file:
      if in_tags:
        if line.lstrip().startswith("-"):
          line = replace_tag(line)
        else:
          in_tags = False
      if "tags:" in line:
        if "[" in line:
          line = replace_tag(line)
        else:
          in_tags = True
      output_file.write(line)
