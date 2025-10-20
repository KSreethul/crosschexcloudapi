# crosschexcloudapi
[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-LGPL--3.0-green)](https://www.gnu.org/licenses/lgpl-3.0.html)  
**CrossChexCloudAPI Python Library for Anviz Biometric Devices**

`crosschexcloudapi` is a Python library that simplifies interaction with Anviz CrossChex Cloud API. It provides high-level methods for fetching attendance records, managing authentication tokens, and handling API communication securely.

---

## Features

- Fetch and manage authentication tokens with automatic renewal.
- Retrieve attendance logs for employees between specific time ranges.
- Handle paginated API responses automatically.
- Lightweight and minimal dependencies (`requests` only).
- Fully compatible with Python 3.10+.

---

## Installation

Install via pip:

```bash
pip install crosschexcloudapi
````

---

## Usage

```python
from crosschexcloudapi import CrossChexCloudAPI
from datetime import datetime

# Initialize the CrossChexCloudAPI client
api = CrossChexCloudAPI(
    api_url="https://api.crosschexcloud.com",
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
    anviz_request_id="REQUEST_ID"
)

# Test connection and fetch token
token_info = api.test_connection()
print(token_info)

# Fetch attendance records for a specific date range
records = api.get_attendance_records(
    begin_time=datetime(2025, 10, 1, 0, 0, 0),
    end_time=datetime(2025, 10, 18, 23, 59, 59)
)
print(records)

# Access token and expiry
print("Token:", records["token"])
print("Expires:", records["expires"])
```

---

## Documentation

* **Token Management**: `get_token()`, `test_connection()`
* **Attendance Records**: `get_attendance_records()`, `get_attendance_payload()`
* **Internal Methods**: `_post()`, `_is_token_expired()`

---

## Dependencies

* `requests>=2.28.0`

---

## License

This project is licensed under the **LGPL 3.0** License.

---

## Author

**Sreethul Krishna**
Email: [sreethulkrishna24@gmail.com](mailto:sreethulkrishna24@gmail.com)

---

## Project Links

* [GitHub Repository](https://github.com/KSreethul/crosschexcloudapi)
* [Bug Tracker](https://github.com/KSreethul/crosschexcloudapi/issues)