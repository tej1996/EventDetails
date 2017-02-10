import cloudinary
from django import template
from django.shortcuts import get_object_or_404

from website.models import UserProfile
from django.contrib.staticfiles.templatetags.staticfiles import static
register = template.Library()


@register.simple_tag
def dp_request(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if user.passphoto is not None and user.passphoto != "":
        dp = cloudinary.CloudinaryImage(user.passphoto).build_url(sign_url=True, format='png', width=0.5,
                                                                  type='authenticated')
    else:
        dp = static('website/images/profilepic.png')
    return dp


@register.simple_tag
def name_request(request):
    user = get_object_or_404(UserProfile, user=request.user)

    return user.name


@register.simple_tag
def type_request(request):
    user = get_object_or_404(UserProfile, user=request.user)
    if user.type:
        type = "Faculty"
    else:
        type = "Student"
    return type
