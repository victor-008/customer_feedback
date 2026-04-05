# API Documentation

## POST /feedback

### Request
```json
{
    "text": "Internet is slow"
}

### Response
{
    "category" : "complaint",
    "prolem" : "slow internet",
    "solution" : "restart router....etc"
}

## Get /feedback

Returns all stored feedback