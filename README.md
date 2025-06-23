# Ping Sweeper

**Ping Sweeper** is a simple multithreaded Python script that performs a ping sweep over a `/24` subnet to detect active hosts. It is cross-platform and automatically adapts the `ping` command based on your operating system (Windows or Unix-based).

---

## 🚀 Features

- Multithreaded for fast scanning
- Cross-platform support (Windows and Linux/macOS)
- Suppresses terminal clutter by hiding ping output
- Detects and prints active hosts only

---

## 🛠️ Requirements

- Python 3.x
- Works on:
  - Windows
  - Linux
  - macOS

---

## 📄 Example Usage

```bash
python ping-sweeper.py 192.168.1.0

NOTE: Use the network address of the subnet to get the correct result.