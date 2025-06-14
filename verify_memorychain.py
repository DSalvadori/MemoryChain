#!/usr/bin/env python3
"""
Script di verifica per MemoryChain
Permette a chiunque di verificare l'integrità e autenticità dei documenti
"""

import hashlib
import json
import os
from datetime import datetime

def verify_document_hash(file_path, expected_hash, algorithm="SHA3-512"):
    """Verifica che l'hash del documento corrisponda"""
    if algorithm == "SHA3-512":
        hash_obj = hashlib.sha3_512()
    else:
        raise ValueError(f"Algoritmo non supportato: {algorithm}")
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                hash_obj.update(chunk)
        
        calculated_hash = hash_obj.hexdigest()
        is_valid = calculated_hash == expected_hash
        
        return {
            "valid": is_valid,
            "calculated_hash": calculated_hash,
            "expected_hash": expected_hash,
            "algorithm": algorithm
        }
    except FileNotFoundError:
        return {
            "valid": False,
            "error": f"File non trovato: {file_path}"
        }

def verify_block_integrity(block_data):
    """Verifica l'integrità del blocco"""
    # Rimuovi il block_hash per ricalcolarlo
    block_copy = block_data.copy()
    stored_hash = block_copy.pop("block_hash", None)
    
    # Ricalcola l'hash del blocco
    block_content = json.dumps(block_copy, sort_keys=True, indent=2)
    calculated_hash = hashlib.sha3_256(block_content.encode()).hexdigest()
    
    return {
        "valid": calculated_hash == stored_hash,
        "calculated_hash": calculated_hash,
        "stored_hash": stored_hash
    }

def verify_pgp_signature(signature_data):
    """Verifica la firma PGP (placeholder per implementazione reale)"""
    # In un sistema reale, qui si userebbe GPG per verificare la firma
    if "-----BEGIN PGP SIGNATURE-----" in signature_data:
        return {
            "status": "signature_present",
            "note": "Verifica PGP richiede GPG installato e chiave pubblica",
            "signature_format": "valid"
        }
    return {
        "status": "no_signature",
        "signature_format": "invalid"
    }

def generate_verification_report(block_file, document_file=None):
    """Genera un report completo di verifica"""
    print("=== MemoryChain Verification Report ===\n")
    
    # 1. Carica il blocco
    try:
        with open(block_file, 'r', encoding='utf-8') as f:
            block_data = json.load(f)
        print(f"✅ Blocco caricato: {block_file}")
    except Exception as e:
        print(f"❌ Errore caricamento blocco: {e}")
        return
    
    # 2. Verifica integrità del blocco
    print("\n📋 Verifica Integrità Blocco:")
    block_integrity = verify_block_integrity(block_data)
    if block_integrity["valid"]:
        print("   ✅ Integrità blocco verificata")
        print(f"   Hash: {block_integrity['stored_hash'][:32]}...")
    else:
        print("   ❌ Integrità blocco compromessa!")
        print(f"   Expected: {block_integrity['stored_hash']}")
        print(f"   Got: {block_integrity['calculated_hash']}")
    
    # 3. Verifica hash documento (se fornito)
    if document_file and os.path.exists(document_file):
        print("\n📄 Verifica Hash Documento:")
        doc_hash_info = block_data["document"]["hash"]
        doc_verification = verify_document_hash(
            document_file, 
            doc_hash_info["value"],
            doc_hash_info["algorithm"]
        )
        
        if doc_verification["valid"]:
            print("   ✅ Hash documento verificato")
            print(f"   Algoritmo: {doc_verification['algorithm']}")
            print(f"   Hash: {doc_verification['expected_hash'][:32]}...")
        else:
            print("   ❌ Hash documento non corrisponde!")
    else:
        print("\n📄 Verifica Hash Documento:")
        print("   ⚠️  Documento non fornito - impossibile verificare hash")
    
    # 4. Verifica firma PGP
    print("\n🔐 Verifica Firma PGP:")
    pgp_result = verify_pgp_signature(block_data["signature"]["signature_data"])
    print(f"   Status: {pgp_result['status']}")
    if pgp_result.get("note"):
        print(f"   Nota: {pgp_result['note']}")
    
    # 5. Informazioni blocco
    print("\n📊 Informazioni Blocco:")
    print(f"   Numero: {block_data['block_number']}")
    print(f"   Timestamp: {block_data['timestamp']}")
    print(f"   Documento: {block_data['document']['name']}")
    print(f"   Versione: {block_data['document']['version']}")
    print(f"   Licenza: {block_data['metadata']['license']}")
    
    # 6. Genera proof di verifica
    verification_proof = {
        "verification_timestamp": datetime.now().isoformat(),
        "block_file": block_file,
        "block_integrity": block_integrity["valid"],
        "document_hash_verified": doc_verification["valid"] if document_file else None,
        "signature_present": pgp_result["status"] == "signature_present",
        "verifier": "MemoryChain Verification Tool v1.0"
    }
    
    # Salva proof di verifica
    proof_file = block_file.replace('.json', '_verification_proof.json')
    with open(proof_file, 'w', encoding='utf-8') as f:
        json.dump(verification_proof, f, indent=2)
    
    print(f"\n✅ Proof di verifica salvato: {proof_file}")
    
    return verification_proof

def main():
    """Funzione principale"""
    print("MemoryChain Verification Tool v1.0\n")
    
    # Percorsi dei file
    block_file = "block_0001.json"
    document_file = "../memory-ai-whitepaper-2025.pdf"
    
    # Genera report di verifica
    verification_proof = generate_verification_report(block_file, document_file)
    
    if verification_proof:
        print("\n" + "="*50)
        if verification_proof["block_integrity"] and verification_proof.get("document_hash_verified"):
            print("🎉 VERIFICA COMPLETATA CON SUCCESSO!")
        elif verification_proof["block_integrity"]:
            print("⚠️  Verifica parziale - blocco integro ma documento non verificato")
        else:
            print("❌ VERIFICA FALLITA - Integrità compromessa")

if __name__ == "__main__":
    main()
