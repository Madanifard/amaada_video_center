from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# GET /api/categories/ - لیست تمام دسته‌بندی‌ها و ویدیوهای مرتبط
# POST /api/categories/ - ایجاد یک دسته‌بندی جدید
# GET /api/categories/{id}/ - دریافت جزئیات یک دسته‌بندی
# PUT /api/categories/{id}/ - به‌روزرسانی یک دسته‌بندی
# DELETE /api/categories/{id}/ - حذف یک دسته‌بندی
