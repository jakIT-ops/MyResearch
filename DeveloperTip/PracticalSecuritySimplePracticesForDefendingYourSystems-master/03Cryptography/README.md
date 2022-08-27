# 1. Don’t Roll Your Own Crypto


## Bugs in the crypto can have a huge impact

Writing cryptography software isn’t like writing regular software. When writing regular software, little bugs tend to have little impacts. If you have an off-by-one bug, you could expect a small bug, for example, omitting one result on a search page. If you forget to check for null references, maybe a program crashes. But with cryptography, a small mistake may leave you with a system that encrypts and decrypts correctly for well-intentioned inputs but fails entirely when faced with malicious input.

The developer needs to either rediscover the entire field from scratch or subject the code to the scrutiny of others with a deep understanding of the field. Just as you can’t tickle yourself, you can’t find the mistakes you’ve made that involve flaws you haven’t learned about yet. Bruce Schneier has a nice essay on Schneier’s Law that expands on this.

## Attack models

There are many different attack models to consider. A common, though misguided, mental model of a secure cryptosystem is one where the attacker gets to see a single message of modest length. If the attacker can decrypt it, then the system is insecure; otherwise, it’s suitable for any and all purposes. That certainly is an attack that a cryptosystem should be able to defend against. But there are many other models to consider, such as the following:

* An attacker who can listen to many encrypted messages between two parties

* An attacker who can replay previously transmitted encrypted messages

* An attacker who can replay modified variants of previously transmitted encrypted messages

* An attacker who can replay modified variants of previously transmitted encrypted messages to a recipient who’s expecting only well-behaved communication and who therefore displays helpful error messages if anything goes wrong during decryption

* An attacker who can listen to the encrypted communication between two parties where some of the plaintexts are known to the attacker

* An attacker who can influence the contents of encrypted communication between two other parties

## Issues with rolling your own crypto

It’s easy to see all of the security breaches in the news and decide to protect ourselves by building a new kind of encryption. That’s a laudable goal, but it’s misguided. Without a deep understanding of how systems have been compromised, it’s unlikely that someone would be able to design a safer system from first principles. Better to reign in that desire to build a new cryptosystem until you have broken a couple yourself. If you haven’t broken anything yet, you are likely to just repeat other people’s mistakes from the past. As the saying goes,

# 2. Security When the Enemy Knows the System

## The key is key

The key is key. Encryption algorithms don’t just take plain text as input, they take a key as well. A well-written encryption algorithm will produce wildly different outputs when encrypting a given plaintext with keys that differ only slightly. The key is the only part that needs to be kept secret. Rather than keeping an entire algorithm secret, we just need to keep our key secret.

An encryption algorithm should be so strong that even if an attacker had full access to the source code, the attacker would have no better option than to brute force all possible passwords. We won’t cover how the encryption libraries recommended in this chapter achieve this goal. We’ll merely note that they’ve been found to do so.

### What’s so great about a deck of playing cards?

I have to turn your attention to one of the most fun bits of math I’ve ever read. It’s a great way to help visualize just how many different ways you can order a standard deck of playing cards. When you order a deck, there are 52 possibilities for the first card. You pick the first one, and that leaves 51 possibilities for the second card, 50 for the third card, and so on. That makes for 52 \times 51 \times 50 \times ... \times 4 \times 3 \times 2 \times 1
52×51×50×...×4×3×2×1
 different possibilities. The shorthand for this is 52!
52!
 (pronounced “52 factorial”) and it’s so big, that, well, just read the linked story. It’s fun.

# 3. Don’t Use Low-Level Crypto Libraries

Hopefully, we’re now in agreement that we shouldn’t roll our own crypto. It might seem that all we need to do is grab a low-level encryption library and start using it’s AES encryption and decryption functions. After all, that’s not “rolling our own crypto.”

## Low-level libraries are easy to misconfigure

For example, many low-level cryptography libraries provide support for outdated algorithms like MD5 and 3DES. And oftentimes comparisons of libraries such as Wikipedia’s show supported algorithms in a way makes it seem as though libraries with support for more algorithms are fuller featured.

Low-level libraries don’t provide guidance; instead, they force the developer to know which algorithms are safe to use. Even if the developer knows to choose a strong encryption algorithm like AES, low-level cryptography libraries still provide dangerous configuration choices. These choices include things like block mode and key size. Getting these choices wrong can result in a system that’s insecure. In contrast, a high-level encryption library is opinionated and makes these configuration choices for the developer. This makes a high-level encryption library misuse-resistant.

## AES and the ECB penguin

Have there ever been three letters that give such a feeling of safety? AES, or the Advanced Encryption Standard, has a strong pedigree. Initially called Rijndael, after its creators, Vincent Rijmen and Joan Daemen, it earned the name AES after being named the finalist in the National Institute of Standards and Technology (NIST) selection process. This selection process took several years and pitted fifteen competing algorithms against each other. During that process and after its selection, the AES algorithm has withstood tremendous scrutiny from a tremendous number of talented cryptographers.

## Pitfalls of AES

