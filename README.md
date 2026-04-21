# 🚀 crosschexcloudapi – Python SDK for Anviz CrossChex Cloud

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-LGPL--3.0-green)](https://www.gnu.org/licenses/lgpl-3.0.html)
![PyPI Downloads](https://img.shields.io/pypi/dm/crosschexcloudapi)
![GitHub stars](https://img.shields.io/github/stars/KSreethul/crosschexcloudapi)

Tired of dealing with complex CrossChex Cloud API authentication and pagination?

**crosschexcloudapi** is a clean Python SDK that simplifies working with the Anviz CrossChex Cloud API.

✔ Automatic token management
✔ Built-in pagination handling
✔ Clean and structured responses
✔ Minimal setup, production-ready

Perfect for **HRMS, attendance sync systems, and cloud integrations**.

---

## ⚡ Quick Start

```python
from crosschexcloudapi import CrossChexCloudAPI

api = CrossChexCloudAPI(
    api_url="https://api.crosschexcloud.com",
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
    anviz_request_id="REQUEST_ID"
)

# Fetch attendance records
records = api.get_attendance_records()
print(records)
```

---

## 📦 Installation

```bash
pip install crosschexcloudapi
```

---

## ❓ Why This Library?

Working directly with CrossChex Cloud API involves:

* Token expiration handling
* Complex payload structure
* Manual pagination
* Repeated authentication calls

**This library solves it by:**

* 🔐 Automatically generating & refreshing tokens
* 🔁 Handling expired tokens internally
* 📄 Managing pagination transparently
* ⚙️ Providing simple Python methods
* 🧠 Reducing API complexity drastically

---

## ✨ Features

* 🔐 Automatic token generation & renewal
* 📊 Fetch attendance logs with pagination support
* ⏱ ISO timestamp handling
* 🔁 Retry on token expiration
* 📦 Clean structured response format
* ⚡ Lightweight (`requests` only)

---

## 🛠 Real-World Use Cases

* Sync attendance data to HRMS
* Build payroll automation pipelines
* Integrate Anviz devices into SaaS platforms
* Centralize biometric data from multiple locations

---

## 📄 Usage Examples

### 🔑 Test connection & get token

```python
token_info = api.test_connection()
print(token_info)
```

---

### 📊 Fetch attendance records (date range)

```python
from datetime import datetime

records = api.get_attendance_records(
    begin_time=datetime(2025, 10, 1, 0, 0, 0),
    end_time=datetime(2025, 10, 18, 23, 59, 59)
)

print(records)
```

---

### 📦 Example Response

```json
{
  "token": "abc123",
  "expires": "2025-10-20T10:00:00",
  "count": 2,
  "list": [
    {
      "employee_id": "E1001",
      "check_time": "2025-10-18T09:00:00",
      "type": "checkin"
    }
  ]
}
```

---

## 🧠 How It Works (Under the Hood)

* Generates token using API key & secret
* Stores token + expiry internally
* Auto-refreshes token when expired
* Fetches paginated data until complete
* Returns a single merged dataset

No manual handling needed.

---

## 📚 API Overview

### 🔐 Authentication

* `get_token()`
* `test_connection()`

### 📊 Attendance

* `get_attendance_records()`
* `get_attendance_payload()`

### ⚙️ Internal Helpers

* `_post()`
* `_is_token_expired()`

---

## ⚠️ Requirements

* Python 3.10+
* `requests>=2.28.0`

---

## 🚧 Roadmap

* [ ] Async support
* [ ] Webhook support
* [ ] Filtering helpers
* [ ] Better error handling

---

## 🤝 Contributing

Contributions are welcome!

### Steps:

1. Fork the repository
2. Create a branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

---

## 📄 License

Licensed under **LGPL-3.0**
👉 [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)

---

## 🔗 Links

* GitHub: [https://github.com/KSreethul/crosschexcloudapi](https://github.com/KSreethul/crosschexcloudapi)
* Issues: [https://github.com/KSreethul/crosschexcloudapi/issues](https://github.com/KSreethul/crosschexcloudapi/issues)

---

## ⭐ Support

If this project helps you:

* ⭐ Star the repo
* 🐛 Report issues
* 🔁 Share with others

---

## 🎯 Final Note

If you're integrating **Anviz CrossChex Cloud with your backend**,
this library removes 80% of the complexity.

Build faster. Integrate smarter.
