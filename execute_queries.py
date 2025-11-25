from sqlalchemy import create_engine, text

# Update these with your actual MySQL credentials and database name
DB_USER = 'root'
DB_PASSWORD = 'mySql2%4024'
DB_HOST = 'localhost'
DB_NAME = 'caregiver_db'
DB_PORT = 3306
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# 1. Create SQL stetements
create_queries = [
	# Create the general app_user table to store user account information
	("app_user-table", """
	CREATE TABLE IF NOT EXISTS app_user (
		id INT AUTO_INCREMENT PRIMARY KEY,
		email VARCHAR(254) NOT NULL UNIQUE,
		given_name VARCHAR(30) NOT NULL,
		surname VARCHAR(30) NOT NULL,
		city VARCHAR(50) NOT NULL,
		phone_number VARCHAR(20) NOT NULL,
		profile_description TEXT);
	"""),
	# Create the address table
    ("address-table", """
    CREATE TABLE IF NOT EXISTS address (
        id INT AUTO_INCREMENT PRIMARY KEY,
        street VARCHAR(100) NOT NULL,
        house_number VARCHAR(10) NOT NULL,
        city VARCHAR(50) NOT NULL);
     """),
	# Create the care_type table
    ("care_type-table", """
    CREATE TABLE IF NOT EXISTS care_type (
        id INT AUTO_INCREMENT PRIMARY KEY,
        type_name VARCHAR(50) NOT NULL UNIQUE,
        type_description TEXT);
     """),
	# Create the caregiver table
    ("caregiver-table", """
    CREATE TABLE IF NOT EXISTS caregiver (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        gender ENUM('Male', 'Female', 'Other') NOT NULL,
        hourly_rate DECIMAL(6,2) NOT NULL,
        care_type_id INT,
        FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE CASCADE,
        FOREIGN KEY (care_type_id) REFERENCES care_type(id) ON DELETE SET NULL);
    """),
	# Create the member table
    ("member-table", """
    CREATE TABLE IF NOT EXISTS member (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        house_rules TEXT,
        dependent_description TEXT,
        dependent_age INT NOT NULL,
        address_id INT,
        FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE CASCADE,
        FOREIGN KEY (address_id) REFERENCES address(id) ON DELETE SET NULL);
    """),
	# Create the job_ad table
    ("job-table", """
    CREATE TABLE IF NOT EXISTS job_ad (
        id INT AUTO_INCREMENT PRIMARY KEY,
        member_id INT NOT NULL,
        required_caregiver_type_id INT,
        other_requirements TEXT,
        date_posted DATE NOT NULL DEFAULT (CURRENT_DATE),
        status ENUM('Open', 'Closed') NOT NULL DEFAULT 'Open',
        FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE CASCADE,
        FOREIGN KEY (required_caregiver_type_id) REFERENCES care_type(id) ON DELETE SET NULL);
    """),
	# Create the job_application table
    ("job_application-table", """
    CREATE TABLE IF NOT EXISTS job_application (
        id INT AUTO_INCREMENT PRIMARY KEY,
        job_id INT NOT NULL,
        caregiver_id INT NOT NULL,
        date_applied DATE NOT NULL DEFAULT (CURRENT_DATE),
        status ENUM('Pending', 'Accepted', 'Rejected') NOT NULL DEFAULT 'Pending',
        FOREIGN KEY (job_id) REFERENCES job_ad(id) ON DELETE CASCADE,
        FOREIGN KEY (caregiver_id) REFERENCES caregiver(id) ON DELETE CASCADE);
    """),
	# Create the appointment table
    ("appointment-table", """
    CREATE TABLE IF NOT EXISTS appointment (
        id INT AUTO_INCREMENT PRIMARY KEY,
        caregiver_id INT NOT NULL,
        member_id INT NOT NULL,
        appointment_date DATE NOT NULL,
        appointment_time TIME NOT NULL,
        work_hours DECIMAL(4,2) NOT NULL,
        status ENUM('Pending', 'Accepted', 'Rejected') NOT NULL DEFAULT 'Pending',
        FOREIGN KEY (caregiver_id) REFERENCES caregiver(id) ON DELETE CASCADE,
        FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE CASCADE);
    """),
	# Create the message table
    ("message-table", """
    CREATE TABLE IF NOT EXISTS message (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sender_id INT NOT NULL,
        receiver_id INT NOT NULL,
        content TEXT NOT NULL,
        timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        status ENUM('Sent', 'Delivered', 'Read') NOT NULL DEFAULT 'Sent',
        FOREIGN KEY (sender_id) REFERENCES app_user(id) ON DELETE CASCADE,
        FOREIGN KEY (receiver_id) REFERENCES app_user(id) ON DELETE CASCADE);
    """)
]

