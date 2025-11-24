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
	("1.3", """
	CREATE TABLE IF NOT EXISTS caregiver_member (
		id INT AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(100) NOT NULL,
		house_rules TEXT NOT NULL,
		dependent_description TEXT NOT NULL
	);
	"""),
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
	("2.1", """
	INSERT INTO caregiver_member (id, name, house_rules, dependent_description)
	VALUES (1001, 'Aigerim Akhmetov', 'No pets.', 'Elderly Care required')
	ON DUPLICATE KEY UPDATE name=name;
	"""),
	("2.2", """
	INSERT INTO caregiver_address (id, member_id, house_number, street, town)
	VALUES (1001, 1001, '12A', 'Main Street', 'Astana')
	ON DUPLICATE KEY UPDATE house_number=house_number;
	"""),
	("2.3", """
	INSERT INTO caregiver_caregiver (id, name, gender, caregiver_type, hourly_rate)
	VALUES (1001, 'Ivan Ivanov', 'Male', 'Babysitter', 30.00)
	ON DUPLICATE KEY UPDATE name=name;
	"""),
	("2.4", """
	INSERT INTO caregiver_job (id, member_id, required_caregiver_type, other_requirements, date_posted)
	VALUES (1001, 1001, 'Elderly Care', 'Looking for a soft-spoken caregiver', CURDATE())
	ON DUPLICATE KEY UPDATE required_caregiver_type=required_caregiver_type;
	"""),
	("2.5", """
	INSERT INTO caregiver_job (id, member_id, required_caregiver_type, other_requirements, date_posted)
	VALUES (1002, 1001, 'Babysitter', 'Babysitter needed for evenings', CURDATE())
	ON DUPLICATE KEY UPDATE required_caregiver_type=required_caregiver_type;
	"""),
	("2.6", """
	INSERT INTO caregiver_job_application (id, job_id, caregiver_id, date_applied)
	VALUES (1001, 1001, 1001, CURDATE())
	ON DUPLICATE KEY UPDATE job_id=job_id;
	"""),
	("2.7", """
	INSERT INTO caregiver_appointment (id, caregiver_id, member_id, appointment_date, appointment_time, work_hours, status)
	VALUES (1001, 1001, 1001, CURDATE(), '09:00:00', 4.0, 'Accepted')
	ON DUPLICATE KEY UPDATE status=status;
	"""),
	("3.1", """
	UPDATE caregiver_user
	SET phone_number = '+77773414141'
	WHERE given_name = 'Arman' AND surname = 'Armanov';
	"""),
	("3.2", """
	UPDATE caregiver_caregiver
	SET hourly_rate = CASE
		WHEN hourly_rate < 10 THEN hourly_rate + 0.3
		ELSE hourly_rate * 1.10
	END;
	"""),
	("4.1", """
	DELETE FROM caregiver_job
	WHERE member_id IN (
		SELECT id FROM caregiver_member WHERE name = 'Amina Aminova'
	);
	"""),
	("4.2", """
	DELETE FROM caregiver_member
	WHERE id IN (
		SELECT member_id FROM caregiver_address WHERE street = 'Kabanbay Batyr'
	);
	"""),
	("5.1", """
		SELECT c.name AS caregiver_name, m.name AS member_name
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		JOIN caregiver_member m ON a.member_id = m.id
		WHERE a.status = 'Accepted';
	"""),
	("5.2", """
		SELECT id FROM caregiver_job
		WHERE other_requirements LIKE '%soft-spoken%';
	"""),
	("5.3", """
		SELECT a.work_hours
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE c.caregiver_type = 'Babysitter';
	"""),
	("5.4", """
		SELECT m.name
		FROM caregiver_member m
		JOIN caregiver_job j ON m.id = j.member_id
		JOIN caregiver_address a ON m.id = a.member_id
		WHERE j.required_caregiver_type = 'Elderly Care'
			AND a.town = 'Astana'
			AND m.house_rules LIKE '%No pets.%';
	"""),
	("6.1", """
		SELECT j.id AS job_id, m.name AS member_name, COUNT(ja.id) AS applicant_count
		FROM caregiver_job j
		JOIN caregiver_member m ON j.member_id = m.id
		LEFT JOIN caregiver_job_application ja ON j.id = ja.job_id
		GROUP BY j.id, m.name;
	"""),
	("6.2", """
		SELECT c.name AS caregiver_name, SUM(a.work_hours) AS total_hours
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted'
		GROUP BY c.name;
	"""),
	("6.3", """
		SELECT AVG(c.hourly_rate) AS avg_pay
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted';
	"""),
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
	("7", """
		SELECT c.name, SUM(a.work_hours * c.hourly_rate) AS total_cost
		FROM caregiver_appointment a
		JOIN caregiver_caregiver c ON a.caregiver_id = c.id
		WHERE a.status = 'Accepted'
		GROUP BY c.name;
	"""),
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
			if user_input == 'y':
				try:
					result = conn.execute(text(sql))
					# Try to fetch results if it's a SELECT
					if sql.strip().lower().startswith('select'):
						rows = result.fetchall()
						if rows:
							for row in rows:
								print(row)
						else:
							print("No results.")
					else:
						print("Query executed.")
				except Exception as e:
					print(f"Error executing query {label}: {e}")
			else:
				print(f"Skipped query {label}.")
		
if __name__ == "__main__":
	main()
