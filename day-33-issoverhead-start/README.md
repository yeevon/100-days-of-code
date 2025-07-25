# ISS Overhead Notifier

This python script checks if the International Space Station (ISS) is  curretnly flying over your location and
if its dark outside and emails you to go outside to watch it flyby.

## Features

- Uses real-time data from:
  - Open Notify ISS API
  - Sunrise-Sunset API
- Sends an email alert when conditions are met (ISS overhead and Dark outside)
- Runs continuously in the background every 60 seconds

## Requirements
- Python 3.6
- A Gmail account for sending notifications
- ENV variable for email password

## Setup 
1. **Install Dependencies**

Create a virtual env and install required packages
```bash
   pip install python-dotenv requests
```

2. **Create a .env File**

In the same directory as your script, create a .env file with your Gmail password:
```.env
PW=your_gmail_app_password
```
Use an App Password if you have 2FA enabled on your Gmail account.

3. **Edit your location**

Replace the coordinates in the script with your actual latitude and longitude:
```python
MY_LAT = XXX  # Your latitude
MY_LONG = -XXX  # Your longitude
```
You can use latlong.net to find your longitude / latitude

4. **Set your recipient email**

Update the send_email function to set the correct sender/recipient emails.

5. **Run the script**

```bash
   python iss_notifier.py
```