# pqc_mock.py  (now using real Dilithium2 signatures)

import json

# 🔐 Real post-quantum signatures (Dilithium2)
from pqcrypto.sign.dilithium2 import generate_keypair, sign as pqc_sign, verify as pqc_verify

# --------------------------------------------------------------------
# Generate a module-level Dilithium2 keypair when this file loads.
# This simulates "wallet PQC keys" for demo purposes.
# --------------------------------------------------------------------
_public_key, _secret_key = generate_keypair()


def keygen():
    """
    For compatibility with your existing code.
    Returns the generated Dilithium2 public and secret keys as hex.
    """
    return {
        "pk": _public_key.hex(),
        "sk": _secret_key.hex(),
    }


def sign(message_obj):
    """
    Sign a JSON message using Dilithium2.
    Returns signature as hex string.
    """
    blob = json.dumps(message_obj, sort_keys=True).encode("utf-8")
    sig_bytes = pqc_sign(_secret_key, blob)
    return sig_bytes.hex()


def verify(message_obj, signature):
    """
    Verify Dilithium2 signature (hex).
    Returns True/False.
    """
    blob = json.dumps(message_obj, sort_keys=True).encode("utf-8")
    sig_bytes = bytes.fromhex(signature)

    try:
        pqc_verify(_public_key, blob, sig_bytes)
        return True
    except Exception:
        return False
