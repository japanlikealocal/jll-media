import re,sys
out=[];prev=''
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.strip()
    if not line or '-->' in line or line.startswith(('WEBVTT','Kind:','Language:')) or line.isdigit(): continue
    line=re.sub(r'<[^>]+>','',line)
    if line!=prev and (not out or line not in out[-1]): out.append(line); prev=line
print(''.join(out))
