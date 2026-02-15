# 🍕 ربات تلگرام سفارش پیتزا

یک ربات تلگرام ساده برای سفارش‌گیری پیتزا با پایتون

## ویژگی‌ها

✅ منوی تعاملی با دکمه‌های فارسی
✅ مدیریت سبد خرید
✅ محاسبه خودکار قیمت
✅ ارسال رایگان برای خریدهای بالای ۳۰۰ هزار تومان

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8+
- توکن ربات تلگرام (از @BotFather)

### مراحل نصب

1. کلون کردن پروژه:
```bash
git clone https://github.com/YOUR_USERNAME/telegram-pizza-bot.git
cd telegram-pizza-bot
```

2. ساخت محیط مجازی:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. تنظیم توکن:
```bash
# کپی کردن فایل نمونه
copy config_example.py config.py

# ویرایش config.py و گذاشتن توکن واقعی
```

5. اجرای ربات:
```bash
python bot.py
```

## استفاده

1. ربات خود را در تلگرام پیدا کنید
2. دستور `/start` را بفرستید
3. از منو پیتزای مورد نظر را انتخاب کنید
4. سبد خرید را مشاهده و تایید کنید

## تکنولوژی‌ها

- Python 3.8+
- python-telegram-bot 20.7
- Telegram Bot API

## نویسنده

**نام شما**

- Telegram: @Lord_V
- GitHub: [@saeed-agent47](https://github.com/saeed-agent47)

## مجوز

MIT License

---

ساخته شده با ❤️ برای یادگیری