t = open('templates/base.html', encoding='utf-8').read()
print("Current block content count:", t.count('{% block content %}'))
print("Has else:", '{% else %}' in t)
print("Has include navbar:", 'partials/navbar' in t)

# Find where {% else %} is and what comes after it
if '{% else %}' in t:
    idx = t.index('{% else %}')
    print("After else:")
    print(t[idx:idx+200])