#Build a notification system with multiple channels

from datetime import datetime
import time

class Notification:
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.timestamp = datetime.now()
        self.is_sent = False

    def send(self):
        raise NotImplementedError(f"{type(self).__name__} must implement send()")

    def __str__(self):
        return f"[{type(self).__name__}] To: {self.recipient} | {self.subject}"


class EmailNotification(Notification):
    def __init__(self, recipient, subject, body, sender_email):
        super().__init__(recipient, subject, body)
        self.sender_email = sender_email

    def send(self):
        print(f"\n📧 EMAIL")
        print(f"   From: {self.sender_email}")
        print(f"   To:   {self.recipient}")
        print(f"   Subj: {self.subject}")
        print(f"   Body: {self.body}")
        self.is_sent = True


class SMSNotification(Notification):
    def __init__(self, recipient, subject, body, phone_number):
        super().__init__(recipient, subject, body)
        self.phone_number = phone_number

    def send(self):
        sms_body = self.body[:160]
        print(f"\n📱 SMS → {self.phone_number}: {sms_body}")
        self.is_sent = True


class PushNotification(Notification):
    def __init__(self, recipient, subject, body, device_token, badge_count=1):
        super().__init__(recipient, subject, body)
        self.device_token = device_token
        self.badge_count = badge_count

    def send(self):
        print(f"\n🔔 PUSH → {self.device_token[:12]}... | Badge: {self.badge_count}")
        self.is_sent = True


class RetryMixin:
    def send_with_retry(self, max_attempts=3, delay=1):
        for attempt in range(1, max_attempts + 1):
            try:
                print(f"  Attempt {attempt}/{max_attempts}...")
                self.send()
                print("  ✅ Sent successfully")
                return
            except Exception as e:
                print(f"  ❌ Attempt {attempt} failed: {e}")
                if attempt < max_attempts:
                    time.sleep(delay)
        raise RuntimeError(f"Failed after {max_attempts} attempts")


class ReliableEmailNotification(RetryMixin, EmailNotification):
    pass   # inherits everything from both parents

# Test
email = EmailNotification("alice@co.com", "Welcome!", "Hello Alice.", "noreply@app.com")
sms = SMSNotification("Bob", "Code", "Your OTP is 423891", "+44 7700 900 123")
email.send()
sms.send()

reliable = ReliableEmailNotification("carol@co.com", "Alert", "System OK", "alerts@app.com")
reliable.send_with_retry()