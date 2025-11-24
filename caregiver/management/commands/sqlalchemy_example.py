from sqlalchemy import create_engine, text

# Update these with your actual MySQL credentials and database name
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_NAME = 'your_db_name'

# SQLAlchemy connection string
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

def main():
    with engine.connect() as conn:
        # Example 1: Select all caregivers
        print("All caregivers:")
        result = conn.execute(text("SELECT * FROM caregiver_caregiver"))
        for row in result:
            print(row)

        # Example 2: Insert a new caregiver
        print("\nInserting a new caregiver...")
        conn.execute(
            text("""
                INSERT INTO caregiver_caregiver (name, gender, caregiver_type, hourly_rate)
                VALUES (:name, :gender, :type, :rate)
            """),
            {"name": "Example Caregiver", "gender": "Female", "type": "Nurse", "rate": 30.00}
        )
        conn.commit()
        print("Inserted new caregiver.")

        # Example 3: Update a caregiver's hourly rate
        print("\nUpdating caregiver's hourly rate...")
        conn.execute(
            text("""
                UPDATE caregiver_caregiver SET hourly_rate = :rate WHERE name = :name
            """),
            {"rate": 35.00, "name": "Example Caregiver"}
        )
        conn.commit()
        print("Updated hourly rate.")

        # Example 4: Delete a caregiver
        print("\nDeleting caregiver...")
        conn.execute(
            text("DELETE FROM caregiver_caregiver WHERE name = :name"),
            {"name": "Example Caregiver"}
        )
        conn.commit()
        print("Deleted caregiver.")

if __name__ == "__main__":
    main()
