from django.db import models

GENDER_CHOICE = (
    ("M", "M"),
    ("F", "F"),
)

COURSE_CHOICE = (
    ('C', 'C'),
    ('C++', 'C++'),
    ('Python', 'Python'),
    ('JAVA', 'JAVA'),
)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)

    roll_no = models.CharField(max_length=255)

    name = models.CharField(max_length=255)

    dob = models.DateField()

    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    course = models.CharField(max_length=255, choices=COURSE_CHOICE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'


class MarkList(models.Model):
    id = models.BigAutoField(primary_key=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    subject_name = models.CharField(max_length=255)

    mark = models.IntegerField()

    def __str__(self):
        return self.student.name

    class Meta:
        db_table = 'mark_list'


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'


class State(models.Model):
    id = models.BigAutoField(primary_key=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'state'


class City(models.Model):
    id = models.BigAutoField(primary_key=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'


class SystemSettings(models.Model):
    id = models.BigAutoField(primary_key=True)

    company_name = models.TextField()

    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    zipcode = models.CharField(max_length=255)

    phone = models.CharField(max_length=255)

    email = models.CharField(max_length=255)

    website = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'system_setting'
