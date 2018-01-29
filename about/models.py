from django.db import models

# Create your models here.


# Model for About page==
class About(models.Model):
        name = models.CharField("Enter your name here", max_length=20)
        occupation = models.CharField("What do you do?", max_length=30)
        occupation_why = models.CharField("Why do you like you work?", max_length=30)
        contact = models.EmailField(max_length=250, help_text="Enter your email")
        memes = models.CharField(max_length=20)


        def __str__(self):
                return self.name + '-' +  str(self.contact)


# Model for Blog page==
class Blog(models.Model):
        name = models.CharField("Blog Name", max_length = 300)
        tagline = models.CharField("A caption", max_length = 40)

        def __str__(self):
                return self.name


class Author(models.Model):
        name = models.CharField("Author name", max_length=20)

        def __str__(self):
                return self.name


class Entry(models.Model):
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        authors = models.ManyToManyField(Author)
        pub_date = models.DateTimeField()
        
        def __str__(self):
                return str(self.blog)
