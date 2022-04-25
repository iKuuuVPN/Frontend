import re
import os
import requests

FONTS_SAVE_PATH = "../../fonts/fontim/"
REWRITE_URL_PREFIX = '/gh/iKuuuVPN/Frontend@master/theme/malio/fonts/fontim/'


def find_font_url_in_content(content: str):
    for font_url in re.findall(r'url\((.*?)\)', css):
        font_url = font_url.replace('"', '').replace("'", '')
        if font_url.startswith('//'):
            font_url = 'http:' + font_url
        if font_url.startswith('http'):
            yield font_url


def dump_font(url: str, path: str):
    response = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response.content)


all_font_css = filter(lambda x: x.endswith(".css"), os.listdir())
for font_css in all_font_css:
    with open(font_css, 'r') as f:
        css = f.read()

        backup_current_css = font_css.replace('.css', '_backup.css')
        with open(backup_current_css, 'w') as f:
            f.write(css)

        for font_url in find_font_url_in_content(css):
            print(font_url)

            os.makedirs(os.path.join(FONTS_SAVE_PATH, font_css.replace('.css', '')), exist_ok=True)
            dump_font(
                font_url,
                os.path.join(FONTS_SAVE_PATH, font_css.replace('.css', ''), font_url.split('/')[-1])
            )

            css = css.replace(font_url, REWRITE_URL_PREFIX + font_css.replace('.css', '') + '/' + font_url.split('/')[-1])
        print(css)

    with open(font_css, 'w') as f:
            f.write(css)
