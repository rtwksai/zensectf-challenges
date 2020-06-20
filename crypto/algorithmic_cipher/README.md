# Algorithmic Cipher

### Author: Hem_C

One idea to make strong cryptographic systems is to use NP-hard problems. Decryption without a key should require non-polynomial time and decryption with it should require polynomial time. Encryption of course should require polynomial time. The reason this is a good idea is because rather than us making up random encryption processes and hoping they can't be decrypted easily, we mathematically prove that it is really hard to do so and we make sure that the cipher is secure enough to not be crackable by brute force.

Meet Hemanth Chitti, a guy who thinks speaking of himself in the third person makes him cool. But anyways to the point, everybody keeps snooping into his phone to read his WhatsApp chats. So he's tired of it and decides to encrypt further messages.

But he's seen so many people fail by using standard ciphers, and he reasons that standard ciphers have standard vulnerabilities. So he decides to sit down and use the fact mentioned in the first paragraph.

He encrypts a message, ciphertext of which is found in the file attached.

Some trivia :

(i) The NP-hard problem this cipher is linked to is the subset sum problem.

(ii) The given list is a list of numbers. Each character of the flag is converted to decimal and is found somewhere in the list. To make things easier, I have inserted them in order. In other words a character that appears earlier in the flag will appear first in the list too i.e. assuming Python notation for indexing that indices are accessed with .index(), if there are two characters c1 and c2 in the flag with flag.index(c1) < flag.index(c2), then in the list too, list.index(c1) < list.index(c2).

(iii) A subset that sums up to this sum, 804, makes up the flag.

(iv) Only English lowercase letters, numbers and underscores have been used, and only English words are used.

zenseCTF{the decrypted plaintext} is the flag you need to submit.

Also, be mindful of recursion ;)

List is found in the below file:
