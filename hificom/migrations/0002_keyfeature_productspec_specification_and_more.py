# Generated by Django 4.2 on 2024-06-26 06:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hificom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TitleAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='spec',
            name='table',
        ),
        migrations.RemoveField(
            model_name='spectable',
            name='product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-priority']},
        ),
        migrations.RemoveField(
            model_name='category',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='carousel',
            name='added_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='category',
            name='display_childs',
            field=models.CharField(choices=[('all', 'All Categories'), ('none', 'Display No Childs'), ('general', 'General Category'), ('brand', 'Brand Category'), ('feature', 'Feature Category'), ('tag', 'Tag Under Feature')], default='brand', max_length=20),
        ),
        migrations.AddField(
            model_name='category',
            name='get_features_from_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='hificom.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_products', to='hificom.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_type',
            field=models.CharField(choices=[('general', 'General Category'), ('brand', 'Brand Category'), ('feature', 'Feature Category'), ('tag', 'Tag Under Feature')], default='general', max_length=20),
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Spec',
        ),
        migrations.DeleteModel(
            name='SpecTable',
        ),
        migrations.AddField(
            model_name='specificationtable',
            name='aliases',
            field=models.ManyToManyField(related_name='tables', to='hificom.titlealias'),
        ),
        migrations.AddField(
            model_name='specificationtable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hificom.category'),
        ),
        migrations.AddField(
            model_name='specification',
            name='aliases',
            field=models.ManyToManyField(related_name='specs', to='hificom.titlealias'),
        ),
        migrations.AddField(
            model_name='specification',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hificom.specificationtable'),
        ),
        migrations.AddField(
            model_name='productspec',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hificom.product'),
        ),
        migrations.AddField(
            model_name='productspec',
            name='specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hificom.specification'),
        ),
        migrations.AddField(
            model_name='keyfeature',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hificom.product'),
        ),
    ]