But it’s really easy to misuse.

AES is a block cipher. Probably the easiest way to misuse AES is to pick the wrong block mode.

## ECB mode

We’ll start with ECB because it’s the simplest block mode and is the default block mode in many libraries. In ECB mode, the first block of plaintext is encrypted by itself. Then the next block of plaintext is encrypted by itself, and so on. A padding operation is used to add on data so that the final block is also a full block. The ciphertext is just the concatenation of encrypting each block of the plaintext individually. It’s the straightforward approach you’d first think of when thinking about how to apply an operation that works on a fixed-size block to plaintext of arbitrary length.

# 4. Evaluating Crypto Libraries Without Being a Crypto Expert

But how do we know experts when we see them? Evaluating people based on skills we don’t have ourselves is a tough problem with no great solution. We encounter it in other parts of our life. How do we evaluate doctors, mechanics, lawyers, plumbers, and other specialists with skills we don’t have? We tend to use a few techniques. We can look for professionals with certifications. Sometimes we can look for professionals who have written helpful books, articles, or blog posts. We ask our friends or look to the wisdom of crowds and check ratings online.

When we apply any of these, we find folks like Bernstein and Lange (authors of NaCl) and Bleichenbacher and Duong (authors of Tink) pass with flying colors. But since we’re in cryptography, we have one more technique we can bring to bear. When we evaluate a library, we can look at the track record of its authors. What have they broken? What have they built and how has that held up to scrutiny? Add this metric, and you’ll find Bernstein, Lange, Bleichenbacher, and Duong have about as impressive a trophy case as you’re going to find.

## Track record of reputable libraries

So what have the authors of these libraries done that should inspire confidence?

### Bernstein and Lange

Bernstein and Lange are accomplished academics with a strong body of work. In addition, their work on NaCl has stood up to widespread scrutiny for many years. NaCl uses Bernstein’s Salsa20 cipher extensively. Bernstein’s related ChaCha20 cipher has been used by Google for securing TLS communication since 2014, which is a nice compliment on the strength of ChaCha20. Additionally, Bernstein’s earlier work on programs such as djbdns and qmail has also stood up to widespread usage and scrutiny for many years.

### Bleichenbacher

Daniel Bleichenbacher is most famous for the “Bleichenbacher attack” against RSA. He first described this attack in 1998. His attack allows for decrypting RSA encryption without direct access to the decryption key. Twenty years later, this attack is still relevant. It was the inspiration for Hanno Böck, Juraj Somorovsky, and Craig Young’s ROBOT (Return Of Bleichenbacher’s Oracle Threat) attack. The ROBOT attack even won the 2018 Pwnie Award for Best Cryptographic Attack.

### Duong

Thai Duong co-discovered the BEAST, CRIME, and POODLE vulnerabilities in SSL/TLS. The BEAST attack, discovered by Duong and Rizzo, allows an eavesdropper to decrypt TLS 1.0 communication. Its discovery was a major factor in the adoption of the TLS 1.1 standard. The CRIME attack, also discovered by Duong and Rizzo, leverages HTTP compression to decrypt HTTPS traffic to steal cookies and hijack sessions. Finally, we have the POODLE attack, discovered by Bodo Möller, Thai Duong, and Krzysztof Kotowicz. POODLE allows a man-in-the-middle attack during the TLS handshake that allows the attacker to downgrade what would have been a TLS connection between a browser and a server to a much weaker SSL 3.0 connection.

# 5. Password Storage

## On storing (and not storing) Your users’ passwords

Instead of storing a user password, we can store a value that’s derived from the password itself. If this derivation can only be performed in one direction (that is, it’s easy to calculate the derived value given a password but it’s hard to go from a derived value back to the original password), then we’ll have a great defense. When a user creates an account for themselves, they’ll enter a password and we won’t store the password itself, we’ll only store the derived value. Next time the user logs in, they’ll type in their password, we’ll perform that same derivation and compare it to the previously stored derived value. If the two derived values match, we know the user typed in the right password. If they don’t match, we know the user typed in the wrong password.

## Store passwords in the clear

Initially, passwords were just stored in the clear on the server. The thinking was that an attacker who got as far as being able to read from the database had already “won,” so why bother doing anything else? You can see evidence of this having been a trend if you think back to websites in the 1990s and early 2000s. It was common practice at the time for websites to email passwords back to users who clicked on the “I forgot my password” button.

## Reversibly encrypt everyone’s passwords

One weak response to this threat is to encrypt all passwords before storing them in the database. But it’s weak because the master password that allows the system to decrypt all of the user passwords has to be known to the system. If it weren’t, the system would not be able to log anyone in. So this defense only helps in a very narrow set of circumstances.

## Store hash of passwords

The important insight for secure password storage is to realize that you never have to store the password itself. Instead, you can store a value that’s derived from the password. You need a derivation that’s extremely unlikely to generate the same derived value for two different inputs. Initially, people used this insight by storing the output of generic hashing algorithms like MD5 and SHA-1 instead of the password itself. Then, when a user logged in, the hash output of the user-supplied input was compared to the previously stored hash output from when the user was created. If they’re the same, then the user is logged in. This was a step forward because the passwords themselves no longer had to be stored. So if the database were compromised, the passwords weren’t given up to the attacker directly.

