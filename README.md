# 🔗 MemoryChain - Blockchain per Memory AI

## 📋 Panoramica

MemoryChain è il sistema blockchain proprietario di Memory AI per garantire l'integrità, autenticità e tracciabilità di tutti i documenti critici del progetto.

## 🏗️ Struttura

```
MemoryChain/
├── block_0001.json              # Primo blocco con whitepaper firmato
├── block_0001_verification_proof.json  # Proof di verifica
├── calculate_hash_and_sign.py   # Script per creare nuovi blocchi
├── verify_memorychain.py        # Script di verifica pubblica
├── memorychain_deployment_guide.md  # Guida al deployment
└── README.md                    # Questo file
```

## 🔐 Caratteristiche di Sicurezza

### Hash Crittografici
- **SHA3-512** per i documenti (resistente a collisioni)
- **SHA3-256** per i blocchi della catena
- Hash calcolati su file binari completi

### Firma Digitale
- **PGP/GPG** per autenticazione
- Chiave pubblica per verifica
- Chiave privata mai condivisa

### Integrità della Catena
- Ogni blocco referenzia il precedente
- Hash del blocco include tutti i metadati
- Timestamp immutabile

## 📊 Dati del Primo Blocco

```json
{
  "block_number": 1,
  "document": "memory-ai-whitepaper-2025.pdf",
  "hash_algorithm": "SHA3-512",
  "hash_value": "8b449e14363f780bad89ada455c45cb5dded2e00392456c0ea90d6b8135dfd930e1faa326d01b3720fdddaadeb1771574ea2b84fa5daaf38d6d7a175b3415ccc",
  "signature": "PGP signed",
  "license": "CC BY-SA 4.0"
}
```

## 🚀 Come Usare

### 1. Verificare un Documento
```bash
cd MemoryAI_Docs/docs/WhitePaper/MemoryChain
python verify_memorychain.py
```

### 2. Aggiungere un Nuovo Documento
```python
# Modifica calculate_hash_and_sign.py con:
# - Percorso del nuovo documento
# - Metadati appropriati
# - Riferimento al blocco precedente
python calculate_hash_and_sign.py
```

### 3. Pubblicare su GitHub
```bash
git add block_*.json
git commit -m "Add new MemoryChain block"
git push origin main
```

## 🌐 Opzioni di Pubblicazione

### Fase 1: GitHub (Immediata) ✅
- Repository pubblico o privato
- Timestamp Git verificabile
- Facile accesso

### Fase 2: IPFS (Prossima)
```bash
ipfs add block_0001.json
# Pin su servizi come Pinata per persistenza
```

### Fase 3: Blockchain Pubblica (Futura)
- Smart contract su Polygon/Ethereum
- Immutabilità garantita
- Costo per transazione

## ❓ FAQ

### È sicuro pubblicare gli hash?
**Sì!** Gli hash SHA3-512 sono unidirezionali. È computazionalmente impossibile ricostruire il documento originale dall'hash.

### Cosa succede se perdo la chiave PGP?
Mantieni sempre backup sicuri della chiave privata. La chiave pubblica può essere distribuita liberamente per la verifica.

### Posso modificare un blocco esistente?
**No!** I blocchi sono immutabili per design. Per aggiornamenti, crea un nuovo blocco che referenzia il precedente.

### Come verifico l'autenticità?
1. Scarica il documento originale
2. Calcola l'hash SHA3-512
3. Confronta con l'hash nel blocco
4. Verifica la firma PGP (se hai la chiave pubblica)

## 📈 Roadmap

- [x] Creazione primo blocco
- [x] Script di verifica
- [ ] Integrazione GPG reale
- [ ] Pubblicazione su IPFS
- [ ] Smart contract Ethereum/Polygon
- [ ] Explorer web per MemoryChain
- [ ] API REST per verifica programmatica

## 🤝 Contribuire

Per aggiungere documenti alla MemoryChain:
1. Fork del repository
2. Crea nuovo blocco con script
3. Verifica integrità
4. Pull request con motivazione

## 📜 Licenza

MemoryChain è rilasciata sotto licenza MIT.
I documenti nella catena mantengono le loro licenze originali (vedi metadati).

---

**Memory AI Team** - Innovazione attraverso la Memoria 🧠
