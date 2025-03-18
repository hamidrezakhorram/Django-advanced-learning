from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import Profile , User
from blog.models import Post , Category
import random
category_list = [
    'news',
    'interesting',
    'weather',
]

class Command(BaseCommand):
    help = "insert dummy data"
    
    def __init__(self, stdout = None, stderr = None, no_color = None, force_color = None):
        super().__init__(stdout, stderr, no_color, force_color)
        self.faker = Faker("fa_IR")

    def handle(self, *args, **options):
        user = User.objects.create_user(email = self.faker.email() , password ='@test123456')
        profile = Profile.objects.get(user = user)
        profile.first_name = self.faker.first_name()
        profile.last_name = self.faker.last_name()
        profile.description = self.faker.paragraph(nb_sentences=3)
        profile.image = self.faker.image_url()
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name = name)

        for _ in range(3):
            Post.objects.create(
                auther = profile,
                title = self.faker.sentence(),
                content = self.faker.paragraph(nb_sentences=5),
                status = True,
                category = Category.objects.get(name=random.choice(category_list)),
                published_date =self.faker.date_time()

            )    


