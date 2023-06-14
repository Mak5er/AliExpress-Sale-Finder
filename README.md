## Project description

This project is a Telegram bot that parses the AliExpress website, searches for cheap products and sends them to the user. The bot has a smear filter to filter out unhelpful ads. The bot is implemented using the Python programming language and the Telebot framework for interacting with the Telegram API.

## Usage.

    /start: Start interaction with the bot and receive a welcome message.
    /admin: Access to the admin panel (only allowed to the administrator).
    /info: Get information about the user and statistics of bot usage.

## Functionality

### Regular user

    Get new found products or view all products from the database. View bot statistics.

### Administrator
  
    Add a new product, mark a product as spam, delete a product.
    Start parsing, send a message to all users on behalf of the bot.

## Database

The bot uses a SQLite database with the following tables:

    items - Stores information about the product.
    send_items - Stores the item and to whom it was sent to the user.
    spam_id - Stores the spam ids of the items.
    users - Stored users.
