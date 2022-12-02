# Generated by Django 4.0 on 2022-11-23 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_sdp'),
        ('places', '0008_alter_placephoto_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_content', models.CharField(max_length=100)),
                ('category_group', models.CharField(blank=True, choices=[('공통', '공통'), ('식당 및 카페', '식당 및 카페'), ('전시 및 체험공간', '전시 및 체험공간'), ('제로웨이스트 샵', '제로웨이스트 샵'), ('도시 재생 및 친환경 건출물', '도시 재생 및 친환경 건출물'), ('복합 문화 공간', '복합 문화 공간'), ('녹색 공간', '녹색 공간'), ('그 외', '그 외')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contents', models.TextField(help_text='리뷰를 작성해주세요.')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place')),
                ('visitor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisitorReviewCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.categorycontent')),
                ('category_choice', models.ManyToManyField(to='places.VisitorReview')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