# 2. Populate SQL statements
populate_users = [
	# Populate all tables with initial randomized data
	("populate-users", """
    INSERT INTO app_user (email, given_name, surname, city, phone_number, profile_description) VALUES
        -- Caregivers (first 10)
        ('aigerim.akhmetova@example.com', 'Aigerim', 'Akhmetova', 'Astana', '+77011234567', 'Caregiver: experienced, patient, and reliable'),
        ('daniyar.nursultanov@example.com', 'Daniyar', 'Nursultanov', 'Almaty', '+77021234567', 'Caregiver: specializes in elderly care'),
        ('aliya.saparova@example.com', 'Aliya', 'Saparova', 'Shymkent', '+77031234567', 'Caregiver: energetic and creative'),
        ('nursultan.abishev@example.com', 'Nursultan', 'Abishev', 'Karaganda', '+77041234567', 'Caregiver: great with children'),
        ('zhanel.kairatova@example.com', 'Zhanel', 'Kairatova', 'Pavlodar', '+77051234567', 'Caregiver: organized and punctual'),
        ('arman.armanov@example.com', 'Arman', 'Armanov', 'Astana', '+77061234567', 'Caregiver: specializes in special needs care'),
        ('madina.tulegenova@example.com', 'Madina', 'Tulegenova', 'Almaty', '+77071234567', 'Caregiver: friendly and responsible'),
        ('yerbolat.zhanibekov@example.com', 'Yerbolat', 'Zhanibekov', 'Shymkent', '+77081234567', 'Caregiver: excellent communicator'),
        ('saule.amanova@example.com', 'Saule', 'Amanova', 'Karaganda', '+77091234567', 'Caregiver: flexible and reliable'),
        ('maksat.nurlybekov@example.com', 'Maksat', 'Nurlybekov', 'Pavlodar', '+77101234567', 'Caregiver: soft-spoken and caring'),

        -- Family members (next 10)
        ('olga.petrova@example.com', 'Olga', 'Petrova', 'Astana', '+77111234567', 'Member: family member seeking care for elderly parent'),
        ('ivan.ivanov@example.com', 'Ivan', 'Ivanov', 'Almaty', '+77121234567', 'Member: looking for a babysitter for two children'),
        ('elena.smirnova@example.com', 'Elena', 'Smirnova', 'Shymkent', '+77131234567', 'Member: needs daily care for a disabled spouse'),
        ('sergey.pavlov@example.com', 'Sergey', 'Pavlov', 'Karaganda', '+77141234567', 'Member: searching for weekend caregiver for grandmother'),
        ('daria.kozlova@example.com', 'Daria', 'Kozlova', 'Pavlodar', '+77151234567', 'Member: requires after-school care for child'),
        ('dmitry.sokolov@example.com', 'Dmitry', 'Sokolov', 'Astana', '+77161234567', 'Member: needs part-time help for elderly father'),
        ('anastasia.tikhonova@example.com', 'Anastasia', 'Tikhonova', 'Almaty', '+77171234567', 'Member: seeking caregiver for post-surgery recovery'),
        ('nikita.egorov@example.com', 'Nikita', 'Egorov', 'Shymkent', '+77181234567', 'Member: looking for special needs caregiver'),
        ('maria.kuznetsova@example.com', 'Maria', 'Kuznetsova', 'Karaganda', '+77191234567', 'Member: needs weekend babysitter'),
        ('amina.aminova@example.com', 'Amina', 'Aminova', 'Pavlodar', '+77201234567', 'Member: searching for daily elderly care');
  """)
]

