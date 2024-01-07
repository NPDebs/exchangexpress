# Exchangexpress: A currency conversion app

This simple Python script allows users to convert currency using real-time exchange rates obtained from the [Open Exchange Rates](https://openexchangerates.org) API.

## Prerequisites (Dependencies)
Before running the application, confirm you have the following installed:

- Python (>= 3.0 recommended)
- Required Python packages: `requests` library

You can install the required packages using the following command:

```bash
pip install requests
```

## Usage
1. Obtain an API key from [Open Exchange Rates](https://openexchangerates.org/signup).

2. Create a file named `APP_ID.py` with the following content:

   ```python
   APP_ID = "YOUR_OPEN_EXCHANGE_RATES_API_KEY"
   ```

   Replace "YOUR_OPEN_EXCHANGE_RATES_API_KEY" with the actual API key you obtained.

3. Run the script:

   ```bash
   python your_script_name.py
   ```
   
   Replace _your_script_name.py_ with the actual API key you obtained.

4. Enter the requested information (amount, source currency, target currency) to get the conversion result.

   - The script fetches the latest exchange rates from the Open Exchange Rates API.
   - The conversion result is displayed in two decimal places.


## Author
NPDebs

## License
This project is licensed CC-BY.
In English, you have the right to share, use, and build upon this creation!