from django.conf import settings
from .InstaScraper import InstaScraper
from .models import Image

from django_cron import CronJobBase, Schedule


class Scrape(CronJobBase):

    RUN_EVERY_MINS = 5 if settings.DEBUG else 360

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'Scrape'

    def do(self):
        images = InstaScraper('nbladakh').images
        DB_images = Image.objects.all()
        existing_imgs = [img.code for img in DB_images]
        print(existing_imgs)
        new_imgs = [img.code for img in images]
        print(new_imgs)
        for img in images:
            if img.code not in existing_imgs:
                print('not in')
                i = Image.create(img.code, img.low_res_url, img.embed_code)
                i.save()
                print('saved img')
        for img in DB_images:
            if img.code not in new_imgs:
                img.delete()


            
if __name__ == '__main__':
    images = InstaScraper('nbladakh')
    for img in images:
        print(img.code)
