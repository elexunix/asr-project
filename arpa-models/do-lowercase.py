import sys, os

uppercase_lm = sys.argv[1]
lowercase_lm = 'lowercase-' + uppercase_lm
if not os.path.exists(lowercase_lm):
  with open(uppercase_lm, 'r') as f_upper:
    with open(lowercase_lm, 'w') as f_lower:
      for line in f_upper:
        f_lower.write(line.lower())
