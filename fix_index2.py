import re

with open("index.html", "r") as f:
    html = f.read()

# Fix the broken newsletter tag
broken_footer_pattern = r'<div class="column xl-3 lg-6 md-12 tab-12 s-footer__block s-footer__contact">.*?<div class="mc-status"></div>\s*</form>\s*</div>\s*</div>'

html = re.sub(
    broken_footer_pattern,
    '<div class="column xl-3 lg-6 md-12 tab-12 s-footer__block s-footer__contact">\n                    <h3>Contact</h3>\n                    <p><a href="mailto:mindful@hamednouri.com">mindful@hamednouri.com</a><br>+1 214 245 0784<br>Denton, TX</p>\n                </div>',
    html, flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(html)
print("Done fixing index.html")
