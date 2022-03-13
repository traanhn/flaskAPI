# flaskAPI


## Installation

After cloning this repo into a local directory. Running the following commands in Bash 
The docker container will be created and the Flask app will be running

Note: Replace the **REPLACE_BY_YOUR_KEY** with any value of your choice 

```bash
cd flaskAPI
echo APP_API_KEY=REPLACE_BY_YOUR_KEY >> .env
docker-compose build
docker-compose up
```
## Usage

When the app is running. 
You could use PostMan to test the API endpoints
These commands below for testing in terminal. Updated the **x-api-key** using the same value as the **APP_API_KEY** entered above 

### Examples: 

GET 
```bash
curl --location --request GET 'http://127.0.0.1:5000/api/user/500' \
--header 'x-api-key: egkewjgbg' \
--header 'Content-Type: application/json'
```

DELETE 
```bash
curl --location --request DELETE 'http://127.0.0.1:5000/api/user/500' \
--header 'x-api-key: egkewjgbg' \
--header 'Content-Type: application/json' 
```

PUT 
```bash
curl --location --request PUT 'http://127.0.0.1:5000/api/user/501' \
--header 'x-api-key: egkewjgbg' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_id": 501,
    "first_name": "Test",
    "last_name": "Denniston",
    "gender": "adennistondw@hao123.com",
    "email": "Non-binary",
    "ip_address": "76.181.31.23",
    "country_code": "PH"
}'
```

POST 
```bash
curl --location --request POST 'http://127.0.0.1:5000/api/user' \
--header 'x-api-key: egkewjgbg' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Test",
    "last_name": "Denniston",
    "gender": "adennistondw@hao123.com",
    "email": "Non-binary",
    "ip_address": "76.181.31.23",
    "country_code": "PH"
}'
```







## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)