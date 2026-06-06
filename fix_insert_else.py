t = open('templates/base.html', encoding='utf-8').read()
print("Has endif:", '{% endif %}' in t)
print("Has if user.is_authenticated:", 'user.is_authenticated' in t)

# Find {% endif %} near the end and insert else+block content before it
last_endif = t.rfind('{% endif %}')
print("Last endif position:", last_endif)
print("Content around last endif:")
print(t[last_endif-100:last_endif+50])