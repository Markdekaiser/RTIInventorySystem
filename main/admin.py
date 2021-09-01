from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import Employee, Customer, Product, Requesition, Section,RawMaterial,RawBatch

admin.site.site_header = 'Inventory System'
admin.site.site_title = 'Inventory System Admin Panel'
admin.site.index_title = 'Welcome to Inventory System Admin'

@admin.register(RawMaterial)
class RMAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    fields = [
        'name',
    ]
    search_fields = [
        'name'
    ]

@admin.register(RawBatch)
class RBAdmin(admin.ModelAdmin):
    list_display = [
        'tp',
        'batch_name',
        'date_created',
        'quantity'
    ]
    fields = [
        'tp',
        'batch_name',
        'quantity'
    ]
    search_fields = [
        'batch_name',
    ]    

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    fields = [
        'name',
    ]
    search_fields = [
        'name'
    ]

@admin.register(Requesition)
class RequesitionAdmin(admin.ModelAdmin):
    
    list_display=[
        'Control_Number',
        'Item',
        'Qty',
        'status'
    ]
    fields = [
        'customer_id',
        'Control_Number',
        'Section',
        'Item',
        'Qty',
        'status'
    ]
    search_fields=[
        'Control_Number',
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'stock_quantity',
        'unit_of_measurement',
        'price'
    ]
    fields = [
        'name','description','stock_quantity','unit_of_measurement','price'
    ]
    search_fields = [
        'name'
    ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'name','phone_number','email'
    ]
    fields = [
        'name','phone_number','email'
    ]
    search_fields = [
        'name','email'
    ]

class UserCreationform(forms.ModelForm):
    email = forms.EmailField()
    user_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    
    address = forms.CharField(max_length = 150)
    phone_number = forms.IntegerField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = [
            'email','first_name','last_name','user_name','password1','password2','address','phone_number',
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserCreationform, self).__init__(*args, **kwargs)

        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control input-lg'

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = [
            'email','user_name','first_name','last_name','address','phone_number','is_active','is_staff'
        ]


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    ordering = ['last_name']
    list_display=[
        'email','first_name','last_name','section','is_active','is_staff', 'section'
    ]
    list_filter = ['is_staff']
    search_fields=[
        'email','user_name','first_name'
    ]
    fieldsets=[
        [None,{'fields':['email','user_name','first_name','last_name']}],
        ['Permissions', {'fields':['is_active','is_staff']}],
        ['Others',{'fields':['address','phone_number','section']}]
    ]
    add_fieldsets = [
        [None,{
            'classes':['wide',],
            'fields':['email','user_name','first_name','last_name','password1','password2','address','phone_number','section','is_staff','is_active']
        }]
    ]

admin.site.register(Employee, UserAdmin)
admin.site.unregister(Group)