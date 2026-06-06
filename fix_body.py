t = open('templates/base.html', encoding='utf-8').read()
t = t.replace('<body>', '<body style="background:#0D0C1E;color:#EAE8FF">')
open('templates/base.html', 'w', encoding='utf-8').write(t)
print('FIXED!')