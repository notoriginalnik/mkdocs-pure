# MkDocs Pure Theme

Theme free from JavaScript and external links.

[site example](https://notoriginalnik.github.io/)

[![PyPI Downloads][pypi-dl-image]][pypi-dl-link]
[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-dl-image]: https://img.shields.io/pypi/dm/mkdocs-pure.png
[pypi-dl-link]: https://pypi.python.org/pypi/mkdocs-pure
[pypi-v-image]: https://img.shields.io/pypi/v/mkdocs-pure.png
[pypi-v-link]: https://pypi.python.org/pypi/mkdocs-pure

## Installation

First, install the package via PyPI:

```sh
pip3 install mkdocs-pure
```

Then include the theme in your `mkdocs.yml` file:

```yaml
theme:
  name: pure
```
Or clone for custom:

```sh
git clone https://github.com/notoriginalnik/mkdocs-pure
pip3 install .
```

Use `pip install` for win.

## auto dark and light mode

```css
:root {
  color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  :root {
  --main-bg-color: black;
  --text-color: white;
  --code-color: #0f0;
  --details-color: #432;
  }
}
@media (prefers-color-scheme: light) {
  :root {
  --main-bg-color: ffd;
  --text-color: black;
  --code-color: green;
  --details-color: #ffe;
  }
  /* bug */
  #menu {
	background: #fff;
}
```

## Customize

Change colors and sidebar-width at ./css/theme.ccss

## Blog

For simple blogging prefer naming like logs YYYY-MM-DD-*.md:
```
docs/
    2015-10-30.md
    2018-12-31.md
    2019-01-02.md

or
docs/
    2015/10-30.md
    2018/12-31.md
    2019/01-02.md

or even
docs/
    2015/10/30.md
    2018/12/31.md
    2019/01/02.md
```

## Template blocks

Theme provide the standart blocks:

    site_meta: Contains meta tags in the document head.
    htmltitle: Contains the page title in the document head.
    styles: Contains the link tags for stylesheets.
    libs: Contains the JavaScript libraries (jQuery, etc) included in the page header.
    scripts: Contains JavaScript scripts which should execute after a page loads.
    analytics: Contains the analytics script.
    extrahead: An empty block in the <head> to insert custom tags/scripts/etc.
    site_name: Contains the site name in the navigation bar.
    site_nav: Contains the site navigation in the navigation bar.
    search_button: Contains the search box in the navigation bar.
    next_prev: Contains the next and previous buttons in the navigation bar.
    repo: Contains the repository link in the navigation bar.
    content: Contains the page content and table of contents for the page.
    footer: Contains the page footer.


## links

1. [mkdocs-basic-theme](https://mkdocs.github.io/mkdocs-basic-theme/)
1. [pure-css repository](https://github.com/pure-css/pure)
1. [pure-css site](https://purecss.io/)
1. [side-menu](https://purecss.io/layouts/side-menu/)
1. [CSS-SideBar-Toggle](https://codepen.io/swastikyadav/pen/zYZPyrN)
1. [example css menu](https://blog.logrocket.com/create-responsive-mobile-menu-with-css-no-javascript/)
1. [dark mode](https://css-tricks.com/a-complete-guide-to-dark-mode-on-the-web/#aa-using-a-body-class)
1. [layout blog](https://purecss.io/layouts/blog/)
1. [repository layout blog](https://github.com/pure-css/pure/tree/master/site/static/layouts/blog)
1. [blogging-plugin](https://github.com/liang2kl/mkdocs-blogging-plugin)
1. [blogging-plugin-example](https://github.com/liang2kl/mkdocs-blogging-plugin-example)
1. [git-revision-date-plugin](https://github.com/zhaoterryy/mkdocs-git-revision-date-plugin/tree/master)
1. [material theme request git-revision-date-plugin](https://github.com/squidfunk/mkdocs-material/issues/1350)
1. [material theme blog](https://www.codeinsideout.com/blog/#page1)

## Notes

```
v0.1
remove search
remove js
store all files localy
added sidebar
toogle sidebar
auto resize site for mobile
auto dark and light mode

v0.2
added simple blog
```