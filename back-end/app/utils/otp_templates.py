def LOG_IN_OTP_TEMPLATE(otp: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xplore - Your One-Time Password</title>
    <style>
        /* General Body Styles */
        body {{
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f7f6; /* Light, calming background */
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            width: 100% !important;
        }}

        /* Container for the email content */
        .email-container {{
            max-width: 600px;
            margin: 40px auto;
            background-color: #ffffff; /* Clean white for the main content */
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }}

        /* Header Section */
        .header {{
            background-color: #5bb381; /* A soothing, professional green */
            padding: 30px;
            text-align: center;
            color: #ffffff;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 600;
        }}

        /* Content Section */
        .content {{
            padding: 40px;
            text-align: center;
            color: #333333;
            line-height: 1.6;
        }}
        .content p {{
            margin-bottom: 20px;
            font-size: 16px;
        }}

        /* OTP Display */
        .otp-display {{
            background-color: #e0f2f1; /* A very light, gentle blue-green */
            color: #00796b; /* A slightly darker, professional blue-green */
            font-size: 36px;
            font-weight: bold;
            letter-spacing: 6px;
            padding: 20px 30px;
            margin: 30px auto;
            border-radius: 6px;
            display: inline-block; /* Allows centering with text-align */
            max-width: fit-content;
            border: 1px dashed #b2dfdb; /* Subtle dashed border for visual emphasis */
        }}

        /* Call to Action/Instructions */
        .instructions {{
            font-size: 14px;
            color: #666666;
            margin-top: 30px;
        }}

        /* Footer Section */
        .footer {{
            background-color: #f0f0f0; /* Light grey for the footer */
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #999999;
            border-top: 1px solid #eeeeee;
        }}
        .footer a {{
            color: #5bb381; /* Matching the header green */
            text-decoration: none;
        }}

        /* Responsive adjustments */
        @media screen and (max-width: 600px) {{
            .email-container {{
                margin: 20px;
                border-radius: 0;
                box-shadow: none;
            }}
            .header, .content, .footer {{
                padding: 20px;
            }}
            .header h1 {{
                font-size: 24px;
            }}
            .otp-display {{
                font-size: 30px;
                padding: 15px 25px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Xplore</h1>
        </div>
        <div class="content">
            <p style="font-size: 18px; font-weight: 500; color: #444;">Welcome back!</p>
            <p>To securely log in to your Xplore account, please use the following One-Time Password (OTP):</p>

            <div class="otp-display">
                {otp} </div>

            <p class="instructions">
                This OTP is valid for the next 3 minutes. Please do not share it with anyone.
            </p>
            <p class="instructions" style="margin-top: 10px;">
                If you did not request this, please ignore this email.
            </p>
        </div>
        <div class="footer">
            <p>&copy; 2025 Xplore. All rights reserved.</p>
            <p><a href="#">Visit Xplore</a></p>
        </div>
    </div>
</body>
</html>"""


def SIGN_UP_OTP_TEMPLATE(otp: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xplore - Welcome! Your Sign Up OTP</title>
    <style>
        /* General Body Styles */
        body {{
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f7f6; /* Light, calming background */
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            width: 100% !important;
        }}

        /* Container for the email content */
        .email-container {{
            max-width: 600px;
            margin: 40px auto;
            background-color: #ffffff; /* Clean white for the main content */
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }}

        /* Header Section */
        .header {{
            background-color: #5bb381; /* A soothing, professional green */
            padding: 30px;
            text-align: center;
            color: #ffffff;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 600;
        }}

        /* Content Section */
        .content {{
            padding: 40px;
            text-align: center;
            color: #333333;
            line-height: 1.6;
        }}
        .content p {{
            margin-bottom: 20px;
            font-size: 16px;
        }}

        /* OTP Display */
        .otp-display {{
            background-color: #e0f2f1; /* A very light, gentle blue-green */
            color: #00796b; /* A slightly darker, professional blue-green */
            font-size: 36px;
            font-weight: bold;
            letter-spacing: 6px;
            padding: 20px 30px;
            margin: 30px auto;
            border-radius: 6px;
            display: inline-block; /* Allows centering with text-align */
            max-width: fit-content;
            border: 1px dashed #b2dfdb; /* Subtle dashed border for visual emphasis */
        }}

        /* Call to Action/Instructions */
        .instructions {{
            font-size: 14px;
            color: #666666;
            margin-top: 30px;
        }}

        /* Footer Section */
        .footer {{
            background-color: #f0f0f0; /* Light grey for the footer */
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #999999;
            border-top: 1px solid #eeeeee;
        }}
        .footer a {{
            color: #5bb381; /* Matching the header green */
            text-decoration: none;
        }}

        /* Responsive adjustments */
        @media screen and (max-width: 600px) {{
            .email-container {{
                margin: 20px;
                border-radius: 0;
                box-shadow: none;
            }}
            .header, .content, .footer {{
                padding: 20px;
            }}
            .header h1 {{
                font-size: 24px;
            }}
            .otp-display {{
                font-size: 30px;
                padding: 15px 25px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Xplore</h1>
        </div>
        <div class="content">
            <p style="font-size: 18px; font-weight: 500; color: #444;">Welcome to Xplore!</p>
            <p>Thanks for signing up! To complete your registration and get started on your career journey, please use the following One-Time Password (OTP):</p>

            <div class="otp-display">
                {otp} </div>

            <p class="instructions">
                This OTP is valid for the next 3 minutes. Please do not share it with anyone.
            </p>
            <p class="instructions" style="margin-top: 10px;">
                If you did not attempt to sign up, please ignore this email.
            </p>
            <p style="margin-top: 30px; font-size: 15px;">
                We're excited to help you explore your future!
            </p>
        </div>
        <div class="footer">
            <p>&copy; 2025 Xplore. All rights reserved.</p>
            <p><a href="#">Visit Xplore</a></p>
        </div>
    </div>
</body>
</html>"""


def RESET_PASSWORD_OTP_TEMPLATE(otp: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xplore - Password Reset OTP</title>
    <style>
        /* General Body Styles */
        body {{
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f7f6; /* Light, calming background */
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            width: 100% !important;
        }}

        /* Container for the email content */
        .email-container {{
            max-width: 600px;
            margin: 40px auto;
            background-color: #ffffff; /* Clean white for the main content */
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            overflow: hidden;
        }}

        /* Header Section */
        .header {{
            background-color: #5bb381; /* A soothing, professional green */
            padding: 30px;
            text-align: center;
            color: #ffffff;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            font-weight: 600;
        }}

        /* Content Section */
        .content {{
            padding: 40px;
            text-align: center;
            color: #333333;
            line-height: 1.6;
        }}
        .content p {{
            margin-bottom: 20px;
            font-size: 16px;
        }}

        /* OTP Display */
        .otp-display {{
            background-color: #e0f2f1; /* A very light, gentle blue-green */
            color: #00796b; /* A slightly darker, professional blue-green */
            font-size: 36px;
            font-weight: bold;
            letter-spacing: 6px;
            padding: 20px 30px;
            margin: 30px auto;
            border-radius: 6px;
            display: inline-block; /* Allows centering with text-align */
            max-width: fit-content;
            border: 1px dashed #b2dfdb; /* Subtle dashed border for visual emphasis */
        }}

        /* Call to Action/Instructions */
        .instructions {{
            font-size: 14px;
            color: #666666;
            margin-top: 30px;
        }}

        /* Footer Section */
        .footer {{
            background-color: #f0f0f0; /* Light grey for the footer */
            padding: 20px;
            text-align: center;
            font-size: 12px;
            color: #999999;
            border-top: 1px solid #eeeeee;
        }}
        .footer a {{
            color: #5bb381; /* Matching the header green */
            text-decoration: none;
        }}

        /* Responsive adjustments */
        @media screen and (max-width: 600px) {{
            .email-container {{
                margin: 20px;
                border-radius: 0;
                box-shadow: none;
            }}
            .header, .content, .footer {{
                padding: 20px;
            }}
            .header h1 {{
                font-size: 24px;
            }}
            .otp-display {{
                font-size: 30px;
                padding: 15px 25px;
            }}
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Xplore</h1>
        </div>
        <div class="content">
            <p style="font-size: 18px; font-weight: 500; color: #444;">Password Reset Request</p>
            <p>We received a request to reset your password for your Xplore account. Please use the following One-Time Password (OTP) to proceed:</p>

            <div class="otp-display">
                {otp} </div>

            <p class="instructions">
                This OTP is valid for the next 3 minutes. Please enter it on the password reset screen.
            </p>
            <p class="instructions" style="margin-top: 10px; font-weight: bold; color: #d9534f;">
                If you did not request a password reset, please ignore this email immediately. Your account is safe.
            </p>
        </div>
        <div class="footer">
            <p>&copy; 2025 Xplore. All rights reserved.</p>
            <p><a href="#">Visit Xplore</a></p>
        </div>
    </div>
</body>
</html>"""