populate_care_types = [
    ("populate-care_types", """
    INSERT INTO care_type (type_name, type_description) VALUES
        ('Nurse', 'Provides medical care and assistance.'),
        ('Elderly Care', 'Offers companionship and support to elderly individuals.'),
        ('Babysitter', 'Cares for children.');
    """),
]

populate_addresses = [
    ("populate-addresses", """
    INSERT INTO address (street, house_number, city) VALUES
        ('Abai Avenue', '12A', 'Astana'),
        ('Dostyk Street', '34B', 'Almaty'),
        ('Tauke Khan Street', '56C', 'Shymkent'),
        ('Bukhar Zhyrau Boulevard', '78D', 'Karaganda'),
        ('Satpayev Street', '90E', 'Pavlodar'),
        ('Nazarbayev Avenue', '15F', 'Astana'),
        ('Akmeshit Street', '27G', 'Almaty'),
        ('Respublika Avenue', '39H', 'Shymkent'),
        ('Auezov Street', '41I', 'Karaganda'),
        ('Zhambyl Street', '53J', 'Pavlodar'),
        ('Kunayev Street', '65K', 'Astana'),
        ('Al-Farabi Avenue', '77L', 'Almaty'),
        ('Mangilik El Avenue', '89M', 'Astana'),
        ('Kabanbay Batyr Avenue', '91N', 'Shymkent'),
        ('Seifullin Street', '13O', 'Karaganda');
    """),
]

populate_caregivers = [
    ("populate-caregivers", """
    INSERT INTO caregiver (user_id, gender, hourly_rate, care_type_id) VALUES
        ( 1, 'Female', 18.00, 1),
        ( 2, 'Male', 20.00, 2),
        ( 3, 'Female', 17.50, 3),
        ( 4, 'Male', 19.00, 1),
        ( 5, 'Female', 21.00, 2),
        ( 6, 'Male', 16.50, 3),
        ( 7, 'Female', 22.00, 1),
        ( 8, 'Male', 18.50, 2),
        ( 9, 'Female', 20.50, 3),
        ( 10, 'Male', 19.50, 1);
    """),
]

populate_members = [
    ("populate-members", """
    INSERT INTO member (user_id, house_rules, dependent_description, dependent_age, address_id) VALUES
        ( 11, 'No smoking, No pets', 'Elderly parent with mild dementia',87, 1),
        ( 12, 'No loud music', 'Two children aged 5 and 8',5, 2),
        ( 13, 'No outside visitors, No pets', 'Disabled spouse requiring daily assistance',44, 3),
        ( 14, 'Respectful behavior', 'Grandmother needing weekend care',78, 4),
        ( 15, 'Timely pickups', 'After-school care for child',10, 5),
        ( 16, 'No smoking, No pets', 'Elderly father with mobility issues',67, 6),
        ( 17, 'Gentle care', 'Post-surgery recovery assistance',22, 9),
        ( 18, 'Patient and understanding', 'Special needs child care',12, 14),
        ( 19, 'Punctuality', 'Weekend babysitting for two kids',7, 4),
        ( 20, 'Compassionate care', 'Daily elderly care for father',77, 9);
    """),
]

populate_job_ads = [
    ("populate-job_ads", """
    INSERT INTO job_ad (member_id, required_caregiver_type_id, other_requirements, status) VALUES
        (1, 1, 'Experience with dementia patients', 'Open'),
        (2, 3, 'CPR certified', 'Open'),
        (3, 2, 'Able to assist with mobility', 'Open'),
        (4, 1, 'Weekend availability', 'Closed'),
        (5, 3, 'Creative and engaging', 'Open'),
        (6, 2, 'Experience with elderly care, soft-spoken', 'Open'),
        (7, 1, 'Post-surgery care experience', 'Open'),
        (8, 3, 'Special needs experience', 'Closed'),
        (9, 3, 'Reliable and punctual', 'Open'),
        (10, 2, 'Compassionate and soft-spoken', 'Open');
    """),
]

