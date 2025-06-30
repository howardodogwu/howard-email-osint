# OSINT Email Security Tool

## Overview

This Python-based tool leverages the HaveIBeenPwned API to:

- Check if an email address appears in any known data breaches.
- Provide actionable security recommendations.

## Features

- **Email Validation**: Ensure email format is correct.
- **Breach Check**: Retrieve details about breaches affecting the email.
- **Security Recommendations**: Suggest best practices (e.g., password changes, MFA).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/howardodogwu/osint-email-security-tool.git
   cd osint-email-security-tool
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

## Setup

1. Get a free API key from [HaveIBeenPwned](https://haveibeenpwned.com/API/Key)

2. Create a `.env` file in the project root:

   ```bash
   # Create the .env file
   touch .env

   # Add your API key to the .env file
   echo "EMAIL_API_KEY=your_api_key_here" >> .env
   ```

   Replace `your_api_key_here` with your actual API key.

   **⚠️ Security Note**: The `.env` file is automatically ignored by git to prevent accidentally committing your API key. Never commit this file to version control.

## Usage

### Option 1: Using the shell script (Recommended)

```bash
./run_app.sh
```

### Option 2: Manual execution

```bash
export PATH="/Users/hackerodogwu/Library/Python/3.9/bin:$PATH"
streamlit run app.py
```

### Option 3: Direct execution

```bash
python3 -m streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. Enter an email address in the input field
2. Click "Scan for Breaches 🚨"
3. View the results:
   - If breaches are found, you'll see details about each breach
   - If no breaches are found, you'll see a success message
   - Security recommendations will be provided

## API Information

This tool uses the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) which:

- Is free to use (with rate limiting)
- Requires an API key for authentication
- Provides breach data for email addresses

## Security Best Practices

- ✅ **Never commit your `.env` file** - It's automatically ignored by git
- ✅ **Keep your API key private** - Don't share it in public repositories
- ✅ **Use environment variables** - The app loads API keys from `.env` file
- ✅ **Regular security checks** - Use this tool to monitor your email addresses
- ✅ **Change passwords** - If breaches are found, change passwords immediately
- ✅ **Enable MFA** - Use Multi-Factor Authentication wherever possible

## Troubleshooting

If you get "command not found: streamlit", make sure you've:

1. Installed the dependencies with `pip3 install -r requirements.txt`
2. Added the Python user bin directory to your PATH
3. Or use the provided `run_app.sh` script

If you get "API key not found" error:

1. Make sure you've created a `.env` file in the project root
2. Verify your API key is correctly set in the `.env` file
3. Check that the `.env` file format is correct: `EMAIL_API_KEY=your_actual_key`

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
