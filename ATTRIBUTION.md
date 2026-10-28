# Attribution and third-party content

AwesomeFigures' original source code is distributed under the
[MIT license](LICENSE). That license does **not** relicense dependencies,
upstream palette definitions, fonts, journal templates, or user-provided
figures. The underlying dependencies retain their respective licenses.

## Built-in palette specifications

The named-palette module stores references and source links alongside
the original published colour coordinates:

| Palette family | Source |
| --- | --- |
| Okabe–Ito Color Universal Design | https://jfly.uni-koeln.de/color/ |
| Paul Tol Bright, High Contrast, Muted | https://sronpersonalpages.nl/~pault/ |
| Tableau 10 | https://www.tableau.com/blog/colors-upgrade-tableau-10-56782 |
| ColorBrewer Set2, Dark2, RdBu | https://colorbrewer2.org/ |
| Matplotlib sequential maps (viridis, cividis, plasma, magma, inferno) | https://matplotlib.org/stable/users/explain/colors/colormaps.html |

Named palettes are reproduced as reference specifications; continuous
maps are accessed from Matplotlib rather than redistributed as a new
independent implementation. Source attribution does not by itself establish
licensing or trademark permission for uses beyond this repository.

## Python and TeX dependencies

NumPy, Matplotlib, Colorspacious, Sphinx, Jupyter and optional PDF tools
are installed as dependencies. Their code and associated licensing terms
are not part of AwesomeFigures' MIT grant; consult each distribution's
metadata and license files. MiKTeX, TeX Live and any LaTeX journal classes
are external and may have different licenses and redistribution rules.

Do not bundle external journal class files, third-party font binaries,
publisher logos or screenshots without verifying permission and adding
their attribution and license terms here. User-supplied manuscript content
remains the user's responsibility.

Please report any missing attribution or licensing concern through a GitHub
issue (without publishing private material).
