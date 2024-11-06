# Generated by Django 5.1.3 on 2024-11-05 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('AppointmentId', models.AutoField(primary_key=True, serialize=False)),
                ('AppointmentDate', models.DateTimeField()),
                ('TokenNumber', models.IntegerField()),
                ('ConsultationStatus', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('DoctorId', models.AutoField(primary_key=True, serialize=False)),
                ('ConsultationFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabTestCategory',
            fields=[
                ('LabTestCategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('LabTestCategoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineCategory',
            fields=[
                ('MedicineCategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('MedicineCategoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('MembershipId', models.AutoField(primary_key=True, serialize=False)),
                ('MembershipType', models.CharField(max_length=100)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('RoleId', models.AutoField(primary_key=True, serialize=False)),
                ('RoleName', models.CharField(max_length=100)),
                ('IsActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('SpecializationId', models.AutoField(primary_key=True, serialize=False)),
                ('SpecializationName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('ConsultationId', models.AutoField(primary_key=True, serialize=False)),
                ('Symptoms', models.TextField()),
                ('Diagnosis', models.TextField()),
                ('Notes', models.TextField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('AppointmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.appointment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='DoctorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.doctor'),
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('LabTestId', models.AutoField(primary_key=True, serialize=False)),
                ('TestName', models.CharField(max_length=100)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ReferenceMinRange', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ReferenceMaxRange', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SampleRequired', models.CharField(max_length=100)),
                ('IsActive', models.BooleanField(default=True)),
                ('LabTestCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.labtestcategory')),
            ],
        ),
        migrations.CreateModel(
            name='LabTestPrescription',
            fields=[
                ('LabTestPrescriptionId', models.AutoField(primary_key=True, serialize=False)),
                ('LabTestValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('Remarks', models.TextField()),
                ('IsActive', models.BooleanField(default=True)),
                ('AppointmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.appointment')),
                ('LabTestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.labtest')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('MedicineId', models.AutoField(primary_key=True, serialize=False)),
                ('MedicineName', models.CharField(max_length=100)),
                ('ManufacturingDate', models.DateField()),
                ('ExpiryDate', models.DateField()),
                ('Unit', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('MedicineCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.medicinecategory')),
            ],
        ),
        migrations.CreateModel(
            name='MedicinePrescription',
            fields=[
                ('MedicinePrescriptionId', models.AutoField(primary_key=True, serialize=False)),
                ('Dosage', models.CharField(max_length=50)),
                ('Frequency', models.CharField(max_length=50)),
                ('Duration', models.CharField(max_length=50)),
                ('IsActive', models.BooleanField(default=True)),
                ('AppointmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.appointment')),
                ('MedicineId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineStock',
            fields=[
                ('MedicineStockId', models.AutoField(primary_key=True, serialize=False)),
                ('StockInHand', models.IntegerField()),
                ('ReOrderLevel', models.IntegerField()),
                ('Purchase', models.IntegerField()),
                ('Issuance', models.IntegerField()),
                ('CreatedDate', models.DateField()),
                ('IsActive', models.BooleanField(default=True)),
                ('MedicineId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PatientId', models.AutoField(primary_key=True, serialize=False)),
                ('PatientName', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('Address', models.TextField()),
                ('IsActive', models.BooleanField(default=True)),
                ('MembershipId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.membership')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='PatientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.patient'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='SpecializationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.specialization'),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('StaffId', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('JoiningDate', models.DateField()),
                ('MobileNumber', models.CharField(max_length=15)),
                ('UserName', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=128)),
                ('IsActive', models.BooleanField(default=True)),
                ('RoleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.role')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='StaffId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apibackendapp.staff'),
        ),
    ]