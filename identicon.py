from hashlib import md5


def _svg(width, height, body, color):
    return """<?xml version="1.0"?>
    <svg width="{w}" height="{h}"
        viewBox="0 0 {w} {h}"
        viewport-fill="red"
        xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="{w}" height="{h}" fill="{color}"/>
    {body}
    </svg>""".format(w=width, h=height, body=body, color=color)


def _rect(x, y, width, height, color):
    return '<rect x="{}" y="{}" width="{}" height="{}" fill="{}"/>'.format(
        x, y, width, height, color
    )


def identicon(str_, size, background='#fff'):
    digest = int(md5(str_).hexdigest(), 16)
    color = '#{:06x}'.format(digest & 0xffffff)
    digest, body = digest >> 24, ''
    x = y = 0
    for t in range(size ** 2 // 2):
        if digest & 1:
            body += _rect(x, y, 1, 1, color)
            body += _rect(size - x - 1, y, 1, 1, color)
        digest, y = digest >> 1, y + 1
        x, y = (x + 1, 0) if y == size else (x, y)
    return _svg(size, size, body, background)


if __name__ == '__main__':
    print(identicon('The Holy Grail', 8, '#000'))
