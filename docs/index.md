# pinax-blog

Originally named `biblion`, the eldarion.com blog app intended to be suitable
for site-level company and project blogs, is now known as `pinax-blog`.

## Installation

Install the development version:

    pip install pinax-blog

Add `pinax-blog` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # ...
        "pinax.blog",
        # ...
    )

Optionally, if you want `creole` support for a mark up choice:

    pip install creole


NOTE: the `creole` package does not support Python 3


## Dependencies

* `django-appconf>=1.0.1`
* `Pillow>=2.0`
* `Markdown>=2.6`
* `Pygments>=2.0.2`