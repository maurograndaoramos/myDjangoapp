from django.contrib import admin
from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import OracleQuestion, OracleAnswer

def change_category(modeladmin, request, queryset):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            new_category = form.cleaned_data['new_category']
            queryset.update(category=new_category)
            modeladmin.message_user(request, "Category changed successfully.")
            return redirect(request.get_full_path())
    else:
        form = CategoryForm()
    return render(request, 'admin/change_category.html', {'form': form})

change_category.short_description = 'Change category of selected questions'

class OracleQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'category')
    list_filter = ('category',)
    actions = [change_category]

admin.site.register(OracleQuestion, OracleQuestionAdmin)
admin.site.register(OracleAnswer)