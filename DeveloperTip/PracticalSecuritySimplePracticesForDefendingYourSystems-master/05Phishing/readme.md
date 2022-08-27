### What is phishing?

Phishing is the first attack we’ve covered that attacks the user instead of the software. In a phishing attack, the attacker sends an email to the victim and tricks the victim into doing something the attacker wants them to do-generally, reveal their login credentials. Once an attacker has the victim’s credentials, they are no longer impeded by the defenses that we’ve carefully built up over the previous chapters.

No need for an attacker to look for unpatched servers, weak cryptography, or SQL injection if they can just log in and use the system as a legitimate user. It sounds simple, and it is technologically simpler than the attacks we’ve covered so far, but there’s no prize for complexity. Phishing continues to be a problem because it continues to be effective.

# 1. Types of Phishing Attacks

## Phished credentials

By far, the most common phishing attack is to steal login credentials. Generally, this is done by setting up a malicious website that looks the same as the login screen for Gmail, Outlook 365, Dropbox, or another popular website.

The phisher then sends a phishing email to the intended victim. The phishing email will contain a link to the malicious website as part of a message that claims that it’s important for the recipient to click on the link and log in. If the phisher is “lucky,” Pavlovian conditioning will kick in when the user sees what appears to be a familiar login screen and the user will submit their credentials to the malicious website.

Stolen credentials can be quite damaging. A phisher who has taken over an email account can probably trigger password resets for most of the other online services associated with that email address, like social media accounts and financial accounts. The phisher can exfiltrate old email.

If the phisher wants to take over the account, in general, they can reset the password for the email account to lock the victim out of the account. If the phisher wants to be stealthier, they can use the newly compromised email account to send further phishing emails to people in the compromised account’s address book and then delete them from the account to make it harder for the legitimate account owner to discover. These phishing emails will have added credibility because the new wave of victims will see the email as having been sent by someone they know. This credibility increases the likelihood that the recipient will click on the link and follow instructions to log in.

What do phishing emails look like? Many phishing emails are generic and are meant to be sent out widely. A common premise for these is the past-due invoice. These phishing emails create a sense of urgency by claiming that the victim is behind on payments and will get in trouble if they don’t pay right away. When these phishing emails are successful, the phisher will use the newly acquired credentials to resend the phishing email to people in the new victim’s contact list and continue the process. But a phisher who has a specific target in mind can tailor the phishing email.

After doing research about the company, an attacker can forge an email that, at first glance, appears to come from an important executive, customer, or vendor. The subject could pertain to recent company events. Phishing emails could be sent out in batches to see what gets the best responses in order to tweak later batches. Early waves of reconnaissance emails could be used to look for common email signatures or terminology that’s in use at the company.


## XSRF

If we think back to a section in the Vulnerabilities chapter, Cross-Site Request Forgery (XSRF), we see another attack vector for the successful phisher—XSRF.

Recall what an XSRF vulnerability on foo.com allows an attacker to do. It allows an attacker to target logged-in users of foo.com and get them to take whatever actions on foo.com the attacker wants them to. All the attacker needs to do is to get them to visit a URL that the attacker controls. Phishing is a great way for an attacker to get a victim to visit a URL that the attacker controls.

Put another way, if you’re logged in to your bank’s website and the bank’s website doesn’t defend against XSRF, and then you click on a link in a phishing email, the phisher can take over your browser to interact with the bank’s website. This includes transferring money, changing passwords, changing contact information, or anything else you’d be able to do while logged in.

If you’re building a website or a web app, then it’s important for you to prevent XSRF attacks in your site. If your site is vulnerable to XSRF, then if someone’s logged in to your app while also reading email, there’s a clear path for attackers to take over your web app—they just email people who are logged in.

This attack is more tailored and a lot more work for the phisher, so you’re much less likely to encounter this in practice.

## Social engineering

Social engineering is a less technical type of attack. In this kind of attack, a phisher would pretend to be someone they’re not and ask for things they shouldn’t have—HR records, banking information, passwords, and so on. This kind of attack is different because it probably won’t contain a link to a malicious or XSRF-vulnerable website. It probably just comes out and asks the intended victim to do something on behalf of the phisher.

## Malware

Malware-based phishing emails are the least likely attack. It’s comparatively hard to write custom malware to attack phishing victims. Most of the time phishers are just after credentials anyway. And the odds of stealing credentials are so high that it’s generally not worth the effort to try to develop custom malware. Most phishers just increase their chances for success by sending out more phishing emails.

There are two kinds of malware-based phishing attacks. By far the most common is the phishing email that contains a malware attachment and a pretense for why the recipient should execute the attachment. Generally, these are just Microsoft Office documents with embedded macros that open a credential harvesting website. They tend not to be sophisticated. These can be avoided with proper training. The other kind of malware-based phishing attack is the one that attacks the email client itself. It is difficult to find vulnerabilities in email clients, so writing malware that targets vulnerabilities in specific mail clients is expensive, time-consuming, and only viable against users of specific mail clients. Because of this, phishing that targets mail clients is very rare and generally only attempted by sophisticated attackers like nation-states. For a funny take on the difference between nation-state attackers and everyone else, take a look at James Mickens’s hilarious “This World of Ours.” It’s not the most actionable essay I link to in this course, but it’s definitely the funniest.

# 2. Social Defense

