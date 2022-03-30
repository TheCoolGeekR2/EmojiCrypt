# Emoji Crypt
## What is it do?
This encrypts a file using emojis.
## How does it work?
Emojis entered are converted into their full Emoji names.

**For Example:**
> 😀 -> grining_face

Then we take the output from that conversion, turn it into a SHA256 hash and with it generate a symetric encryption key to encrypt our file.

To decrypt we do the same thing and just use the key to decrypt the file.
