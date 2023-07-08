from django import forms


from forum.models import Category, SubCategory, Topic, Post


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ('subcategory_name', 'subcategory_description')


class TopicForm(forms.ModelForm):
    pass


class PostForm(forms.ModelForm):
    pass