You’ll want to provide training for the people in your organization so they develop a healthy level of skepticism toward incoming email. You can put the training together yourself or hire an outside firm. Your best defense is vigilant colleagues. Most phishing attacks spread a wide net, so increasing the likelihood that even one person notices the deception allows you to respond and get the word out sooner. We’ll cover phishing responses later in this chapter.

Here are the basic points you’ll want to emphasize in your anti-phishing training.

* Don’t embarrass your colleagues.

* Be extra skeptical about emails with urgent deadlines.

* Be suspicious of strange-looking domains in links and email addresses.

* Be skeptical about attachments.

* Consider whether the premise of the email makes sense.

## Don’t DIY

Before we get into DNS-based defenses, here’s a simple piece of advice about email hosting—don’t do it yourself. Just host your company’s email with G Suite from Google. (Ok, you could also pick Outlook 365 if you like Microsoft. There are other email hosting options, but I don’t believe any of them are able to put as many resources into security as these two companies do.) It’s a lot of work just to keep a mail server up and running with the reliability that email requires. It’s even more work to keep it patched and configured securely. Maintaining a mail server is a full-time job. And if you want support on holidays, weekends, evenings, and sick days, it’s a full-time job for more than one person.

If your organization is just starting out, you have much better ways to use your employees’ time than maintaining a mail server. Even if you’ve grown to 200 employees and use Google’s most expensive hosting plan, you’d still spend less on G Suite than the cost of a single US-based full-time engineer. All three of the DNS tools we’ll cover work with G Suite but aren’t enabled out of the box. It’s pretty straightforward to enable them as long as you have permissions to edit DNS records for your domain. G Suite maintains good documentation on all three of these tools.

# 3. Authentication-Based Defense

## 2FA

In a traditional login, a user supplies a username and password to authenticate themselves to the system. In this scenario, the password is the single factor the system uses to decide whether to authenticate the user or not. That works fine until the password becomes known to an attacker. This disclosure lets the attacker log in as a legitimate user. If the system had a second factor to be used in addition to the password, then disclosure of the password would not compromise the account. This is the idea behind two-factor authentication (2FA).

## TOTP

The most common type of 2FA is a time-based one-time password (TOTP). In a TOTP system, the server and the client share a second secret in addition to the password. During login, after the user submits the password, the user uses the 2FA application, which uses the current time and the shared secret to generate the time-based one-time password. The user submits this second password, and the server, which knows the current time and remembers the shared secret, can perform the same derivation and make sure that the second factor is correct.

## TOTP Limitations

Adding 2FA to our logins can provide some defense against phishing. An attacker might steal a username and password, but without the second factor, they can’t log in. This stops the effectiveness of simple password theft and can make attempts to use the newly stolen password stand out. But, depending on the type of deception used in the phishing email, it might not be enough to stop a more sophisticated attacker.

Consider a phishing campaign where the phisher wants to exfiltrate data out of a web-based system that’s protected by 2FA. All the phisher needs to do in addition to the normal credential stealing is to convince the user that they need to supply the second factor as well. This can be done with a Man-in-the-Middle style attack. The phishing email will contain a link to a login look-alike web page under the phisher’s control, just as in a normal phishing email. This page will then steal the username and login, store it, submit those credentials to the legitimate login site, and present the user with a lookalike 2FA button. Since the legitimate login site received valid credentials, it will challenge the legitimate user with the 2FA challenge button. But in this scenario, the user already thinks they need to log in. They’re expecting the 2FA challenge, so they supply the second factor, thinking that it’s authenticating the login process they’re seeing on their screen. But instead, it’s authenticating the login process initiated by the phisher’s website.

The presence of 2FA makes this attack harder to pull off. There are more moving parts, there is a second opportunity for the user to decide not to authenticate, and the legitimate website will know the IP address that the phishing site is connecting from, which could raise alarms. But these challenges for the phisher are only speed bumps. None of them actually prevent the attack.

## Prefer non–SMS-based 2FA

There are a variety of 2FA options. Apps that run on your smartphone seem to be the most popular. Some of the smartphone-based 2FA apps communicate over SMS, which isn’t ideal. Phone companies can be social-engineered into making account changes. And attacks on the cell phone network itself are possible.

You’re still much better off with SMS-based 2FA than with no second factor. But if you have the choice, pick a non-SMS system. Requiring 2FA for logins helps decrease the value of stolen credentials. It also helps in the face of credential-stuffing attacks.

## U2F

U2F is a more advanced form of 2FA. It is an open standard designed to address a couple of the shortcomings of typical 2FA. First, U2F is not phishable. Whereas a TOTP client trusts the server implicitly and hands over the TOTP automatically, a U2F client performs a handshake, not unlike the TLS handshake. This lets the server and the client authenticate each other. If the server is an imposter (as is the case in phishing attacks), it will fail this authentication step and won’t gain anything that will help it log in to the website it’s impersonating. Second, U2F clients are small, purpose-built devices. The most popular variety is the YubiKey line of U2F devices from Yubico. They’re generally about the size of a small USB thumb drive. They only have the ability to perform the U2F handshake. They don’t have a full-featured operating system with the ability to run apps like a smartphone, so they’re much harder for an attacker to compromise. Typical TOTP 2FA applications run on either a phone or a regular computer. If either the phone or the computer were to be compromised through targeted malicious software, the 2FA app could become compromised too.








