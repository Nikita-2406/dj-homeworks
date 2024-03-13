from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter_form = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                counter_form += 1
        if counter_form == 0:
            raise ValidationError('Укажите основной раздел')
        elif counter_form > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']