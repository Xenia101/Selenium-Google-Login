# Selenium Google Login

<img width="210" src="img/img.jpg">

Automatically Google login by selenium [Python]

## Description

- Set variables on `.env` file
    ```json
    // .env

    GOOGLE_ID = "" // Google-email
    GOOGLE_PW = "" // Google-password

    // USER_DATA_DIR = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

    GOOGLE_LOGIN_PATH = "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
    ```

- If you are Google Mobile Two-factor Authentication
    ```python
    ...
    # wait
    # time.sleep(100) <- Remove this comment and prove it
    ...
    ```

## Execution / Test Environment
- Windows10
- Python 3.6
- Selenium 3.141.0