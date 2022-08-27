## Windows is common#

Odds are most of the computers where you work run Windows. So let’s take a look at some security advice that’s specific to Windows. Most of the advice in this chapter echoes more general advice from previous chapters, but we’ll see a couple of Windows-specific applications of that advice. We’ll also take a look at Mimikatz, a widely used tool for stealing Windows passwords, as well as some defenses against it.

## Windows users

We’re going to start out with some foundational Windows concepts before we move into best practices. Let’s start with users. There are two main types of interactive user accounts in Windows—administrators and standard users. Administrators are able to install software and make significant changes to the system. Standard users don’t have these permissions but are able to run installed software.

There is one other kind of user, but it’s not an interactive user. It’s called SYSTEM and it’s the user that does work on behalf of Windows itself. Because it works on behalf of the operating system, it has complete permissions to everything on that computer. We’ll come back to this a little later in the chapter.

# 1. Login and Mimikatz

## How Windows stores passwords

Let’s take a look at what happens when a user logs in. How does Windows know that you are who you say you are? You supply a password. But how does Windows know that it’s the right password? We saw in the cryptography chapter that systems that need to authenticate users should store password hashes, not the passwords themselves. Sure enough, Windows stores user password hashes, not the passwords themselves. Windows does this using a hashing algorithm called NTLM. Windows uses NTLM to generate a hash of the password that the user supplies at login time and compares it to the hash that’s been stored for that user. If it’s a local account, the known-good hash is stored on that computer. If it’s a domain account, then the computer will ask the domain controller whether the supplied hash is the right one.

## Mimikatz

Mimikatz is a tool that reads the password hashes that Windows keeps in memory. Due to the way that Windows stores these passwords, any user with administrator-level access to a Windows computer can read the password hashes of any other users that are logged in at the same time. And in earlier versions of Windows, such as Windows 7 and Windows 8.1, Mimikatz could also read the plaintext passwords of any logged-in users.

### Patching

We have a number of defenses available to us, the first of which is to keep up-to-date on patching. As long as we’re on Windows 8.1 or newer, Mimikatz should only be able to steal password hashes, not passwords themselves. In the chapter on patching, we focused on incremental security bug fixes as the main benefit to keeping up-to-date on patches. But there are also systemic improvements like this one. There is a registry setting that would make Windows store the actual passwords, not just the hashes, in memory. But you won’t have this enabled by default. And as your security posture improves, you’ll add endpoint monitoring to prevent settings like this from being enabled or to at least warn you if they’re changed.

### Network segmentation

Another defense against Mimikatz is better network segmentation. The workstations on your network should not generally need to communicate with each other via SMB on port 445. So block that at the router level. Then even if one workstation is compromised, the attacker won’t be able to jump from workstation to workstation looking for one with logged-in domain admins. There’s still need for domain administrators to use port 445 to administer machines on your network, so you’ll want to enable port 445 for communication initiated by admins; just block port 445 for communication initiated by other computers.

Since the attacker’s target is domain admin credentials, make those credentials harder to find by using them less often. If the domain admin credentials are only used when they’re absolutely needed, fewer machines will have domain admin credentials in memory and for shorter periods of time. This also provides a layer of defense against phishing. Domain admins aren’t immune to phishing attacks. If they always use their regular domain user to check email, then even if they get phished, they’ll only provide a regular domain account, not a domain admin account.

This gives us three different levels of access that administrators in your organization will need to have:

* Regular domain user for doing their day-to-day work, reading email, and so on

* Domain admin user for doing work that requires domain admin access, things like editing domain policies

* Local admin on other people’s workstations for administration and troubleshooting purposes

# 2. Password Policy

It’s a good idea to set a Windows policy that requires a long password for domain accounts. There are two main reasons for this. The first is the math of cracking passwords given an NTLM password hash. In contrast to the recommended password hashing algorithms that we saw in Password Storage Done Right, (bcrypt, scrypt, Argon2, and PBKDF2), the NTLM password hashing algorithm does not have a work factor associated with it. This means that an attacker who gets access to an NTLM password hash will be able to attempt to brute force it with a huge number of attempts per second. The NTLM algorithm is not going away any time soon. So our only other defense against this attack is to use a longer password.

## Password rotation

The last piece of a password rotation policy is password rotation frequency. Both GCHQ and NIST have recently released guidance about passwords. The takeaway that you’re likely to hear about is that these two organizations no longer call for enforcing regularly scheduled user password rotation.

## Other useful policies

What may get glossed over is that as a part of shifting the burden for effective password usage from users to site operators, they make additional suggestions, including the following:

* Enable a rate-limiting mechanism that effectively limits the number of failed authentication attempts that can be made on the subscriber’s account.

* Add support for all printable characters in passwords.

* Prevent users from using passwords known to be commonly used, expected, or compromised. Examples of such passwords include:

	* Passwords obtained from previous breach corpuses

	* Dictionary words

	* Repetitive or sequential characters (such as ‘aaaaaa’ and ‘1234abcd’)

	* Context-specific words, such as the name of the service, the username, and derivatives thereof

* Don’t provide password hints.

* Don’t allow for knowledge-based questions that come from publicly available data (ex: mother’s maiden name or name of a childhood friend) as part of handling a password reset.

* If 2FA is supported, provide at least one 2FA option that doesn’t use the public phone network.


# 3. Active Directory: What Else Is It Good For?

## Active Directory as a single point of access

We need to maintain Active Directory in order to run a Windows domain. Can we leverage that investment and get any other benefits from it? It turns out that we can. One of the best of these is the ability to disable access in a single place when someone leaves our organization or we learn that their account has been compromised.

## Caveats

In both of these cases, we see problems that arise from having a single, highly valuable store of hashed passwords. If that store of hashed passwords is compromised, whether through direct access to the password hashes, password reuse, or the memory of a disgruntled former employee, you have a big problem on your hands. How can we decrease the value of these credentials? One approach is to introduce two-factor authorization. We talked briefly about 2FA back in the Crypto chapter. Let’s get into a little more detail here.

## 2FA

When you set up a system to use 2FA for access, you split access between a password that the user remembers and a second, very short-lived password that an external device such as a smartphone app can generate on-demand. Someone who only has one of these factors can’t access the system without the other. With a system like this in place, even if a user’s password is leaked due to password reuse with third-party systems, the attacker won’t be able to log in because they won’t have access to the 2FA app, which generates the other part of the login credentials.


# 4. BitLocker

## Introduction

BitLocker is Microsoft’s full disk encryption (FDE) solution. It encrypts the entire file system transparently to the user and the applications. This is a defense against attackers with physical access, but since the file system is decrypted automatically once the system boots up, this doesn’t provide any defense against malware or attackers with access to the machine via stolen creds or that are exploiting vulnerable software running on the box.

## Sticky keys attack

The Sticky Keys functionality is an accessibility feature of Windows. It allows people who can’t physically press multiple keys on a keyboard at once to interact with their keyboard as though they could. One of the most common uses of this is to make use of the Shift key more accessible. Instead of requiring a user to physically press both the Shift key and a letter key at the same time in order to make a capital letter, when Sticky Keys is enabled, the system considers the Shift key to be held down until it is pressed a second time. It means more keystrokes, but none of them have to happen at the same time. In Windows, a small program called c:\windows\system32\sethc.exe configures whether or not Sticky Keys is enabled for the user currently logged in. The user runs this program by hitting the Shift key five times in a row.











