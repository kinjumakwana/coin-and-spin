from django.test import TestCase
# Create your tests here.
import re
import emoji
import demoji

# text with emojis
text = "EGG-citing news Bunnies🐰😍: a JOKER CARD could be YOURS in our Trading Group! 🎴🎉 Hop on over for a chance to win ➡️ https://coin-master.me/joker-card-easter 🥳️"
encode_text = text.encode('utf-8')
print(encode_text)

# decode_text = encode_text.decode('utf-8')
# print('decode_text',decode_text)

text_no_emoji = emoji.demojize(text)
print("Text without emojis: ", text_no_emoji)

# Remove the URL from the text using regular expressions
text = re.sub(r'https?://\S+', '', text)

# Remove any leading or trailing white space
text = text.strip()

print(text)