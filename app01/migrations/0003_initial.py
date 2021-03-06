# Generated by Django 4.0.4 on 2022-05-06 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=16)),
                ('cphone', models.CharField(max_length=11, unique=True)),
                ('clocation', models.CharField(max_length=16)),
                ('csalary', models.IntegerField()),
                ('csend', models.IntegerField()),
                ('cfetch', models.IntegerField()),
            ],
            options={
                'db_table': 'courier',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=16)),
                ('dphone', models.CharField(max_length=11, unique=True)),
                ('ddeparture', models.CharField(max_length=16)),
                ('ddestination', models.CharField(max_length=16)),
                ('dsalary', models.IntegerField()),
                ('dcompensation', models.IntegerField()),
            ],
            options={
                'db_table': 'driver',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=16)),
                ('mphone', models.CharField(max_length=11, unique=True)),
                ('msalary', models.IntegerField()),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('district', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'map',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(max_length=16)),
                ('sender_id', models.IntegerField()),
                ('receiver_id', models.IntegerField()),
                ('pdeparture', models.CharField(max_length=16)),
                ('pdestination', models.CharField(max_length=16)),
                ('start_time', models.DateTimeField()),
                ('courier_a_id', models.IntegerField(blank=True, null=True)),
                ('send_time', models.DateTimeField(blank=True, null=True)),
                ('driver_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('courier_b_id', models.IntegerField(blank=True, null=True)),
                ('station_id', models.IntegerField(blank=True, null=True)),
                ('arrival_time', models.DateTimeField(blank=True, null=True)),
                ('shelf', models.IntegerField(blank=True, null=True)),
                ('layor', models.IntegerField(blank=True, null=True)),
                ('pick_id', models.CharField(blank=True, max_length=10, null=True)),
                ('picker_id', models.CharField(blank=True, max_length=11, null=True)),
                ('pick_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=3)),
                ('station_price', models.FloatField(blank=True, null=True)),
                ('express_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'package',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('departure', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=16)),
                ('duration', models.IntegerField()),
                ('unit_price', models.IntegerField()),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StaffLogin',
            fields=[
                ('phone', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=80)),
                ('class_field', models.CharField(db_column='class', max_length=5)),
                ('sid', models.IntegerField()),
            ],
            options={
                'db_table': 'staff_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('slocation', models.CharField(max_length=16)),
                ('saddress', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'station',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=16)),
                ('uphone', models.CharField(max_length=11, unique=True)),
                ('uaddress', models.CharField(max_length=200)),
                ('ulocation', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('phone', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'user_login',
                'managed': False,
            },
        ),
    ]
