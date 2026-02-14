# <HINT> Create a Question Model with:
# Used to persist question content for a course
# Has a One-To-Many (or Many-To-Many if you want reuse) relationship with course
# Has a grade point for each question
# Has question content
# Other fields and methods you would like to design
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=5)

    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(is_correct=True, id__in=selected_ids).count()
        if all_answers == selected_correct:
            return True
        else:
            return False

    def __str__(self):
        return self.question_text


# <HINT> Create a Choice Model with:
# Used to persist choice content for a question
# One-To-Many (or Many-To-Many if you want reuse) relationship with Question
# Choice content
# Indicate if this choice of the question is a correct one or not
# Other fields and methods you would like to design
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


# <HINT> The submission model
# One enrollment could have multiple submission
# One submission could have multiple choices
# One choice could belong to multiple submissions
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
