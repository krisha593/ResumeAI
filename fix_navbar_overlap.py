t = open('templates/base.html', encoding='utf-8').read()
# The navbar should only show for non-authenticated users
# Make sure {% else %} separates them properly
print("Has else:", '{% else %}' in t)
print("block content count:", t.count('{% block content %}'))