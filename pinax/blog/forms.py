from django import forms
from django.utils import timezone
from django.utils.functional import curry
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .models import Post, Revision, Section
from .signals import post_published
from .utils import load_path_attr

# kwaddle specific customizations (use CKEditor)
from ckeditor_uploader.widgets import CKEditorUploadingWidget

FIELDS = [
    "section",
    "author",
    "markup",
    "title",
    "slug",
    "content",
    "description",
    "state"
]


class PostFormMixin(object):

    @property
    def markup_choice(self):
        return self.cleaned_data["markup"]

    def __init__(self, *args, **kwargs):
        super(PostFormMixin, self).__init__(*args, **kwargs)
        post = self.instance
        latest_revision = post.latest()
        if latest_revision:
            self.fields["content"].initial = latest_revision.content

    def save_post(self, post):
        published = False

        if post.pk is None or Post.objects.filter(pk=post.pk, published=None).count():
            if self.cleaned_data["state"] == Post.STATE_CHOICES[-1][0]:
                post.published = timezone.now()
                published = True

        render_func = curry(
            load_path_attr(
                settings.PINAX_BLOG_MARKUP_CHOICE_MAP[self.markup_choice]["parser"]
            )
        )

        post.content_html = render_func(self.cleaned_data["content"])
        post.updated = timezone.now()
        post.save()

        r = Revision()
        r.post = post
        r.title = post.title
        r.content = self.cleaned_data["content"]
        r.author = post.author
        r.updated = post.updated
        r.published = post.published
        r.save()

        if published:
            post_published.send(sender=Post, post=post)

        return post


class AdminPostForm(PostFormMixin, forms.ModelForm):

    title = forms.CharField(
        label=_("Title"),
        max_length=90,
        widget=forms.TextInput(attrs={"style": "width: 50%;"}),
    )
    slug = forms.CharField(
        label=_("Slug"),
        widget=forms.TextInput(attrs={"style": "width: 50%;"})
    )
    content = forms.CharField(
        label=_("Content"),
        widget=CKEditorUploadingWidget()
        #widget=forms.Textarea(attrs={"style": "width: 80%; height: 300px;"})
    )
    description = forms.CharField(
        label=_("Description"),
        widget=forms.Textarea(attrs={"style": "width: 80%;"}),
        required=False
    )

    class Meta:
        model = Post
        fields = FIELDS

    class Media:
        js = settings.PINAX_BLOG_ADMIN_JS

    def save(self, blog=None):
        post = super(AdminPostForm, self).save(commit=False)
        if blog:
            post.blog = blog
        return self.save_post(post)


class PostForm(PostFormMixin, forms.ModelForm):

    markup_choice = "html"

    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = [
            "section",
            "title",
            "content",
            "description",
            "state"
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if Section.objects.count() < 2:
            self.section = Section.objects.first()
            del self.fields["section"]
        else:
            self.section = None

    def save(self, blog=None, author=None):
        post = super(PostForm, self).save(commit=False)
        if blog:
            post.blog = blog
        if author:
            post.author = author
        if self.section:
            post.section = self.section
        post.slug = slugify(post.title)
        post.markup = self.markup_choice
        return self.save_post(post)
