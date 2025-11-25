from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Deletes (drops) all user tables in the database except for Django and MySQL system tables.'

    def handle(self, *args, **options):
        print('Starting database cleanup...')
        self.stdout.write(self.style.WARNING('Deleting all user tables...'))
        with connection.cursor() as cursor:
            print('Fetching user tables to delete...')
            # Get all table names except Django and MySQL system tables
            cursor.execute("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_schema = DATABASE()
                AND table_name NOT LIKE 'django_%'
                AND table_name NOT LIKE 'auth_%'
                AND table_name NOT LIKE 'admin_%'
                AND table_name NOT LIKE 'sessions%'
                AND table_name NOT IN ('mysql', 'performance_schema', 'information_schema', 'sys');
            """)
            tables = [row[0] for row in cursor.fetchall()]
            print(f'Found tables: {tables}')
            if not tables:
                print('No user tables found to delete.')
                self.stdout.write(self.style.WARNING('No user tables found to delete.'))
                return
            print('Disabling foreign key checks...')
            # Disable foreign key checks
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
            for table in tables:
                print(f'Dropping table: {table}')
                cursor.execute(f'DROP TABLE IF EXISTS `{table}`;')
                self.stdout.write(self.style.SUCCESS(f'Dropped {table}'))
            print('Re-enabling foreign key checks...')
            # Re-enable foreign key checks
            cursor.execute('SET FOREIGN_KEY_CHECKS = 1;')
        print('Database cleanup complete.')
        self.stdout.write(self.style.SUCCESS('User tables deleted.'))