populate_job_applications = [
    ("populate-job_applications", """
    INSERT INTO job_application (job_id, caregiver_id, status) VALUES
        (1, 1, 'Pending'),
        (1, 3, 'Accepted'),
        (1, 7, 'Rejected'),
        (2, 2, 'Pending'),
        (2, 5, 'Pending'),
        (3, 1, 'Pending'),
        (3, 4, 'Accepted'),
        (3, 8, 'Rejected'),
        (3, 10, 'Pending'),
        (4, 4, 'Accepted'),
        (4, 6, 'Pending'),
        (5, 5, 'Rejected'),
        (5, 9, 'Pending'),
        (5, 2, 'Accepted'),
        (6, 6, 'Pending'),
        (7, 6, 'Pending'),
        (7, 3, 'Accepted'),
        (7, 7, 'Rejected'),
        (8, 8, 'Accepted'),
        (8, 1, 'Pending'),
        (9, 9, 'Rejected'),
        (9, 2, 'Pending'),
        (10, 9, 'Pending'),
        (10, 10, 'Accepted'),
        (10, 4, 'Rejected');
    """),
]

populate_appointments = [
    ("populate-appointments", """
    INSERT INTO appointment (caregiver_id, member_id, appointment_date, appointment_time, work_hours, status) VALUES
        (1, 1, '2024-07-01', '10:00:00', 4.0, 'Pending'),
        (2, 2, '2024-07-02', '14:00:00', 3.5, 'Accepted'),
        (3, 3, '2024-07-03', '09:00:00', 5.0, 'Rejected'),
        (4, 4, '2024-07-04', '11:00:00', 2.0, 'Pending'),
        (5, 5, '2024-07-05', '15:00:00', 4.5, 'Accepted'),
        (6, 6, '2024-07-06', '13:00:00', 3.0, 'Rejected'),
        (7, 7, '2024-07-07', '10:30:00', 4.0, 'Pending'),
        (8, 8, '2024-07-08', '12:00:00', 2.5, 'Accepted'),
        (9, 9, '2024-07-09', '14:30:00', 3.5, 'Rejected'),
        (10, 10, '2024-07-10', '09:30:00', 5.0, 'Pending');
    """),
]

populate_messages = [
    ("populate-messages", """
    INSERT INTO message (sender_id, receiver_id, content, status) VALUES
        (1, 11, 'Hello, I am interested in the caregiver position.', 'Sent'),
        (11, 1, 'Thank you for your interest. We will review your application.', 'Delivered'),
        (2, 12, 'Can you provide more details about your experience?', 'Sent'),
        (12, 2, 'Sure, I have 5 years of experience in childcare.', 'Delivered'),
        (3, 13, 'When are you available to start?', 'Sent');
    """),
]   

# Update SQL Statements
update_arman_phone = [
    # Update Arman Armanov's phone number
    ("update-arman-phone", """
    UPDATE app_user
    SET phone_number = '+77773414141'
    WHERE given_name = 'Arman' AND surname = 'Armanov';
    """)
]

update_add_commmission_fee = [
    # Add $0.3 commission fee to the Caregivers’ hourly rate if it's less than $10, or 10% if it's not
    ("add-commission-fee", '''
    UPDATE caregiver
    SET hourly_rate = CASE
        WHEN hourly_rate < 10 THEN hourly_rate + 0.3
        ELSE hourly_rate * 1.10
    END;
    ''')
]

# Delete SQL Statements
delete_jobs_by_amina = [
    # Delete all job ads posted by the member Amina Aminova
    ("delete-jobs-by-amina", '''
    DELETE FROM job_ad
    WHERE member_id IN (
        SELECT m.id FROM member m
        JOIN app_user u ON m.user_id = u.id
        WHERE u.given_name = 'Amina' AND u.surname = 'Aminova'
    );
    ''')
]

delete_users_from_kabanbay = [
    # Delete all members living on Kabanbay Batyr street
    ("delete-users-from-kabanbay", '''
    DELETE FROM app_user
    WHERE id IN (
        SELECT m.user_id FROM member m
        JOIN address a ON m.address_id = a.id
        WHERE a.street = 'Kabanbay Batyr Avenue'
    );
    ''')
]

