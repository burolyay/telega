from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton

mars_menu = ReplyKeyboardMarkup(
    [
    [
        KeyboardButton("Профиль"),
        KeyboardButton("Мои монеты"),
        KeyboardButton("Space shop"),
    ],
    [
        KeyboardButton("О школе"),
        KeyboardButton("Оставить отзыв")
        
    ]
    ]
)
mars_shop_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Mouse", callback_data="1"),
            InlineKeyboardButton(text="Mars sticker", callback_data="2"),
           
        ],
        [
            InlineKeyboardButton(text="Keyboard", callback_data="3"),
            InlineKeyboardButton(text="Strobar", callback_data="4"),
        ],
        [
            InlineKeyboardButton(text="Usb Fleshka", callback_data="5"),
            InlineKeyboardButton(text="Mars chocolate", callback_data="6"),
        ],
                [
            InlineKeyboardButton(text="Mars mini", callback_data="7"),

        ]
    ]
)
mars_profile_inline = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Имя", callback_data="1"),
            InlineKeyboardButton(text="Фамилия", callback_data="2"),
           
        ],
        [
            InlineKeyboardButton(text="Язык", callback_data="3"),
            InlineKeyboardButton(text="Телефон", callback_data="4"),
        ],
     
        [
            InlineKeyboardButton(text="Город", callback_data="7"),

        ]
    ]
)