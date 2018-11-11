from string import Template
s = Template('$who likes $what')
to_print = s.substitute(who='tim', what='kung pao')
print(s.template)
print(to_print)
