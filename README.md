# 📦 Smart Storage Box Manager (QR Code Linked)

A simple Flask web app for organizing physical storage boxes using QR codes. Each QR code links to a web interface where you can describe the contents of a box, set the date and time it was packed, and keep everything searchable and organized.

## ✨ Features

- Generate a unique page per box (e.g. `/box/box001`)
- Add/edit:
  - Description
  - Date and time
  - List of contents
- Mobile-friendly dark-themed UI
- Automatically readable from QR codes
- Local file-based storage (no database required)
- Easy to deploy on Replit, Render, VPS, or Orange Pi

## 📸 Use Case

1. Print a QR code linking to `/box/box001`, tape it to your physical box.
2. Scan the QR code with your phone.
3. Add a description, date/time, and contents of the box.
4. Done! Next time you scan the QR code, you’ll see exactly what’s inside.

## 🚀 Getting Started

### Requirements

- Python 3.x
- Flask

### Installation

```bash
git clone https://github.com/opencream/qrcode.git
cd box-organizer
pip install -r requirements.txt
python main.py
