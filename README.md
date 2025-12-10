# USDw – Regulated Stablecoin Prototype (Hyperledger Fabric + Python + Streamlit)

USDw is a fully functional **regulated stablecoin prototype** designed for academic, research, and demonstration purposes.  
The project showcases how a modern stablecoin can integrate:

- KYC / AML onboarding  
- Sanctions & freeze enforcement  
- 1:1 reserve-backed minting  
- On-chain compliance validation  
- Transaction history & auditability  
- Travel-rule hashing  
- Optional **Post-Quantum Security (Dilithium2)** signatures  
- A UI dashboard for real-time simulation  

The system includes both a **Hyperledger Fabric blockchain backend** and a **Python simulation layer** with a Streamlit user interface.

---

## 🚀 Features

### ✅ **Blockchain (Hyperledger Fabric Smart Contract)**
- Register accounts  
- Submit & verify KYC  
- Freeze / unfreeze wallet  
- Sanction / unsanction  
- Set reserve reports  
- Mint USDw  
- Transfer USDw with Travel-Rule Hash  
- Query ledger state  
- Get transaction history  

### ✅ **Python Engine (Regulated Logic Simulation)**
- Validates reserves ≥ supply  
- Enforces KYC before mint/transfer  
- Supports sanctions, freezes, travel rule  
- Optional **Dilithium2 PQC signatures** for metadata  
- Generates compliance events  

### ✅ **Streamlit Dashboard**
User-friendly UI where you can:
- Register and verify users  
- Set reserves  
- Mint tokens  
- Transfer tokens  
- Display PQC signature metadata  
- View full ledger simulation  

---

## 📁 Project Structure

usdw_track1_full_v2/
│
├── chaincode/
│ └── usdw/
│ ├── index.js
│ ├── package.json
│ └── lib/usdwContract.js
│
├── python_sim/
│ ├── engine.py
│ ├── pqc_mock.py (or Dilithium2-enabled version)
│ ├── scenarios.py
│ └── requirements.txt
│
└── ui/
└── app.py (Streamlit dashboard)

yaml
Copy code

---

## 🛠️ Setup Instructions

### 1️⃣ Clone The Repo

```bash
git clone https://github.com/<your-username>/usdw-stablecoin.git
cd usdw-stablecoin
2️⃣ Run the Python Simulation
bash
Copy code
cd python_sim
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python -m scenarios
3️⃣ Run the Streamlit Dashboard
bash
Copy code
cd ui
streamlit run app.py
4️⃣ Run the Hyperledger Fabric Network
bash
Copy code
cd ~/fabric-samples/test-network
./network.sh down
./network.sh up createChannel
Deploy USDw Chaincode:

bash
Copy code
./network.sh deployCC \
  -ccn usdw \
  -ccp <path-to-chaincode>/chaincode/usdw \
  -ccl javascript
🔐 Optional: Enable PQC (Post-Quantum Cryptography)
This project includes an optional Dilithium2-based module:

python
Copy code
from pqcrypto.sign.dilithium2 import generate_keypair, sign, verify
Used to:

Sign transaction metadata

Provide PQC hashes for Fabric

Demonstrate future-proof cryptographic design

🎓 Academic / Research Context
USDw was developed as part of a FinTech and Blockchain systems engineering project, demonstrating:

Stablecoin regulatory compliance

On-chain & off-chain coordination

Secure identity workflow

PQC resilience planning

End-to-end architecture from UI → Engine → Blockchain

📜 License
MIT License (you can change to Apache 2.0 if preferred)

✨ Author
Chetan Piraji Bhangare
M.S. Financial Technology (FinTech)
Worcester Polytechnic Institute (WPI)

