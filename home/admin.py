from django.contrib import admin
from .models import *

@admin.register(CustomerMessage)
class CustomerMessageAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'email', 'phone_number', 'subject', 'is_read', 'created_at', 'updated_at')
    
    # Optional: add filters on the right side
    list_filter = ('is_read', 'created_at')
    
    # Optional: search bar
    search_fields = ('name', 'email', 'subject', 'message')
    
    # Optional: ordering
    ordering = ('-created_at',)

    # Optional: show detail view with all fields
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number', 'subject', 'message', 'is_read')
        }),
        ('زمان', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    # Make created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'phone_number', 'phone_number_2', 'email', 'whatsapp', 'telegram', 'created_at')
    search_fields = ('title', 'location', 'phone_number', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

# -------------------------------------
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'experniance', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'description', 'mission', 'vision', 'values')
    readonly_fields = ('created_at', 'updated_at')

# -------------------------------------
@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_read', 'created_at', 'updated_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

# -------------------------------------
@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('facebook', 'instagram', 'tiktok', 'youtube', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(ListingPolicy)