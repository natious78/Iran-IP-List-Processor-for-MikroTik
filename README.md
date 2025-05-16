# Iran IP List Processor

This Python script downloads a MikroTik RouterOS script file containing Iranian IP address ranges, processes it, and generates a simplified list of firewall address list entries for use in RouterOS.

## 📌 What It Does

- Fetches data from:
  ```
  https://raw.githubusercontent.com/MrAriaNet/Get-IP-Iran/main/list.rsc
  ```
- Saves the output as a plain text file: `iran_ip_list.txt`.

## 🛠️ Requirements

- Python 3.6+
- `requests` library

You can install the required package using:

```bash
pip install requests
```

## 🚀 How to Use

1. Clone this repository:


2. Run the script:

```bash
python getIranIpsForMicrotik.py
```

3. The result will be saved in:

```
iran_ip_list.txt
```


## 📂 Output Example


It will be  :

```
/ip firewall address-list
add address=2.57.3.0/24 list=Iran
.
.
.
```
