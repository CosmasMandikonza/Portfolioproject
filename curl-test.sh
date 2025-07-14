#!/bin/bash

# Timeline Post API Testing Script
echo "=== Testing Timeline Post API ==="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API endpoint
API_URL="http://localhost:5000/api/timeline_post"

# Generate random data for testing
RANDOM_ID=$((RANDOM % 10000))
CURRENT_DATE=$(date -u +"%a, %d %b %Y %H:%M:%S GMT")
RANDOM_CONTENT="Test post #${RANDOM_ID} - Testing my endpoints with postman and curl!"
RANDOM_EMAIL="test${RANDOM_ID}@example.com"
RANDOM_NAME="TestUser${RANDOM_ID}"

echo -e "${BLUE}🚀 Step 1: Creating a new timeline post...${NC}"
echo "Content: $RANDOM_CONTENT"
echo "Email: $RANDOM_EMAIL"
echo "Name: $RANDOM_NAME"
echo ""

# POST request to create timeline post
POST_RESPONSE=$(curl -s -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "{
    \"content\": \"$RANDOM_CONTENT\",
    \"created_at\": \"$CURRENT_DATE\",
    \"email\": \"$RANDOM_EMAIL\",
    \"id\": $RANDOM_ID,
    \"name\": \"$RANDOM_NAME\"
  }")

echo -e "${GREEN}✅ POST Response:${NC}"
echo "$POST_RESPONSE"
echo ""

# Wait a moment for the data to be saved
sleep 1

echo -e "${BLUE}🔍 Step 2: Fetching all timeline posts to verify...${NC}"

# GET request to retrieve timeline posts
GET_RESPONSE=$(curl -s "$API_URL")

echo -e "${GREEN}✅ GET Response:${NC}"
echo "$GET_RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$GET_RESPONSE"
echo ""

# Check if our post was added
if echo "$GET_RESPONSE" | grep -q "$RANDOM_CONTENT"; then
    echo -e "${GREEN}✅ SUCCESS: Timeline post was successfully added!${NC}"
else
    echo -e "${RED}❌ ERROR: Timeline post was not found in the response${NC}"
fi

echo ""
echo -e "${BLUE}🧪 Bonus: Testing DELETE endpoint (if available)...${NC}"

# DELETE request (assuming endpoint exists)
DELETE_RESPONSE=$(curl -s -X DELETE "$API_URL/$RANDOM_ID" 2>/dev/null)

if [ $? -eq 0 ] && [ -n "$DELETE_RESPONSE" ]; then
    echo -e "${GREEN}✅ DELETE Response:${NC}"
    echo "$DELETE_RESPONSE"
    
    # Verify deletion
    sleep 1
    VERIFY_GET=$(curl -s "$API_URL")
    if echo "$VERIFY_GET" | grep -q "$RANDOM_CONTENT"; then
        echo -e "${RED}❌ DELETE may not have worked - post still exists${NC}"
    else
        echo -e "${GREEN}✅ DELETE successful - post removed${NC}"
    fi
else
    echo -e "${RED}❌ DELETE endpoint not available or failed${NC}"
fi

echo ""
echo -e "${BLUE}=== Test Complete ===${NC}"