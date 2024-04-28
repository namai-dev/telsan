import telebot
from telebot import types
import requests


bot = telebot.TeleBot("6966100034:AAFllLNYAmKVbA3Wg3Na3Z7nv3yRbRkaONA", parse_mode=None)

def get_crypto_prices():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT")
    bnb_price = float(response.json()["price"])
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=TRXUSDT")
    trx_price = float(response.json()["price"])
    return bnb_price, trx_price


main_menu = types.ReplyKeyboardMarkup(row_width=1)
proxy = types.KeyboardButton("🛒 Buy Proxy")
rdp = types.KeyboardButton("🛒 Buy RDP")
driving_licence = types.KeyboardButton("🛒 Buy driving_licence")
passport = types.KeyboardButton("🛒 Buy passport")
check_balance = types.KeyboardButton("💰 Check Balance")
deposit = types.KeyboardButton("💳 Deposit")
main_menu.add(proxy, rdp, driving_licence, passport, check_balance, deposit, row_width=2)


proxy_data = {
    "usa": {"Proxies": ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "uk": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "netherlands": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "argentina": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "canada": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "kenya": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "nigeria": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "south_africa": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "philippines": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
    "indonesia": {"Proxies":  ["Information Only", "Photo Back&Front and information "], "Prices": ["$6", "$8"]},
}


# Define proxy locations menu
proxy_locations_menu = types.InlineKeyboardMarkup(row_width=2)
usa_location = types.InlineKeyboardButton("🇺🇸 USA", callback_data="usa")
uk_location = types.InlineKeyboardButton("🇬🇧 UK", callback_data="uk")
netherlands_location = types.InlineKeyboardButton("🇳🇱 Netherlands", callback_data="netherlands")
argentina_location = types.InlineKeyboardButton("🇦🇷 Argentina", callback_data="argentina")
canada_location = types.InlineKeyboardButton("🇨🇦 Canada", callback_data="canada")
kenya_location = types.InlineKeyboardButton("🇰🇪 Kenya", callback_data="kenya")
south_africa_location = types.InlineKeyboardButton("🇿🇦 South Africa", callback_data="south_africa")
philippines_location = types.InlineKeyboardButton("🇵🇭 Philippines", callback_data="philippines")
indonesia_location = types.InlineKeyboardButton("🇮🇩 Indonesia", callback_data="indonesia")
cancel_button = types.InlineKeyboardButton("❌ Cancel", callback_data="cancel")
proxy_locations_menu.add(usa_location, uk_location, netherlands_location, argentina_location, canada_location,kenya_location,  indonesia_location, philippines_location,south_africa_location, cancel_button,)


proxy_locations_menu1 = types.InlineKeyboardMarkup(row_width=2)
usa_location1 = types.InlineKeyboardButton("🇺🇸 USA", callback_data="usa1")
uk_location1 = types.InlineKeyboardButton("🇬🇧 UK", callback_data="uk1")
netherlands_location1 = types.InlineKeyboardButton("🇳🇱 Netherlands", callback_data="netherlands1")
argentina_location1 = types.InlineKeyboardButton("🇦🇷 Argentina", callback_data="argentina1")
canada_location1 = types.InlineKeyboardButton("🇨🇦 Canada", callback_data="canada1")
kenya_location1 = types.InlineKeyboardButton("🇰🇪 Kenya", callback_data="kenya1")
south_africa_location1 = types.InlineKeyboardButton("🇿🇦 South Africa", callback_data="south_africa1")
philippines_location1 = types.InlineKeyboardButton("🇵🇭 Philippines", callback_data="philippines1")
indonesia_location1 = types.InlineKeyboardButton("🇮🇩 Indonesia", callback_data="indonesia1")
cancel_button1 = types.InlineKeyboardButton("❌ Cancel", callback_data="cancel")
proxy_locations_menu1.add(usa_location1, uk_location1, netherlands_location1, argentina_location1, canada_location1,kenya_location1,  indonesia_location1, philippines_location1,south_africa_location1, cancel_button1)




@bot.message_handler(commands=["start"])
def send_menu(message):
   
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=main_menu)

@bot.message_handler(func=lambda message: message.text == "💳 Deposit")
def handle_deposit(message):
    bot.send_message(message.chat.id, "Please enter the deposit amount (minimum 10 USDT equivalence):", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, process_deposit_amount)

