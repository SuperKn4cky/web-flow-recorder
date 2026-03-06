from __future__ import annotations

import secrets
from dataclasses import dataclass


@dataclass(frozen=True)
class SignupData:
    email: str
    password: str
    confirm_password: str
    accepted_terms: bool = True


def build_signup_data(domain: str = "example.test") -> SignupData:
    token = secrets.token_hex(4)
    password = f"Test!{secrets.token_hex(6)}"
    email = f"qa+{token}@{domain}"
    return SignupData(email=email, password=password, confirm_password=password)
