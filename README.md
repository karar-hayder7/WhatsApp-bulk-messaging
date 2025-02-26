# WhatsApp-bulk-messaging
![whatsapp daigram](https://github.com/user-attachments/assets/d3b9b45c-b6f2-46e7-8098-8f737de66839)

# WhatsApp Bulk Messaging Script

This Python script automates sending personalized WhatsApp messages using the `pywhatkit` library. It reads phone numbers and names from an Excel file and formats a message from a text file before sending it to each recipient.

## Features
- Reads contact details from an Excel file (`list.xlsx`).
- Loads a pre-written message from `message.txt`.
- Sends personalized messages to multiple recipients instantly via WhatsApp Web.
- Saves a record of every message sent in a file called `PyWhatKit_DB`.
- Adds delays to prevent being flagged as spam.

## Prerequisites
Ensure you have the following installed before running the script:
- Python 3.11.9 or later
- Required Python packages:
  ```sh
  pip install pywhatkit pandas openpyxl
  ```
- Google Chrome or any web browser with an active WhatsApp Web session

## Preparing the Files
1. **Prepare the Contact List:**
   - Create an Excel file (`list.xlsx`) with at least two columns:
     - `Phone number` (including country code, e.g., `971XXXXXXXXX` for UAE numbers)
     -     ✅ Correct: 971XXXXXXXXX
           ❌ Incorrect: +971XXXXXXXXX
     - {name} (Recipient's name)

   - Ensure the file is saved after editing.

2. **Prepare the Message Template:**
   - Create a `message.txt` file with a message template. You can use `{name}` as a placeholder for dynamic names.
     ```
     Hello {name},
     This is a test message from our automated WhatsApp sender.
     ```
   - Save the file after editing.

## Running the Script
1. Open WhatsApp Web on any web browser and ensure it is logged in.
2. Run the script:
   ```sh
   python main.py
   ```
3. The script will:
   - Read the contact list from `list.xlsx`.
   - Load the message from `message.txt`.
   - Replace `{name}` in the message with the recipient's actual name.
   - Send the message via WhatsApp Web.
   - Save a record of every message sent in `PyWhatKit_DB`.

## Notes
- WhatsApp Web must remain open during execution.
- Each message waits 10 seconds before sending to avoid spam detection.
- The script automatically closes WhatsApp Web after sending the message.
- If you experience issues, ensure your WhatsApp Web session is active.


   ```




