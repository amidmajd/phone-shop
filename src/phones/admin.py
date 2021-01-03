from django.contrib import admin
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('brand', 'name', 'id', 'date', 'price', 'is_available')
    readonly_fields = ('add_datetime',)
    fieldsets = (
        (None, {'fields': ('id', 'brand', 'name', 'date', 'add_datetime', 'price', 'is_available', 'about', 'image')}),
        ('بدنه', {'fields': (
            'body_size',
            'body_weight',
            'body_structure',
            'body_colors',
            'body_other')}),
        ('نمایشگر', {'fields': (
            'display_type',
            'display_quality',
            'display_colors',
            'display_size',
            'display_other',
        )}),
        ('سخت افزار', {'fields': (
            'hardware_cpu',
            'hardware_gpu',
            'hardware_ram',
            'hardware_battery',
            'hardware_other',
        )}),
        ('دوربین اصلی', {'fields': (
            'back_cam_pic_quality',
            'back_cam_lens',
            'back_cam_vid_quality',
            'back_cam_fps',
            'back_camera_other',
        )}),
        ('دوربین جلو', {'fields': (
            'front_cam_pic_quality',
            'front_cam_lens',
            'front_cam_vid_quality',
            'front_cam_fps',
            'front_camera_other',
        )}),
        ('فضای ذخیره‌سازی', {'fields': (
            'storage_type',
            'storage_size',
            'storage_other',
        )}),
        ('سایر مشخصات', {'fields': (
            'other_sim',
            'other_sim_count',
            'other_os',
            'other_ui',
            'other_sensors',
            'other_specials',
        )}),
    )
    search_fields = ('brand', 'name', 'id', 'date', 'price')
    ordering = ('-add_datetime',)
    list_filter = ('is_available', 'brand', 'other_os', 'storage_size', 'hardware_ram')
    filter_horizontal = ()


admin.site.register(Phone, PhoneAdmin)
