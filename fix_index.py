import re

with open("index.html", "r") as f:
    html = f.read()

# Replace About headline
html = re.sub(
    r'<h2 class="text-display-title">\s*An inspiring headline about yourself\.\s*</h2>',
    '<h2 class="text-display-title">\n                            I help people make their digital lives calmer, clearer, safer, and easier to maintain.\n                            </h2>',
    html
)

# Replace About text
html = re.sub(
    r'<div class="s-about__content-main grid-section-split__primary">.*?</div> <!-- end s-about__content-main -->',
    '''<div class="s-about__content-main grid-section-split__primary">
                            <p class="attention-getter">
                            Mindful computing is the practical work of reducing digital clutter, organizing information, improving privacy, choosing tools intentionally, and building workflows that support real life instead of overwhelming it. My work combines personal knowledge systems, AI workflows, device setup, privacy tools, and practical technical communication.
                            </p>
                        </div> <!-- end s-about__content-main -->''',
    html, flags=re.DOTALL
)

# Expertise Header
html = re.sub(
    r'<h2 class="text-display-title">\s*My key areas of expertise\.\s*</h2>',
    '<h2 class="text-display-title">\n                            Mindful Computing Services\n                            </h2>',
    html
)

# Expertise Items
services = [
    ("Digital Decluttering", "Organize files, apps, accounts, notes, and digital spaces into a structure that is easier to maintain."),
    ("Second Brain Setup", "Design Obsidian, PARA, notes, dashboards, and databases for projects, resources, meetings, and personal knowledge."),
    ("AI Workflow Setup", "Use AI tools to speed up writing, planning, research organization, workflows, and recurring tasks."),
    ("Privacy and Account Safety", "Set up password managers, 2FA, YubiKeys, aliases, VPNs, and safer account habits."),
    ("Family / Creative Business Systems", "Create practical systems for creative projects, family tasks, content planning, and digital resource libraries.")
]

services_html = '<div class="grid-list-items list-items show-ctr">\n'
for title, desc in services:
    services_html += f'''                                <div class="grid-list-items__item list-items__item">
                                    <div class="grid-list-items__title list-items__item-header">
                                        <h3 class="list-items__item-title">{title}</h3>
                                    </div>
                                    <div class="grid-list-items__text list-items__item-text">
                                        <p>{desc}</p>
                                    </div>
                                </div>\n'''
services_html += '                            </div> <!-- grid-list-items -->'

html = re.sub(
    r'<div class="grid-list-items list-items show-ctr">.*?</div> <!-- grid-list-items -->',
    services_html,
    html, flags=re.DOTALL
)

# Remove Clients Section completely
html = re.sub(
    r'<!-- clients\s*-*\s*-->\s*<section id="clients" class="s-clients">.*?</section> <!-- end s-clients -->',
    '',
    html, flags=re.DOTALL
)

# Remove Journal Section completely
html = re.sub(
    r'<!-- # journal\s*=*-->\s*<section id="journal" class="s-journal">.*?</section> <!-- end s-journal -->',
    '',
    html, flags=re.DOTALL
)

# Fix Footer site links -> remove Journal
html = re.sub(
    r'<li><a href="blog.html">Journal</a></li>',
    '',
    html
)
html = re.sub(
    r'<li><a href="https://www.dreamhost.com/r.cgi\?287326">DreamHost</a></li>',
    '',
    html
)

# Remove Header Journal link
html = re.sub(
    r'<li><a href="blog\.html">Journal</a></li>',
    '',
    html
)

# Fix Newsletter (remove it)
html = re.sub(
    r'<div class="column xl-3 lg-6 md-12 tab-12 s-footer__block s-footer__newsletter">.*?</div>',
    '<div class="column xl-3 lg-6 md-12 tab-12 s-footer__block s-footer__contact">\n                    <h3>Contact</h3>\n                    <p><a href="mailto:mindful@hamednouri.com">mindful@hamednouri.com</a><br>+1 214 245 0784<br>Denton, TX</p>\n                </div>',
    html, flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(html)

print("Done updating index.html")