def process_deposit_amount(message):
    try:
        deposit_amount = float(message.text)
        if deposit_amount < 10:
            bot.send_message(message.chat.id, "Deposit amount must be at least 10 USDT equivalence. Please try again.", reply_markup=main_menu)
            return
        else:
            bnb_price, trx_price = get_crypto_prices()
            bnb_equivalence = deposit_amount / bnb_price
            trx_equivalence = deposit_amount / trx_price
            deposit_options = (
                "Deposit Options:\n\n"
                "1. **BNB** (Equivalent to {:.2f} BNB): \n   `0x2d03790fD0F67F27aBf30c6fDd69279Aa597B5C4`\n"
                "2. **USDT (TRC)**: \n   `TB6mHA7XZ9qm6xfnKhpiPevRhH1NUde3f7`\n"
                "3. **TRX (TRON)** (Equivalent to {:.2f} TRX): \n   `TB6mHA7XZ9qm6xfnKhpiPevRhH1NUde3f7`\n\n"
                "Please proceed with the deposit.\n\n"
                "_We are waiting for the deposit to arrive._"
            ).format(bnb_equivalence, trx_equivalence)
            bot.send_message(message.chat.id, deposit_options, reply_markup=main_menu)
    except ValueError:
        bot.send_message(message.chat.id, "Invalid input. Please enter a valid numeric amount.", reply_markup=main_menu)



@bot.message_handler(func=lambda message: message.text == "🛒 Buy Proxy")
def handle_buy_proxy(message):
    bot.send_message(message.chat.id, "Select a location:", reply_markup=proxy_locations_menu1)


@bot.message_handler(func=lambda message: message.text == "🛒 Buy RDP")
def handle_buy_rdp(message):
    bot.send_message(message.chat.id, "Select a location:", reply_markup=proxy_locations_menu1)


@bot.message_handler(func=lambda message: message.text == "🛒 Buy passport")
def handle_buy_passport(message):
    bot.send_message(message.chat.id, "Select a location:", reply_markup=proxy_locations_menu)





@bot.message_handler(func=lambda message: message.text == "🛒 Buy driving_licence")
def handle_buy_dl(message):
    bot.send_message(message.chat.id, "Select a location:", reply_markup=proxy_locations_menu)

# Function to handle checking balance
@bot.message_handler(func=lambda message: message.text == "💰 Check Balance")
def handle_check_balance(message):
    balance_text = f"Your balance is 0 USDT"
    options_menu = types.InlineKeyboardMarkup(row_width=1)
    options_menu.add(
        types.InlineKeyboardButton("Request Withdrawal", callback_data="request_withdrawal"),
        types.InlineKeyboardButton("Deposit hasn't arrived", callback_data="deposit_not_arrived"),
        types.InlineKeyboardButton("Contact Customer Support", callback_data="contact_support")
    )
    bot.send_message(message.chat.id, balance_text, reply_markup=options_menu)

import time

# Dictionary to store user states
user_states = {}

# Function to handle checking balance
@bot.message_handler(func=lambda message: message.text == "💰 Check Balance")
def handle_check_balance(message):
    balance_text = f"Your balance is 0 USDT"
    options_menu = types.InlineKeyboardMarkup(row_width=1)
    options_menu.add(
        types.InlineKeyboardButton("Request Withdrawal", callback_data="request_withdrawal"),
        types.InlineKeyboardButton("Deposit hasn't arrived", callback_data="deposit_not_arrived"),
        types.InlineKeyboardButton("Contact Customer Support", callback_data="contact_support")
    )
    bot.send_message(message.chat.id, balance_text, reply_markup=options_menu)

