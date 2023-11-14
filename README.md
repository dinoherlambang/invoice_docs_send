# Invoices Move Module

This module inhereit the `account.move` model in Odoo. The main function of this module is to record the physical invoice document recieval. It adds a feature that restricts the `docs_status` field from being changed to "Recieved" unless both `recieve_by` and `photo` fields are provided. This ensures that the physical invoice document has been received and a photo of the document has been attached before the document status can be updated to "Recieved".

## Features

- Adds a `docs_status` field with options "Sent" and "Recieved".
- Adds a `recieve_by` field to specify who received the document.
- Adds a `photo` field to attach a photo of the document.
- Overrides the `write` method to check `recieve_by` and `photo` fields before changing `docs_status` to "Recieved".

## Usage

When you try to change the `docs_status` to "Recieved", the system will check if the `recieve_by` and `photo` fields are filled out. If either of these fields is empty, you will see an error message: "Fill 'Recieve By' and 'Photo' to set status as 'Received'."

Please note that you need to test this code thoroughly before deploying it in a production environment.

## Modules Depends

- base
- account

## Installation

To install this module, you need to:

1. Download or clone this repository.
2. Place the module in your Odoo addons directory.
3. Update the module list in your Odoo instance.
4. Install the module.