# 6. More Techniques for Password Storage

## GPUs

Moore’s Law has altered the landscape in this cat-and-mouse game. The problem with using general-purpose hashing algorithms for password hashing is that general-purpose hashing algorithms are designed to be really fast. And Moore’s Law makes them faster all the time. Salting doesn’t increase the number of possibilities that need to be checked; salting only changes the set of possibilities that need to be checked from one population (all the printable passwords under, say, 10 characters) to another (that same set of passwords, each prefixed with the same prefix or salt.) This is very parallelizable and a great task for the many cores in a graphical processing unit (GPU) on a modern video card. Checking several billion passwords per second is well within reach.

Additionally, a dedicated password-cracking rig can achieve 350 billion passwords per second for Microsoft’s LM hashing algorithm.

Keep in mind that these two benchmarks describe the state of password cracking from 2013 and 2014, respectively. Cracking has only gotten faster since, due to Moore’s Law. So the defense against this is to use Moore’s Law to make defenses stronger over time. This is done with tunable password- hashing algorithms.

Tunable password-hashing algorithms can be thought of as carefully salted passwords that don’t just get hashed once. Instead, the password P is hashed to produce hash H1. Then H1 is hashed to produce H2. This is repeated tens of thousands of times. So a defender can decide how much time they’re willing to spend on password hashing at user login time. Something like a tenth of a second might be appropriate. The defender then works backward to see how many hashing iterations can fit in that amount of time. The login logic is then set up to hash that many times on each login. In approximately eighteen months, when Moore’s Law has kicked in again and made it easier to do that hashing operation, the defender can double the number of hashing iterations and maintain the level of security they had at the outset. The tunable nature of this defense is key. As time goes on, the defender can keep adjusting the number of hashing iterations to provide the desired performance/cost tradeoff.

## Password storage done right

Remember how easy it was to get crypto wrong, even if you knew enough to use AES? It’s nearly as easy to get hashing wrong. And, as is always the case with developing cryptographic software, the ways in which hashing goes wrong tend not to be obvious errors that prevent themselves as bugs. They tend to show up as attacks that make researchers famous. So if you’re looking at hashing passwords, you want to use a trustworthy implementation of one of the following algorithms:

1. bcrypt

2. scrypt

3. Argon2

4. PBKDF2

# 7. Storing Passwords When You’re the Client

So now we have four perfectly good password-hashing algorithms we can use. They’re so good it’s tempting to think that we’ve solved password storage for all use cases. Unfortunately, that’s not the case. We can only use these for hashing the passwords of clients that authenticate to us. If we need to authenticate to another system, we can’t use these password-hashing algorithms because they’re one-way only. We can never get the passwords back from a hash. So we’ll need another approach for storing passwords that we need to present to other systems.

## Storing passwords on servers

How should we store passwords that are used by our servers to connect to other servers? Perhaps we could encrypt them before we store them on disk. That sounds good, but it doesn’t buy us much. The problem is that the decryption key has to be available in the clear so that our application can decrypt the password in the config file at run time. So how do we protect that decryption key? Eventually, our applications need to have access to credentials in the clear.

The applications we build need to have access to the secrets they require in the clear. Whenever possible, we should run each application on a dedicated server running as a dedicated service account. For example, use separate accounts for your web server and database server, and only give the database account access to the database server.

If we can’t manage to put each application on a dedicated server, our only other option is to leverage OS permissions. We can use a separate OS account for each application that runs on a given server. This isn’t a very strong defense because operating system privilege escalation vulnerabilities are discovered all the time. We should consider a compromise of any account on a server to compromise the entire server. But in situations where multiple applications have to run on a single server, this can at least be a speed bump that slows down an attacker.

It can be worthwhile to use a key store like Azure Key Vault, AWS Key Management Service, or HashiCorp Vault. They don’t keep your secrets safer than not using them, since a compromise of a client of one of these key stores will result in compromised keys, just as would be the case if there were no key store in place. What the key stores provide is an audit trail of key access and key rotation. So by using these, you’ll have an easier time determining which hosts accessed which keys and when. You’ll also have a way to keep track of how often the keys have been rotated.

## Storing passwords on workstations

When it comes to passwords on workstations that you use to authenticate to other systems, use a password manager such as 1Password. The biggest benefit of this is that you’ll be able to use a separate password for every website you log into. This helps you because if one of the websites you use is compromised, the attackers won’t be able to use your password from one website to give them access to other websites. The next benefit is that you’ll be able to generate long passwords drawn from large alphabets. Password managers have fancy additional features like cloud-based sharing between devices. Only use these kinds of features if you must. Better to type them in by hand if you only have a couple of passwords to share between devices. Password managers also have fancy browser plugins to streamline the pasting of passwords into login forms. It’s better to not enable these and instead just copy and paste from 1Password. These plugins increase your attack surface but don’t add very much usability.



























