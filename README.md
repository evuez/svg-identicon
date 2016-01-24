# Github-like SVG identicon generator.

Example:

```python
from identicon import identicon

print(identicon('The Holy Grail', 8, '#000'))
```

![Viking-style identicon!](http://i.imgur.com/2GnmWYt.png)
*(I really like that "The Holy Grail" gives such a nice viking-style head!)*

And here's the SVG:

```
<?xml version="1.0"?>
<svg width="8" height="8"
    viewBox="0 0 8 8"
    viewport-fill="red"
    xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="8" height="8" fill="#000"/>
    <rect x="0" y="4" width="1" height="1" fill="#855b60"/><rect x="7" y="4" width="1" height="1" fill="#855b60"/><rect x="0" y="6" width="1" height="1" fill="#855b60"/><rect x="7" y="6" width="1" height="1" fill="#855b60"/><rect x="0" y="7" width="1" height="1" fill="#855b60"/><rect x="7" y="7" width="1" height="1" fill="#855b60"/><rect x="1" y="0" width="1" height="1" fill="#855b60"/><rect x="6" y="0" width="1" height="1" fill="#855b60"/><rect x="1" y="1" width="1" height="1" fill="#855b60"/><rect x="6" y="1" width="1" height="1" fill="#855b60"/><rect x="1" y="2" width="1" height="1" fill="#855b60"/><rect x="6" y="2" width="1" height="1" fill="#855b60"/><rect x="1" y="3" width="1" height="1" fill="#855b60"/><rect x="6" y="3" width="1" height="1" fill="#855b60"/><rect x="1" y="4" width="1" height="1" fill="#855b60"/><rect x="6" y="4" width="1" height="1" fill="#855b60"/><rect x="1" y="5" width="1" height="1" fill="#855b60"/><rect x="6" y="5" width="1" height="1" fill="#855b60"/><rect x="1" y="6" width="1" height="1" fill="#855b60"/><rect x="6" y="6" width="1" height="1" fill="#855b60"/><rect x="1" y="7" width="1" height="1" fill="#855b60"/><rect x="6" y="7" width="1" height="1" fill="#855b60"/><rect x="2" y="0" width="1" height="1" fill="#855b60"/><rect x="5" y="0" width="1" height="1" fill="#855b60"/><rect x="2" y="3" width="1" height="1" fill="#855b60"/><rect x="5" y="3" width="1" height="1" fill="#855b60"/><rect x="2" y="4" width="1" height="1" fill="#855b60"/><rect x="5" y="4" width="1" height="1" fill="#855b60"/><rect x="2" y="6" width="1" height="1" fill="#855b60"/><rect x="5" y="6" width="1" height="1" fill="#855b60"/><rect x="2" y="7" width="1" height="1" fill="#855b60"/><rect x="5" y="7" width="1" height="1" fill="#855b60"/><rect x="3" y="2" width="1" height="1" fill="#855b60"/><rect x="4" y="2" width="1" height="1" fill="#855b60"/><rect x="3" y="3" width="1" height="1" fill="#855b60"/><rect x="4" y="3" width="1" height="1" fill="#855b60"/><rect x="3" y="4" width="1" height="1" fill="#855b60"/><rect x="4" y="4" width="1" height="1" fill="#855b60"/><rect x="3" y="5" width="1" height="1" fill="#855b60"/><rect x="4" y="5" width="1" height="1" fill="#855b60"/><rect x="3" y="7" width="1" height="1" fill="#855b60"/><rect x="4" y="7" width="1" height="1" fill="#855b60"/>
</svg>
```
