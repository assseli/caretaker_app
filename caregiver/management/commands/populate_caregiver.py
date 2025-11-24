from django.core.management.base import BaseCommand
from caregiver.models import User, Caregiver, Member, Address, Job, Job_Application, Appointment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populate the caregiver app with sample data.'

    def handle(self, *args, **kwargs):

        # Mixed Russian and Kazakh names and cities
        first_names = [
            'Ivan', 'Dmitry', 'Olga', 'Svetlana', 'Nikolai', 'Ekaterina', 'Sergey', 'Anna', 'Vladimir', 'Maria',
            'Ayan', 'Dana', 'Yerlan', 'Aigerim', 'Nursultan', 'Zhansaya', 'Alikhan', 'Gulnaz', 'Dias', 'Madina'
        ]
        surnames = [
            'Ivanov', 'Petrov', 'Sidorov', 'Smirnov', 'Kuznetsova', 'Popova', 'Volkov', 'Morozov', 'Fedorova', 'Mikhailova',
            'Akhmetov', 'Nazarbayeva', 'Tulegenov', 'Sarsenbayeva', 'Kenzhebekov', 'Zhaksylykova', 'Mukhamedzhanov', 'Abdrakhmanova', 'Yessimkhanov', 'Kairatova'
        ]
        cities = ['Almaty', 'Astana', 'Moscow', 'Saint Petersburg', 'Shymkent', 'Karaganda', 'Novosibirsk', 'Pavlodar', 'Omsk', 'Aktobe']

        # Create Users
        users = []
        for i in range(10):
            given_name = random.choice(first_names)
            surname = random.choice(surnames)
            city = random.choice(cities)
            email = f"{given_name.lower()}.{surname.lower()}{i}@example.com"
            user = User.objects.create(
                email=email,
                given_name=given_name,
                surname=surname,
                city=city,
                phone_number=f'+7 777 {random.randint(100,999)}-{random.randint(10,99)}-{random.randint(10,99)}',
                profile_description=f'{given_name} {surname} from {city}.'
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS('Created 10 Users'))

        # Create Caregivers
        caregivers = []
        for i in range(10):
            name = f"{random.choice(first_names)} {random.choice(surnames)}"
            gender = random.choice(['Male', 'Female'])
            caregiver_type = random.choice(['Nurse', 'Companion', 'Therapist'])
            hourly_rate = round(random.uniform(15, 50), 2)
            caregiver = Caregiver.objects.create(
                name=name,
                gender=gender,
                caregiver_type=caregiver_type,
                hourly_rate=hourly_rate
            )
            caregivers.append(caregiver)
        self.stdout.write(self.style.SUCCESS('Created 10 Caregivers'))

        # Create Members
        members = []
        for i in range(10):
            name = f"{random.choice(first_names)} {random.choice(surnames)}"
            house_rules = f"No smoking. Quiet hours after 10pm. Respect {name}."
            dependent_description = f"{name} requires daily assistance."
            member = Member.objects.create(
                name=name,
                house_rules=house_rules,
                dependent_description=dependent_description
            )
            members.append(member)
        self.stdout.write(self.style.SUCCESS('Created 10 Members'))

        # Create Addresses
        for i, member in enumerate(members):
            Address.objects.create(
                member=member,
                house_number=str(100 + i),
                street=f'Street {i}',
                town=f'Town {i}'
            )
        self.stdout.write(self.style.SUCCESS('Created 10 Addresses'))

        # Create Jobs
        jobs = []
        for i, member in enumerate(members):
            job = Job.objects.create(
                member=member,
                required_caregiver_type=random.choice(['Nurse', 'Companion', 'Therapist']),
                other_requirements=f'Other requirements for job {i}'
            )
            jobs.append(job)
        self.stdout.write(self.style.SUCCESS('Created 10 Jobs'))

        # Create Job Applications
        for i in range(10):
            Job_Application.objects.create(
                job=random.choice(jobs),
                caregiver=random.choice(caregivers)
            )
        self.stdout.write(self.style.SUCCESS('Created 10 Job Applications'))

        # Create Appointments
        for i in range(10):
            Appointment.objects.create(
                caregiver=random.choice(caregivers),
                member=random.choice(members),
                appointment_date=timezone.now().date(),
                appointment_time=timezone.now().time(),
                work_hours=round(random.uniform(1, 8), 2),
                status=random.choice(['Scheduled', 'Completed', 'Cancelled'])
            )
        self.stdout.write(self.style.SUCCESS('Created 10 Appointments'))