# Simple SQL Statements
select_accepted_appointments = [
    # Select all appointments that have been accepted
    ("select-accepted-appointments", '''
    SELECT 
        c.id AS caregiver_id,
        u1.given_name AS caregiver_given_name,
        u1.surname AS caregiver_surname,
        m.id AS member_id,
        u2.given_name AS member_given_name,
        u2.surname AS member_surname
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u1 ON c.user_id = u1.id
    JOIN member m ON a.member_id = m.id
    JOIN app_user u2 ON m.user_id = u2.id
    WHERE a.status = 'Accepted';
    ''')
]

select_soft_spoken_jobs = [
    # Select all job ads that require a caregiver with 'soft-spoken' in other requirements
    ("select-soft-spoken-jobs", '''
    SELECT id
        FROM job_ad
        WHERE other_requirements LIKE '%soft-spoken%';
    ''')
]

select_workhours_for_babysitters = [
    # Select total work hours for each caregiver who is a babysitter
    ("select-workhours-for-babysitters", '''
    SELECT a.id AS appointment_id, a.work_hours
        FROM appointment a
        JOIN caregiver c ON a.caregiver_id = c.id
        JOIN care_type ct ON c.care_type_id = ct.id
        WHERE ct.type_name = 'Babysitter';
    ''')
]

list_members_astana_elderly = [
    # List all members in Astana who require elderly care
    ("list-members-astana-elderly", '''
    SELECT u.given_name, u.surname, m.id AS member_id
    FROM member m
    JOIN app_user u ON m.user_id = u.id
    JOIN address a ON m.address_id = a.id
    JOIN job_ad j ON j.member_id = m.id
    JOIN care_type ct ON j.required_caregiver_type_id = ct.id
    WHERE ct.type_name = 'Elderly Care'
        AND a.city = 'Astana'
        AND m.house_rules LIKE '%No pets%';
    ''')
]

# Complex SQL Statements
count_applicants_per_job = [
    # Count the number of applicants for each job ad
    ("count-applicants-per-job", '''
   SELECT
        c.id AS caregiver_id,
        u.given_name,
        u.surname,
        AVG(a.work_hours * c.hourly_rate) AS average_pay
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id
    WHERE a.status = 'Accepted'
    GROUP BY c.id, u.given_name, u.surname;
    ''')
]

total_hours_per_caregiver = [
    # Total hours spent by care givers for all accepted appointments
    ("total-hours-per-caregiver", '''
    SELECT
        c.id AS caregiver_id,
        u.given_name,
        u.surname,
        SUM(a.work_hours) AS total_hours
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id
    WHERE a.status = 'Accepted'
    GROUP BY c.id, u.given_name, u.surname;
    ''')
]

average_pay_caregivers = [
    # Average pay of caregivers based on accepted appointments
    ("average-pay-caregivers", '''
    SELECT
        c.id AS caregiver_id,
        u.given_name,
        u.surname,
        AVG(a.work_hours * c.hourly_rate) AS average_pay
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id
    WHERE a.status = 'Accepted'
    GROUP BY c.id, u.given_name, u.surname;
    ''')
]

nested_query = [
    # Caregivers who earn above average based on accepted appointments
    ("caregivers-above-average", '''
    SELECT
        c.id AS caregiver_id,
        u.given_name,
        u.surname,
        SUM(a.work_hours * c.hourly_rate) AS total_earnings
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id
    WHERE a.status = 'Accepted'
    GROUP BY c.id, u.given_name, u.surname
    HAVING total_earnings > (
        SELECT AVG(sub.earnings)
        FROM (
            SELECT SUM(a2.work_hours * c2.hourly_rate) AS earnings
            FROM appointment a2
            JOIN caregiver c2 ON a2.caregiver_id = c2.id
            WHERE a2.status = 'Accepted'
            GROUP BY c2.id
        ) AS sub
    );
    ''')
]

derived_attributes = [
    # Calculate the total cost to pay for a caregiver for all accepted appointments.
    ("total-cost-per-caregiver", '''
    SELECT
        c.id AS caregiver_id,
        u.given_name,
        u.surname,
        c.hourly_rate,
        SUM(a.work_hours) AS total_hours,
        SUM(a.work_hours * c.hourly_rate) AS total_cost
    FROM appointment a
    JOIN caregiver c ON a.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id
    WHERE a.status = 'Accepted'
    GROUP BY c.id, u.given_name, u.surname, c.hourly_rate;
    ''')
]

