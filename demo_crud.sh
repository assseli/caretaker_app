#!/bin/zsh
# demo_crud.sh - Example CRUD operations using curl for Django API

# Base URL of your deployed Django API (update this to your actual endpoint)
BASE_URL="https://asselderbisova.pythonanywhere.com/api/caregivers/"

# 1. CREATE (POST)
echo "Creating a new caregiver..."
CREATE_RESPONSE=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"name": "Aigerim Akhmetova", "email": "aigerim.akhmetova@example.com", "phone": "87001234567", "gender": "Female", "caregiver_type": "Nurse", "hourly_rate": 15.0}')
echo "Create response: $CREATE_RESPONSE"

# Extract the ID of the created caregiver (adjust the jq/python path as needed)
CAREGIVER_ID=$(echo $CREATE_RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', ''))")

# 2. READ (GET)
echo "Reading caregiver with ID $CAREGIVER_ID..."
curl -s -X GET "${BASE_URL}${CAREGIVER_ID}/" | jq

# Wait for user input before proceeding
echo "Press Enter to continue with reading..."
read

echo "Updating caregiver with ID $CAREGIVER_ID..."
curl -s -X PUT "${BASE_URL}${CAREGIVER_ID}/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Dana Nursultan", "gender": "Female", "caregiver_type": "Nurse", "hourly_rate": 18.0}' | jq

# Wait for user input before proceeding
echo "Press Enter to continue with deletion..."
read

# 4. DELETE (DELETE)
echo "Deleting caregiver with ID $CAREGIVER_ID..."
curl -s -X DELETE "${BASE_URL}${CAREGIVER_ID}/"
echo "Deleted."
