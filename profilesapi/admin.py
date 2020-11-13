from django.contrib import admin
from .models import UserProfile, ProfileFeedItem


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
    pass