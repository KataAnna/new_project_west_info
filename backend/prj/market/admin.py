from django.contrib import admin

from market.models import *
#from django.contrib.flatpages.admin import FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage
#from django.utils.translation import gettext_lazy as get_lazy

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

admin.site.register(SubCategory, SubCategoryAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_small_image', 'category', 'subcategory', 'describe']

admin.site.register(Company, CompanyAdmin)

class ReqOrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(ReqOrder, ReqOrderAdmin)

# Define a new FlatPageAdmin
'''class StaticFlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (get_lazy('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)'''

