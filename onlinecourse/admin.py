from django.contrib import admin
# Yêu cầu import 7 classes:
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Tạo Inline cho Choice (Hiển thị các đáp án ngay trong trang tạo Câu hỏi)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 # Mặc định cho 3 ô nhập đáp án

# Tạo Inline cho Question
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 3

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Đăng ký QuestionAdmin có chứa ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# Đăng ký toàn bộ Models vào Admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
