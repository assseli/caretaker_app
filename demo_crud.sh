#!/bin/zsh
# demo_crud.sh - Example CRUD operations using curl for Django API

# Base URL of your deployed Django API (update this to your actual endpoint)
BASE_URL="https://your-public-api-url.com/api/caregivers/"

# 1. CREATE (POST)
echo "Creating a new caregiver..."
CREATE_RESPONSE=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "phone": "1234567890"}')
echo "Create response: $CREATE_RESPONSE"

# Extract the ID of the created caregiver (adjust the jq/python path as needed)
CAREGIVER_ID=$(echo $CREATE_RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', ''))")

# 2. READ (GET)
echo "Reading caregiver with ID $CAREGIVER_ID..."
curl -s -X GET "${BASE_URL}${CAREGIVER_ID}/" | jq

# 3. UPDATE (PUT)
echo "Updating caregiver with ID $CAREGIVER_ID..."
curl -s -X PUT "${BASE_URL}${CAREGIVER_ID}/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane@example.com", "phone": "0987654321"}' | jq

# 4. DELETE (DELETE)
echo "Deleting caregiver with ID $CAREGIVER_ID..."
curl -s -X DELETE "${BASE_URL}${CAREGIVER_ID}/"
echo "Deleted."

# 5. LIST (GET)
echo "Listing all caregivers..."
curl -s -X GET "$BASE_URL" | jq
