# Xplore Backend

## Endpoints:

- #### Auth
    - Student:
        - Sign Up: `/sign-up`
        - Log In: `/log-in`
        - Send OTP to signUp: `/send-sign-up-otp`
        - Send OTP to logIn: `/send-log-in-otp`
        - Send OTP to reset password: `/send-reset-password-otp`
        - Verify OTP: `/verify-otp`
- #### AI Questionnaire & Career Generation
    - Generate psychometric questions: `/questions`
    - Generate careers for the student with psychometric report: `/careers`
- #### Student Profile
    - Fetch student data: `/data`
    - Fetch student psychometrics: `/psychometrics`
    - Delete student account: `/delete`

### Notes and Resources

- [No-SQL databases](https://realpython.com/introduction-to-mongodb-and-python/)