#!/bin/bash

# Hardcoded sensitive data (API Key)
API_KEY="1234567890abcdefg"
URL="https://example.com/api/data"

# Make API request with the sensitive key
response=$(curl -s -H "Authorization: Bearer $API_KEY" $URL)

if [[ $? -eq 0 ]]; then
  echo "Data fetched successfully!"
else
  echo "Failed to fetch data"
fi
