from dfd_common import process_lines, EntryType
from jinja2 import Template

tsv_file = open("../DFD.tsv", "r", encoding='utf8')
tsv_content = tsv_file.readlines()
entries = process_lines(tsv_content[306:])
radicals = process_lines(tsv_content[:305],True)
dict_entries = {}
dict_order = []
for r in radicals + entries:
    if (r.type in [EntryType.RADICAL,EntryType.NORMAL_CHARACTER]):
        for x in r.spit_rime():
            if (x[0] not in dict_entries):
                dict_order.append(x[0])
                dict_entries[x[0]] = []
            if (x[1] not in dict_entries[x[0]]):
                dict_entries[x[0]].append(x[1])

# DFD.html
f = open('./template/dfd.html.jinja2','r',encoding='utf-8')
t = Template(f.read())
f.close()
output = t.render(chars = entries, radicals = radicals)
f2 = open('../DFD.html',"w", encoding='utf8')
f2.write(output)
f2.close()
