# Generated by Django 4.2.16 on 2024-11-06 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_property_rentpayment_houseavailability_complaint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='rental.property'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='rental.user'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='rental.property'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='rental.user'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='rental.property'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='rental.user'),
        ),
        migrations.AlterField(
            model_name='houseavailability',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability_checks', to='rental.property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='rental.user'),
        ),
        migrations.AlterField(
            model_name='rentpayment',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='rental.property'),
        ),
        migrations.AlterField(
            model_name='rentpayment',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='rental.user'),
        ),
    ]