# Callback function to handle inline button options
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_options(call):
    if call.data == "request_withdrawal":
        # Check if balance is zero
        if 0 == 0:
            bot.send_message(call.message.chat.id, "Your balance is zero. Unable to process withdrawal.")
        else:
            # Process withdrawal
            bot.send_message(call.message.chat.id, "Withdrawal request processed. Funds will be transferred shortly.")
            user_states[call.message.chat.id] = "withdrawal_done"
            # Wait for a few minutes before sending the next message
            time.sleep(10)
            bot.send_message(call.message.chat.id, "Returning to main menu...", reply_markup=main_menu)
    elif call.data == "deposit_not_arrived":
        # Provide transaction hash for deposit
        transaction_hash = "Your transaction hash goes here"  # Replace with actual transaction hash
        bot.send_message(call.message.chat.id, f"Your deposit transaction hash: {transaction_hash}")
        user_states[call.message.chat.id] = "transaction_hash_provided"
        # Wait for a few minutes before sending the next message
        time.sleep(10)
        bot.send_message(call.message.chat.id, "Returning to main menu...", reply_markup=main_menu)
    elif call.data == "contact_support":
        # Prompt user to provide issue details and email
        bot.send_message(call.message.chat.id, "Please provide details of your issue and your email address.")
        user_states[call.message.chat.id] = "issue_provided"
        # Wait for a few minutes before sending the next message
        time.sleep(120)
        bot.send_message(call.message.chat.id, "Coming back to you after a few minutes. Check your email.", reply_markup=main_menu)
        # Clear user state after completing the process
        user_states.pop(call.message.chat.id, None)
    else:
        location_data = proxy_data.get(call.data)
        if location_data:
            proxies = location_data["Proxies"]
            prices = location_data["Prices"]
            proxy_menu = types.InlineKeyboardMarkup(row_width=1)
            for proxy, price in zip(proxies, prices):
                # Create a button for each proxy with its price
                proxy_button = types.InlineKeyboardButton(f"{proxy}: {price}", callback_data=f"proxy_{proxy}_{price}")
                proxy_menu.add(proxy_button)
            bot.send_message(call.message.chat.id, "Available info/pics and their prices in {}:".format(call.data.upper()), reply_markup=proxy_menu)
        else:
            bot.send_message(call.message.chat.id, "Invalid location selected.", reply_markup=main_menu)

# Function to handle user messages
@bot.message_handler(func=lambda message: True)
def handle_user_messages(message):
    # Check if the user is in a specific state
    if message.chat.id in user_states:
        if user_states[message.chat.id] == "transaction_hash_provided":
            bot.send_message(message.chat.id, "Working. Please wait a few minutes...")
            user_states[message.chat.id] = "waiting_for_issue"
        elif user_states[message.chat.id] == "issue_provided":
            bot.send_message(message.chat.id, "Coming back to you after a few minutes. Check your email.")
            # Clear user state after completing the process
            user_states.pop(message.chat.id, None)





# Function to handle checking balance
@bot.message_handler(func=lambda message: message.text == "💰 Check Balance")
def handle_check_balance(message):
    balance_text = f"Your balance is 0 USDT"
    options_menu = types.InlineKeyboardMarkup(row_width=1)
    options_menu.add(
        types.InlineKeyboardButton("Request Withdrawal", callback_data="request_withdrawal"),
        types.InlineKeyboardButton("Deposit hasn't arrived", callback_data="deposit_not_arrived"),
        types.InlineKeyboardButton("Contact Customer Support", callback_data="contact_support")
    )
    bot.send_message(message.chat.id, balance_text, reply_markup=options_menu)

# Callback function to handle inline button options
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_options(call):
    if call.data == "request_withdrawal":
        # Check if balance is zero
        if 0 == 0:
            bot.send_message(call.message.chat.id, "Your balance is zero. Unable to process withdrawal.")
        else:
            # Process withdrawal
            bot.send_message(call.message.chat.id, "Withdrawal request processed. Funds will be transferred shortly.")
        # Return to main menu
        bot.send_message(call.message.chat.id, "Returning to main menu...", reply_markup=main_menu)
    elif call.data == "deposit_not_arrived":
        # Provide transaction hash for deposit
        transaction_hash = "Your transaction hash goes here"  # Replace with actual transaction hash
        bot.send_message(call.message.chat.id, f"Your deposit transaction hash: {transaction_hash}")
        # Return to main menu
        bot.send_message(call.message.chat.id, "Returning to main menu...", reply_markup=main_menu)
    elif call.data == "contact_support":
        # Prompt user to provide issue details and email
        bot.send_message(call.message.chat.id, "Please provide details of your issue and your email address.")
        # Return to main menu
        bot.send_message(call.message.chat.id, "Returning to main menu...", reply_markup=main_menu)




@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🛒 Buy Proxy":
        bot.reply_to(message, "You selected 'Buy Proxy'")
    elif message.text == "🛒 Buy RDP":
        bot.reply_to(message, "You selected 'Buy RDP'")
    elif message.text == "🛒 Buy driving_licence":
        bot.reply_to(message, "You selected 'Buy Licence")
    elif message.text == "🛒 Buy passport":
        bot.reply_to(message, "You selected 'Buy passport")
    elif message.text == "💳 Deposit":
        bot.reply_to(message, "To deposit funds, send your desired amount to our wallet address.")
    elif message.text == "💰 Check Balance":
        bot.reply_to(message, "Your balance is $1000")
    

bot.infinity_polling()
