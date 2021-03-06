from django.db import models

from pine.models.users import Users


class Threads(models.Model):
    author = models.ForeignKey(Users, related_name='authorized')
    is_public = models.BooleanField(default=False)
    readers = models.ManyToManyField(Users, related_name='readable')
    likes = models.ManyToManyField(Users, related_name='likeThreads')
    views = models.ManyToManyField(Users, related_name='viewThreads')
    max_like = models.IntegerField(default=0)
    reports = models.ManyToManyField(Users, related_name='reportThreads')
    pub_date = models.DateTimeField()
    image_url = models.CharField(max_length=256, default='')
    content = models.CharField(max_length=1000)

    class Meta:
        app_label = 'pine'
        ordering = ['-pub_date']

    def __str__(self):
        return ('pk: ' + str(self.pk)
                + ', author: ' + str(self.author.id)
                + ', is_public:' + str(self.is_public)
                + ', readers: [' + ' '.join(str(n) for n in [user.id for user in self.readers.only('id')])
                + '], likes: [' + ' '.join(str(n) for n in [user.id for user in self.likes.only('id')])
                + '], views: [' + ' '.join(str(n) for n in [user.id for user in self.views.only('id')])
                + '], max_like: ' + str(self.max_like)
                + ', reports: [' + ' '.join(str(n) for n in [user.id for user in self.reports.only('id')])
                + '], pub_date: ' + str(self.pub_date)
                + ', image_url: ' + self.image_url
                + ', content: ' + self.content)
