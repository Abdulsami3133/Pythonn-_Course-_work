portfolio = {
    "user_name": "Sami",
    "user_id": 101,                         # int
    "account_balance": 50000.75,            # float
    "kyc_verified": True,                   # bool

    "stocks": [                              # list
        {
            "symbol": "TCS",                # string
            "quantity": 10,                 # int
            "price": 3500.50               # float
        },
        {
            "symbol": "INFY",
            "quantity": 15,
            "price": 1800.25
        }
    ],

    "market_range": (20000, 25000),         # tuple

    "sectors": {                             # set
        "IT",
        "Banking",
        "Technology"
    }
}

print(portfolio)
