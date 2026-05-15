"""
core/pydantic_email_validator.py
Add email validation to Contact model
"""

from pydantic import BaseModel, field_validator


class Contact(BaseModel):
    name: str
    phone: str
    email: str
    
    @field_validator("name")
    @classmethod
    def name_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip().title()
    
    @field_validator("phone")
    @classmethod
    def phone_digits_only(cls, v: str) -> str:
        cleaned = ''.join(c for c in v if c.isdigit())
        if len(cleaned) < 7:
            raise ValueError("Phone must have at least 7 digits")
        return cleaned
    
    @field_validator("email")
    @classmethod
    def email_valid(cls, v: str) -> str:
        # Check for exactly one @ symbol
        if v.count("@") != 1:
            raise ValueError("Email must contain exactly one @ symbol")
        
        # Split into local and domain parts
        local, domain = v.split("@")
        
        # Check local part not empty
        if not local:
            raise ValueError("Email local part cannot be empty")
        
        # Check domain has at least one dot
        if "." not in domain:
            raise ValueError("Email domain must contain a dot")
        
        # Check domain parts not empty
        domain_parts = domain.split(".")
        if any(len(part) == 0 for part in domain_parts):
            raise ValueError("Email domain has empty parts")
        
        return v.lower().strip()


if __name__ == "__main__":
    # Valid emails
    valid_emails = [
        "user@example.com",
        "john.doe@example.co.uk",
        "alice@example.org"
    ]
    
    for email in valid_emails:
        try:
            contact = Contact(name="Test User", phone="1234567890", email=email)
            print(f"✅ Valid: {email}")
        except Exception as e:
            print(f"❌ Should be valid: {email} - {e}")
    
    print("\n--- Invalid emails ---")
    
    # Invalid emails
    invalid_emails = [
        "noatsign.com",           # No @
        "two@@atsigns.com",       # Two @
        "@missinglocal.com",      # Empty local
        "user@missingdot",        # No dot in domain
        "user@.com",              # Empty domain part
    ]
    
    for email in invalid_emails:
        try:
            contact = Contact(name="Test User", phone="1234567890", email=email)
            print(f"❌ Should be invalid: {email}")
        except Exception as e:
            print(f"✅ Caught error for {email}: {e}")