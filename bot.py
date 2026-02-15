# bot.py
"""
ربات تلگرام سفارش پیتزا
"""

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, MENU, MESSAGES, DELIVERY_FEE, FREE_DELIVERY_THRESHOLD


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """شروع ربات و نمایش منو"""

    # ساخت دکمه‌های منو
    keyboard = []
    for item, price in MENU.items():
        button_text = f'{item} - {price:,} تومان'
        keyboard.append([button_text])

    # دکمه‌های اضافی
    keyboard.append(['📋 مشاهده سفارش', '🗑 پاک کردن سبد'])
    keyboard.append(['✅ تایید و ارسال'])

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        MESSAGES['welcome'],
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """مدیریت پیام‌های کاربر"""

    text = update.message.text

    # چک کن آیا پیتزا انتخاب شده؟
    for item, price in MENU.items():
        if item in text:
            # اگه سبد خرید نداره، بساز
            if 'order' not in context.user_data:
                context.user_data['order'] = []

            # اضافه کن به سبد
            context.user_data['order'].append(item)

            await update.message.reply_text(
                MESSAGES['added'].format(item=item, price=price)
            )
            return

    # مشاهده سبد خرید
    if '📋' in text:
        await show_cart(update, context)

    # پاک کردن سبد
    elif '🗑' in text:
        context.user_data['order'] = []
        await update.message.reply_text(MESSAGES['order_cleared'])

    # تایید سفارش
    elif '✅' in text:
        await confirm_order(update, context)


async def show_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """نمایش سبد خرید"""

    # چک کن سبد خرید داره یا نه
    if 'order' not in context.user_data or not context.user_data['order']:
        await update.message.reply_text(MESSAGES['empty_cart'])
        return

    # محاسبه قیمت‌ها
    order_items = context.user_data['order']
    order_text = '🛒 سبد خرید شما:\n\n'
    subtotal = 0

    for item in order_items:
        price = MENU[item]
        subtotal += price
        order_text += f'• {item}: {price:,} تومان\n'

    # محاسبه هزینه ارسال
    if subtotal >= FREE_DELIVERY_THRESHOLD:
        delivery = 0
    else:
        delivery = DELIVERY_FEE

    total = subtotal + delivery

    # اضافه کردن جمع کل
    order_text += f'\n📦 جمع جزء: {subtotal:,} تومان\n'
    order_text += f'🚚 هزینه ارسال: {delivery:,} تومان\n'
    order_text += f'💰 جمع کل: {total:,} تومان'

    if delivery == 0:
        order_text += '\n\n🎉 ارسال رایگان!'

    await update.message.reply_text(order_text)


async def confirm_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تایید نهایی سفارش"""

    if 'order' not in context.user_data or not context.user_data['order']:
        await update.message.reply_text('سبد خرید خالی است!')
        return

    # پیام تایید
    await update.message.reply_text(
        '✅ سفارش شما ثبت شد!\n\n'
        '⏰ زمان تحویل: ۳۰-۴۵ دقیقه\n'
        '📞 پشتیبانی: @YourSupport\n\n'
        'ممنون از خرید شما! 🙏'
    )

    # پاک کردن سبد
    context.user_data['order'] = []


def main():
    """اجرای ربات"""

    print("🤖 در حال راه‌اندازی ربات...")

    # ساخت Application
    app = Application.builder().token(BOT_TOKEN).build()

    # اضافه کردن handler ها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ ربات آماده است!")
    print("🔄 در حال دریافت پیام‌ها...")

    # شروع polling
    app.run_polling()


if __name__ == '__main__':
    main()