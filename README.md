<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Memory AI - Proof of Existence</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 50px;
        }
        
        h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .proof-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .timestamp {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        
        .timestamp-item {
            background: rgba(255,255,255,0.2);
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 1.1em;
        }
        
        .hash-container {
            background: rgba(0,0,0,0.3);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            word-break: break-all;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        
        .feature {
            background: rgba(255,255,255,0.1);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s;
        }
        
        .feature:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .verify-section {
            text-align: center;
            margin: 40px 0;
        }
        
        .verify-btn {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 15px 40px;
            border-radius: 30px;
            text-decoration: none;
            font-size: 1.1em;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(76,175,80,0.3);
        }
        
        .verify-btn:hover {
            background: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(76,175,80,0.4);
        }
        
        .legal-section {
            background: rgba(255,255,255,0.05);
            padding: 30px;
            border-radius: 15px;
            margin: 30px 0;
        }
        
        .legal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .legal-item {
            text-align: center;
        }
        
        .legal-icon {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            opacity: 0.8;
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 2em;
            }
            
            .proof-card {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔐 Memory AI</h1>
            <p class="subtitle">Proof of Existence - Certificato Blockchain</p>
        </header>
        
        <div class="proof-card">
            <h2>📄 Memory AI Whitepaper 2025</h2>
            
            <div class="timestamp">
                <div class="timestamp-item">
                    📅 14 Giugno 2025
                </div>
                <div class="timestamp-item">
                    🕐 22:35:52
                </div>
                <div class="timestamp-item">
                    🌍 UTC+2 (Europe/Rome)
                </div>
            </div>
            
            <h3>Hash SHA3-512:</h3>
            <div class="hash-container">
                8b449e14363f780bad89ada455c45cb5dded2e00392456c0ea90d6b8135dfd930e1faa326d01b3720fdddaadeb1771574ea2b84fa5daaf38d6d7a175b3415ccc
            </div>
        </div>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">✅</div>
                <h3>Proof of Existence</h3>
                <p>Prova immutabile che il documento esisteva in questa data</p>
            </div>
            
            <div class="feature">
                <div class="feature-icon">⏰</div>
                <h3>Timestamp Verificabile</h3>
                <p>Data e ora certificate sulla blockchain</p>
            </div>
            
            <div class="feature">
                <div class="feature-icon">🔒</div>
                <h3>Trasparenza Tecnologica</h3>
                <p>Sistema open source e verificabile pubblicamente</p>
            </div>
            
            <div class="feature">
                <div class="feature-icon">©️</div>
                <h3>Proprietà Intellettuale</h3>
                <p>Protezione legale del contenuto innovativo</p>
            </div>
        </div>
        
        <div class="verify-section">
            <h2>🔍 Verifica l'Autenticità</h2>
            <p style="margin: 20px 0;">Chiunque può verificare l'integrità del documento</p>
            <a href="https://github.com/DSalvadori/MemoryChain" class="verify-btn">
                Verifica su GitHub
            </a>
        </div>
        
        <div class="legal-section">
            <h2>🛡️ Protezioni Legali</h2>
            <div class="legal-grid">
                <div class="legal-item">
                    <div class="legal-icon">📜</div>
                    <h4>Prior Art</h4>
                    <p>Per brevetti e copyright</p>
                </div>
                
                <div class="legal-item">
                    <div class="legal-icon">⚖️</div>
                    <h4>Prova Forense</h4>
                    <p>Validità in tribunale</p>
                </div>
                
                <div class="legal-item">
                    <div class="legal-icon">🚫</div>
                    <h4>Anti-Plagio</h4>
                    <p>Protezione contro copie</p>
                </div>
                
                <div class="legal-item">
                    <div class="legal-icon">🔐</div>
                    <h4>Non Ripudiabile</h4>
                    <p>Timestamp immutabile</p>
                </div>
            </div>
        </div>
        
        <div class="proof-card" style="background: rgba(76,175,80,0.2);">
            <h3>✅ Cosa significa?</h3>
            <p style="margin-top: 15px; line-height: 1.6;">
                Questo certificato blockchain prova che il whitepaper Memory AI esisteva 
                il 14 Giugno 2025 alle 22:35:52. L'hash SHA3-512 garantisce che il 
                contenuto non è stato modificato. Questa è una prova legale valida per 
                dimostrare la priorità temporale e la proprietà intellettuale del documento.
            </p>
        </div>
        
        <footer>
            <p>Memory AI Team - Innovazione attraverso la Memoria 🧠</p>
            <p style="margin-top: 10px; font-size: 0.9em;">
                Powered by MemoryChain | CC BY-SA 4.0
            </p>
        </footer>
    </div>
    
    <script>
        // Animazione timestamp in tempo reale
        function updateLiveTime() {
            const now = new Date();
            const rome = now.toLocaleString('it-IT', { timeZone: 'Europe/Rome' });
            // Potresti aggiungere un elemento per mostrare l'ora corrente
        }
        
        // Copia hash al click
        document.querySelector('.hash-container').addEventListener('click', function() {
            const hash = this.textContent.trim();
            navigator.clipboard.writeText(hash).then(() => {
                alert('Hash copiato negli appunti!');
            });
        });
        
        // Effetto parallax leggero
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX / window.innerWidth;
            const y = e.clientY / window.innerHeight;
            
            document.body.style.background = `linear-gradient(${135 + x * 10}deg, 
                #1e3c72 0%, #2a5298 100%)`;
        });
    </script>
</body>
</html>