view_operations = [
    # View all job applications and the applicants
    ("create-applicants-view", '''
    CREATE OR REPLACE VIEW job_applications_view AS
    SELECT
        ja.id AS application_id,
        ja.job_id,
        ja.status AS application_status,
        ja.date_applied,
        c.id AS caregiver_id,
        u.given_name AS applicant_given_name,
        u.surname AS applicant_surname,
        u.email AS applicant_email,
        u.phone_number AS applicant_phone
    FROM job_application ja
    JOIN caregiver c ON ja.caregiver_id = c.id
    JOIN app_user u ON c.user_id = u.id;
''')
]

# Logic to execute queries with user confirmation
def execute_queries(conn, queries_dict, prompt_message):
    """Execute a list of queries with user confirmation"""
    user_input = input(f"Do you want to {prompt_message}? [y/n]: ").strip().lower()
    if user_input == 'y':
        for name, query in queries_dict:
            result = conn.execute(text(query))
            # Check if the query is a SELECT
            if query.strip().lower().startswith("select"):
                rows = result.fetchall()
                print(f"\033[92mRows returned: {len(rows)}\033[0m")
                for row in rows:
                    print(row)
            else:
                print(f"\033[92mRows affected: {result.rowcount}\033[0m")
            print(f"Completed: {name}")

def main():
    with engine.begin() as conn:
        # Execute create tables querys
        execute_queries(conn, create_queries, "create tables")
        # Execute populate users query
        execute_queries(conn, populate_users, "populate users")
        # Execute populate care types query
        execute_queries(conn, populate_care_types, "populate care types")
        # Execute populate addresses query
        execute_queries(conn, populate_addresses, "populate addresses")
        # Execute populate caregivers query
        execute_queries(conn, populate_caregivers, "populate caregivers")
        # Execute populate members query
        execute_queries(conn, populate_members, "populate members")
        # Execute populate job ads query
        execute_queries(conn, populate_job_ads, "populate job ads")
        # Execute populate job applications query
        execute_queries(conn, populate_job_applications, "populate job applications")
        # Execute populate appointments query
        execute_queries(conn, populate_appointments, "populate appointments")
        # Execute populate messages query
        execute_queries(conn, populate_messages, "populate messages")
        # Execute update Arman phone number query
        execute_queries(conn, update_arman_phone, "update Arman Armanov's phone number")
        # Execute add commission fee to caregivers query
        execute_queries(conn, update_add_commmission_fee, "add commission fee to caregivers' hourly rate")
        # Execute delete jobs by Amina Aminova query
        execute_queries(conn, delete_jobs_by_amina, "delete jobs posted by Amina Aminova")
        # Execute delete users from Kabanbay Batyr street query
        execute_queries(conn, delete_users_from_kabanbay, "delete members living on Kabanbay Batyr street")
        # Execute select accepted appointments query
        execute_queries(conn, select_accepted_appointments, "select accepted appointments")
        # Execute select soft-spoken jobs query
        execute_queries(conn, select_soft_spoken_jobs, "select soft-spoken jobs")
        # Execute select workhours for babysitters query
        execute_queries(conn, select_workhours_for_babysitters, "select work hours for babysitters")
        # Execute list members in Astana requiring elderly care query
        execute_queries(conn, list_members_astana_elderly, "list members in Astana requiring elderly care")
        # Execute count applicants per job query
        execute_queries(conn, count_applicants_per_job, "count applicants per job")
        # Execute total hours per caregiver query
        execute_queries(conn, total_hours_per_caregiver, "calculate total hours per caregiver")
        # Execute average pay of caregivers query
        execute_queries(conn, average_pay_caregivers, "calculate average pay of caregivers")
        # Execute caregivers above average earnings query
        execute_queries(conn, nested_query, "list caregivers earning above average")
        # Execute total cost per caregiver query
        execute_queries(conn, derived_attributes, "calculate total cost per caregiver")
        # Execute create applicants view query
        execute_queries(conn, view_operations, "create job applications view")

if __name__ == "__main__":
    main()
