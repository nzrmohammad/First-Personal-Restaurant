from django.contrib import admin
from .models import About,Special_Dishes,Category,Food_Menu,Reservation_Date,Reservation_Time,Reservation_Count,Reservation_Table_Number,Reservation_Item,Reservation_Received,Service,Popular_Dishes,Event,Event_Bottom,Testimonial,ContactUs,Contact,Profile
from django.utils.html import format_html

# 1 - About Page 1 - About Page 1 - About Page 1 - About Page 1 - About Page
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name','title1','image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="75px" height="75px"/>'.format(obj.image1.url))
    image_tag.short_description = 'Image'

# 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page

@admin.register(Special_Dishes)
class Special_DishesAdmin(admin.ModelAdmin):
    list_display = ['title','price','description','image_tag']
    list_editable = ['price']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="155px" height="155px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image Preview'

# 3 - Category # 3 - Category # 3 - Category # 3 - Category # 3 - Category # 3 - Category # 3 - Category 

admin.site.register(Category)

# 4 - Food_Menu # 4 - Food_Menu # 4 - Food_Menu # 4 - Food_Menu # 4 - Food_Menu # 4 - Food_Menu # 4 - Food_Menu
@admin.register(Food_Menu)
class Food_MenuAdmin(admin.ModelAdmin):
    list_display = ['title','price','category','image_tag']
    list_filter = ['category']
    list_editable = ['price','category']
    search_fields = ['title']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100px" height="100px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

# 5 - Reservation_Item # 5 - Reservation_Item # 5 - Reservation_Item # 5 - Reservation_Item

class ProfileInline(admin.TabularInline):
    model = Reservation_Date
    extra = 1

class ProfileInline2(admin.TabularInline):
    model = Reservation_Time
    extra = 1

class ProfileInline3(admin.TabularInline):
    model = Reservation_Count
    extra = 1

class ProfileInline4(admin.TabularInline):
    model = Reservation_Table_Number
    extra = 1

@admin.register(Reservation_Item)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline,ProfileInline2,ProfileInline3,ProfileInline4]

# 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received

@admin.register(Reservation_Received)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','date','time','count','table_number','is_read']
    list_display_links = ['name']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['name']
    readonly_fields = ['name','date','time','count','table_number']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# 7 - Service Page # 7 - Service Page # 7 - Service Page # 7 - Service Page # 7 - Service Page
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','description']
    list_editable = ['description']
    readonly_fields= ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="85px" height="85px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

# 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page
@admin.register(Popular_Dishes)
class Popular_DishesAdmin(admin.ModelAdmin):
    list_display = ['title','price','description','image_tag']
    list_editable = ['price']
    readonly_fields= ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100px" height="100px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

# 8 - Event Page # 8 - Event Page # 8 - Event Page # 8 - Event Page # 8 - Event Page
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','date','image_tag']
    readonly_fields= ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="85px" height="85px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

# 9 - Event_Bottom Page
admin.site.register(Event_Bottom)

# 10 - Testimonial Page # 10 - Testimonial Page # 10 - Testimonial Page # 10 - Testimonial Page # 10 - Testimonial Page
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']
    readonly_fields= ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="85px" height="85px"/>'.format(obj.image.url))
    image_tag.short_description = 'Image'

# 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','is_read']
    list_display_links = ['name']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['name','subject','message']
    readonly_fields = ['name','subject','email','message']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# 12 - Contact # 12 - Contact # 12 - Contact # 12 - Contact # 12 - Contact # 12 - Contact

class ProfileInline3(admin.TabularInline):
    model = Profile
    extra = 1  

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [ProfileInline3]
    list_display = ['phone','email','address']
    list_display_links = ['phone']
    list_editable = ['email','address']
