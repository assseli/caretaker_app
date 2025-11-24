from sqlalchemy import create_engine, text

# Update these with your actual MySQL credentials and database name
DB_USER = 'root'
DB_PASSWORD = 'mySql2%4024'
DB_HOST = 'localhost'
DB_NAME = 'caregiver_db'
DB_PORT = 3306
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# 1. Create SQL stetements
queries = [
	# 1.1: Create the general caregiver_user table to store user account information
	("1.1", """
	CREATE TABLE IF NOT EXISTS caregiver_user (
		id INT AUTO_INCREMENT PRIMARY KEY,
		email VARCHAR(254) NOT NULL UNIQUE,
		given_name VARCHAR(30) NOT NULL,
		surname VARCHAR(30) NOT NULL,
		city VARCHAR(50) NOT NULL,
		phone_number VARCHAR(20) NOT NULL,
		profile_description TEXT
	);
	"""),
	# 1.2: Create the caregivers table to store caregiver profiles
	("1.2", """
	CREATE TABLE IF NOT EXISTS caregiver_caregiver (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(100) NOT NULL,
		photo VARCHAR(100),
		gender VARCHAR(10) NOT NULL,
		caregiver_type VARCHAR(50) NOT NULL,
		hourly_rate DECIMAL(6,2) NOT NULL
	);
	"""),
	# 1.3: Create the caregiver_member table to store member (client) information
	("1.3", """
	CREATE TABLE IF NOT EXISTS caregiver_member (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(100) NOT NULL,
		house_rules TEXT NOT NULL,
		dependent_description TEXT NOT NULL
	);
	"""),
	# 1.4: Create the caregiver_address table to store addresses for members
	("1.4", """
	CREATE TABLE IF NOT EXISTS caregiver_address (
		id INT AUTO_INCREMENT PRIMARY KEY,
		member_id INT NOT NULL,
		house_number VARCHAR(10) NOT NULL,
		street VARCHAR(100) NOT NULL,
		town VARCHAR(50) NOT NULL,
		FOREIGN KEY (member_id) REFERENCES caregiver_member(id) ON DELETE CASCADE
	);
	"""),
	# 1.5: Create the caregiver_job table to store job postings by members
	("1.5", """
	CREATE TABLE IF NOT EXISTS caregiver_job (
		id INT AUTO_INCREMENT PRIMARY KEY,
		member_id INT NOT NULL,
		required_caregiver_type VARCHAR(50) NOT NULL,
		other_requirements TEXT NOT NULL,
		date_posted DATE NOT NULL,
		FOREIGN KEY (member_id) REFERENCES caregiver_member(id) ON DELETE CASCADE
	);
	"""),
	# 1.6: Create the caregiver_job_application table to store applications to jobs
	("1.6", """
	CREATE TABLE IF NOT EXISTS caregiver_job_application (
		id INT AUTO_INCREMENT PRIMARY KEY,
		job_id INT NOT NULL,
		caregiver_id INT NOT NULL,
		date_applied DATE NOT NULL,
		FOREIGN KEY (job_id) REFERENCES caregiver_job(id) ON DELETE CASCADE,
		FOREIGN KEY (caregiver_id) REFERENCES caregiver_caregiver(id) ON DELETE CASCADE
	);
	"""),
	# 1.7: Create the caregiver_appointment table to store scheduled appointments
	("1.7", """
	CREATE TABLE IF NOT EXISTS caregiver_appointment (
		id INT AUTO_INCREMENT PRIMARY KEY,
		caregiver_id INT NOT NULL,
		member_id INT NOT NULL,
		appointment_date DATE NOT NULL,
		appointment_time TIME NOT NULL,
		work_hours DECIMAL(4,2) NOT NULL,
		status VARCHAR(20) NOT NULL,
		FOREIGN KEY (caregiver_id) REFERENCES caregiver_caregiver(id) ON DELETE CASCADE,
		FOREIGN KEY (member_id) REFERENCES caregiver_member(id) ON DELETE CASCADE
	);
	"""),
	# 2.1: Insert 10 demo users into caregiver_user (including Arman Armanov)
	("2.1", """
	INSERT INTO caregiver_user (id, email, given_name, surname, city, phone_number, profile_description) VALUES
	(1001, 'arman.armanov@example.com', 'Arman', 'Armanov', 'Astana', '+77773414551', 'Experienced caregiver and user of the system'),
	(1002, 'aigerim.akhmetov@example.com', 'Aigerim', 'Akhmetov', 'Almaty', '+77770000001', 'Friendly and responsible'),
	(1003, 'daniyar.nursultan@example.com', 'Daniyar', 'Nursultan', 'Shymkent', '+77770000002', 'Patient and caring'),
	(1004, 'amina.aminova@example.com', 'Amina', 'Aminova', 'Astana', '+77770000003', 'Loves working with children'),
	(1005, 'yerbolat.zhanibek@example.com', 'Yerbolat', 'Zhanibek', 'Karaganda', '+77770000004', 'Specializes in elderly care'),
	(1006, 'madina.tulegenova@example.com', 'Madina', 'Tulegenova', 'Pavlodar', '+77770000005', 'Energetic and creative'),
	(1007, 'ruslan.karimov@example.com', 'Ruslan', 'Karimov', 'Astana', '+77770000006', 'Organized and punctual'),
	(1008, 'aliya.saparova@example.com', 'Aliya', 'Saparova', 'Almaty', '+77770000007', 'Great with kids'),
	(1009, 'nursultan.abishev@example.com', 'Nursultan', 'Abishev', 'Shymkent', '+77770000008', 'Experienced in special needs care'),
	(1010, 'zhanel.kairat@example.com', 'Zhanel', 'Kairat', 'Astana', '+77770000009', 'Excellent communicator')
	ON DUPLICATE KEY UPDATE email=VALUES(email);
	"""),
	# 2.2: Insert 10 demo members (clients) into caregiver_member
	("2.2", """
	INSERT INTO caregiver_member (id, name, house_rules, dependent_description) VALUES
	(1001, 'Aigerim Akhmetov', 'No pets.', 'Elderly Care required'),
	(1002, 'Daniyar Nursultan', 'No smoking.', 'Child with special needs'),
	(1003, 'Amina Aminova', 'Quiet hours after 10pm.', 'Assistance with mobility'),
	(1004, 'Yerbolat Zhanibek', 'No visitors.', 'Post-surgery care'),
	(1005, 'Madina Tulegenova', 'Vegetarian meals only.', 'Elderly Care required'),
	(1006, 'Ruslan Karimov', 'No loud music.', 'Child care'),
	(1007, 'Aliya Saparova', 'No pets.', 'Assistance with medication'),
	(1008, 'Nursultan Abishev', 'No smoking.', 'Elderly Care required'),
	(1009, 'Zhanel Kairat', 'Quiet hours after 9pm.', 'Child with allergies'),
	(1010, 'Aruzhan Serik', 'No visitors.', 'Assistance with daily activities')
	ON DUPLICATE KEY UPDATE name=VALUES(name);
	"""),
	# 2.3: Insert 10 demo addresses for members into caregiver_address
	("2.2", """
	INSERT INTO caregiver_address (id, member_id, house_number, street, town) VALUES
	(1001, 1001, '12A', 'Main Street', 'Astana'),
	(1002, 1002, '34B', 'Abay Avenue', 'Almaty'),
	(1003, 1003, '56C', 'Kabanbay Batyr', 'Shymkent'),
	(1004, 1004, '78D', 'Tauelsizdik', 'Astana'),
	(1005, 1005, '90E', 'Satpayev', 'Karaganda'),
	(1006, 1006, '21F', 'Pushkin', 'Pavlodar'),
	(1007, 1007, '43G', 'Zhibek Zholy', 'Almaty'),
	(1008, 1008, '65H', 'Dostyk', 'Astana'),
	(1009, 1009, '87I', 'Al-Farabi', 'Shymkent'),
	(1010, 1010, '10J', 'Bogenbay Batyr', 'Astana')
	ON DUPLICATE KEY UPDATE house_number=VALUES(house_number);
	"""),
	# 2.4: Insert 10 demo caregivers into caregiver_caregiver
	("2.3", """
	INSERT INTO caregiver_caregiver (id, name, gender, caregiver_type, hourly_rate) VALUES
	(1001, 'Ivan Ivanov', 'Male', 'Babysitter', 30.00),
	(1002, 'Olga Petrova', 'Female', 'Elderly Care', 35.00),
	(1003, 'Sergey Smirnov', 'Male', 'Child Care', 28.00),
	(1004, 'Aigerim Zhumabek', 'Female', 'Babysitter', 32.00),
	(1005, 'Dmitry Pavlov', 'Male', 'Elderly Care', 40.00),
	(1006, 'Aliya Kenzhe', 'Female', 'Child Care', 29.00),
	(1007, 'Nikita Sokolov', 'Male', 'Babysitter', 27.00),
	(1008, 'Zhanna Tulegen', 'Female', 'Elderly Care', 38.00),
	(1009, 'Maksat Nurlybek', 'Male', 'Child Care', 31.00),
	(1010, 'Saule Amanova', 'Female', 'Babysitter', 33.00)
	ON DUPLICATE KEY UPDATE name=VALUES(name);
	"""),
	# 2.5: Insert 10 demo jobs into caregiver_job
	("2.4", """
	INSERT INTO caregiver_job (id, member_id, required_caregiver_type, other_requirements, date_posted) VALUES
	(1001, 1001, 'Elderly Care', 'Looking for a soft-spoken caregiver', CURDATE()),
	(1002, 1002, 'Child Care', 'Babysitter needed for evenings', CURDATE()),
	(1003, 1003, 'Elderly Care', 'Experience with mobility assistance', CURDATE()),
	(1004, 1004, 'Babysitter', 'Energetic and patient', CURDATE()),
	(1005, 1005, 'Child Care', 'Knowledge of allergies', CURDATE()),
	(1006, 1006, 'Elderly Care', 'Can help with medication', CURDATE()),
	(1007, 1007, 'Babysitter', 'Creative with activities', CURDATE()),
	(1008, 1008, 'Child Care', 'Flexible hours', CURDATE()),
	(1009, 1009, 'Elderly Care', 'Gentle and reliable', CURDATE()),
	(1010, 1010, 'Babysitter', 'Good with pets', CURDATE())
	ON DUPLICATE KEY UPDATE required_caregiver_type=VALUES(required_caregiver_type);
	"""),
	# 2.6: Insert 10 demo job applications into caregiver_job_application
	("2.5", """
	INSERT INTO caregiver_job_application (id, job_id, caregiver_id, date_applied) VALUES
	(1001, 1001, 1001, CURDATE()),
	(1002, 1002, 1002, CURDATE()),
	(1003, 1003, 1003, CURDATE()),
	(1004, 1004, 1004, CURDATE()),
	(1005, 1005, 1005, CURDATE()),
	(1006, 1006, 1006, CURDATE()),
	(1007, 1007, 1007, CURDATE()),
	(1008, 1008, 1008, CURDATE()),
	(1009, 1009, 1009, CURDATE()),
	(1010, 1010, 1010, CURDATE())
	ON DUPLICATE KEY UPDATE job_id=VALUES(job_id);
	"""),
	# 2.7: Insert 10 demo appointments into caregiver_appointment
	("2.6", """
	INSERT INTO caregiver_appointment (id, caregiver_id, member_id, appointment_date, appointment_time, work_hours, status) VALUES
	(1001, 1001, 1001, CURDATE(), '09:00:00', 4.0, 'Accepted'),
	(1002, 1002, 1002, CURDATE(), '10:00:00', 3.5, 'Pending'),
	(1003, 1003, 1003, CURDATE(), '11:00:00', 2.0, 'Accepted'),
	(1004, 1004, 1004, CURDATE(), '12:00:00', 5.0, 'Cancelled'),
	(1005, 1005, 1005, CURDATE(), '13:00:00', 4.5, 'Accepted'),
	(1006, 1006, 1006, CURDATE(), '14:00:00', 3.0, 'Accepted'),
	(1007, 1007, 1007, CURDATE(), '15:00:00', 2.5, 'Pending'),
	(1008, 1008, 1008, CURDATE(), '16:00:00', 4.0, 'Accepted'),
	(1009, 1009, 1009, CURDATE(), '17:00:00', 3.5, 'Accepted'),
	(1010, 1010, 1010, CURDATE(), '18:00:00', 5.0, 'Accepted')
	ON DUPLICATE KEY UPDATE status=VALUES(status);
	"""),
	# 3.1: Update Arman Armanov's phone number in caregiver_user
	("3.1", """
	UPDATE caregiver_user
	SET phone_number = '+77773414141'
	WHERE given_name = 'Arman' AND surname = 'Armanov';
	"""),
	# 3.2: Update hourly rates for all caregivers in caregiver_caregiver
	("3.2", """
	UPDATE caregiver_caregiver
	SET hourly_rate = CASE
		WHEN hourly_rate < 10 THEN hourly_rate + 0.3
		ELSE hourly_rate * 1.10
	END;
	"""),
	# 4.1: Delete jobs for members named 'Amina Aminova'
	("4.1", """
	DELETE FROM caregiver_job
	WHERE member_id IN (
		SELECT id FROM caregiver_member WHERE name = 'Amina Aminova'
	);
	"""),
	# 4.2: Delete members who have an address on 'Kabanbay Batyr' street
	("4.2", """
	DELETE FROM caregiver_member
	WHERE id IN (
		SELECT member_id FROM caregiver_address WHERE street = 'Kabanbay Batyr'
	);
	"""),
	# 5.1: Select all accepted appointments with caregiver and member names
	("5.1", """
		SELECT c.name AS caregiver_name, m.name AS member_name
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		JOIN caregiver_member m ON a.member_id = m.id
		WHERE a.status = 'Accepted';
	"""),
	# 5.2: Select job IDs where requirements mention 'soft-spoken'
	("5.2", """
		SELECT id FROM caregiver_job
		WHERE other_requirements LIKE '%soft-spoken%';
	"""),
	# 5.3: Select work hours for appointments with caregivers of type 'Babysitter'
	("5.3", """
		SELECT a.work_hours
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE c.caregiver_type = 'Babysitter';
	"""),
	# 5.4: Select member names for elderly care jobs in Astana with 'No pets.' rule
	("5.4", """
		SELECT m.name
		FROM caregiver_member m
		JOIN caregiver_job j ON m.id = j.member_id
		JOIN caregiver_address a ON m.id = a.member_id
		WHERE j.required_caregiver_type = 'Elderly Care'
			AND a.town = 'Astana'
			AND m.house_rules LIKE '%No pets.%';
	"""),
	# 6.1: Select job IDs, member names, and applicant counts for each job
	("6.1", """
		SELECT j.id AS job_id, m.name AS member_name, COUNT(ja.id) AS applicant_count
		FROM caregiver_job j
		JOIN caregiver_member m ON j.member_id = m.id
		LEFT JOIN caregiver_job_application ja ON j.id = ja.job_id
		GROUP BY j.id, m.name;
	"""),
	# 6.2: Select caregiver names and total accepted work hours
	("6.2", """
		SELECT c.name AS caregiver_name, SUM(a.work_hours) AS total_hours
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted'
		GROUP BY c.name;
	"""),
	# 6.3: Select average hourly pay for accepted appointments
	("6.3", """
		SELECT AVG(c.hourly_rate) AS avg_pay
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted';
	"""),
	# 6.4: Select caregivers with above-average hourly rates for accepted appointments
	("6.4", """
		SELECT c.name, c.hourly_rate
		FROM caregiver_caregiver c
		JOIN caregiver_appointment a ON c.id = a.caregiver_id
		WHERE a.status = 'Accepted'
		GROUP BY c.id
		HAVING c.hourly_rate > (
			SELECT AVG(c2.hourly_rate)
			FROM caregiver_appointment a2
			JOIN caregiver_caregiver c2 ON a2.caregiver_id = c2.id
			WHERE a2.status = 'Accepted'
		);
	"""),
	# 7: Select total cost per caregiver for accepted appointments
	("7", """
		SELECT c.name, SUM(a.work_hours * c.hourly_rate) AS total_cost
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted'
		GROUP BY c.name;
	"""),
	# 8: Select all job applications with caregiver, job, and member names
	("8", """
		SELECT ja.id AS application_id, c.name AS caregiver_name, j.id AS job_id, m.name AS member_name
		FROM caregiver_job_application ja
		JOIN caregiver_caregiver c ON ja.caregiver_id = c.id
		JOIN caregiver_job j ON ja.job_id = j.id
		JOIN caregiver_member m ON j.member_id = m.id;
	""")
]

def main():
	with engine.connect() as conn:
		for label, sql in queries:
			print(f"\nQuery {label}:")
			print(sql)
			user_input = input("Execute this query? [y/n]: ").strip().lower()
			if user_input == '' or user_input == 'y':
				try:
					result = conn.execute(text(sql))
					# Try to fetch results if it's a SELECT
					if sql.strip().lower().startswith('select'):
						rows = result.fetchall()
						if rows:
							for row in rows:
								print(f"\033[92m{row}\033[0m")  # Green text
						else:
							print("No results.")
					else:
						print(f"\033[92mQuery executed. Rows affected: {result.rowcount}\033[0m")
				except Exception as e:
					print(f"Error executing query {label}: {e}")
			else:
				print(f"Skipped query {label}.")
		
if __name__ == "__main__":
	main()
