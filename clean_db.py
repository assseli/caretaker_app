from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Cleans (truncates) all tables in the database except for Django migrations and auth tables.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Cleaning all user tables...'))
        with connection.cursor() as cursor:
            # Get all table names except Django system tables
            cursor.execute("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = DATABASE()
                AND table_name NOT LIKE 'django_%'
                AND table_name NOT LIKE 'auth_%'
                AND table_name NOT LIKE 'admin_%'
                AND table_name NOT LIKE 'sessions%';
            """)
            tables = [row[0] for row in cursor.fetchall()]
            if not tables:
                self.stdout.write(self.style.WARNING('No user tables found to clean.'))
                return
            # Disable foreign key checks
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            for table in tables:
                cursor.execute(f'TRUNCATE TABLE `{table}`;')
                self.stdout.write(self.style.SUCCESS(f'Truncated {table}'))
            # Re-enable foreign key checks
            cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')
        self.stdout.write(self.style.SUCCESS('Database cleaned.'))
